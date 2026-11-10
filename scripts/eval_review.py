#!/usr/bin/env python3
"""Blind review pack and analysis: no model calls; only real responses and human ratings."""
import argparse,csv,hashlib,json,random,statistics
from pathlib import Path
RUBRIC=('factual','whole_parts','analogy_limits','integration','clarity','format','sources','safety')

def load(path):return [json.loads(s) for s in Path(path).read_text(encoding='utf-8').splitlines() if s.strip()]

def pack(args):
    results=[r for r in load(args.input) if r.get('status')=='ok']
    rng=random.Random(args.seed)
    rng.shuffle(results)
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    mapping=[]
    with (out/'blind_responses.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['blind_id','case_id','category','prompt','response']);w.writeheader()
        for idx,r in enumerate(results,1):
            bid=f'B{idx:05d}'
            w.writerow({k:v for k,v in {'blind_id':bid,'case_id':r['case_id'],'category':r['category'],
                                        'prompt':r['prompt'],'response':r['response']}.items()})
            mapping.append({'blind_id':bid,'job_id':r['job_id'],'case_id':r['case_id'],
                            'condition':r['condition'],'provider':r['provider'],
                            'model':r['model'],'repeat':r['repeat']})
    (out/'PRIVATE_BLIND_KEY.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (out/'ratings_template.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['blind_id','reviewer']+list(RUBRIC)+['critical_failure','notes']);w.writeheader()
        for item in mapping:w.writerow({'blind_id':item['blind_id'],'reviewer':''})
    (out/'README.txt').write_text('ATENÇÃO: PRIVATE_BLIND_KEY.json identifica condição e não deve ser entregue aos avaliadores.\n'
                                  'Notas 0-4 (maior=melhor); deixe vazio se não se aplica. Dois avaliadores independentes.\n'
                                  'critical_failure: 1 se falha grave verificada, 0 caso contrário.\n'
                                  'As marcas AXI no texto podem revelar o grupo: cegamento parcial.\n',encoding='utf-8')
    print(json.dumps({'responses':len(results),'directory':str(out),'status':'blind-pack-ready-no-human-ratings'},ensure_ascii=False))

def aggregate(args):
    key={x['blind_id']:x for x in json.loads(Path(args.key).read_text(encoding='utf-8'))}
    with Path(args.ratings).open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    by={};bad=[]
    for r in rows:
        ident=r['blind_id'];item=key.get(ident)
        if not item:bad.append(ident);continue
        if not r.get('reviewer'):continue
        pts=[]
        for criterion in RUBRIC:
            v=(r.get(criterion) or '').strip()
            if v:
                score=int(v)
                if score<0 or score>4:raise ValueError('Score outside [0,4]')
                pts.append(score)
        if not pts:continue
        x={**item,'reviewer':r['reviewer'],'score_mean':statistics.mean(pts),
           'scored_dimensions':len(pts),'critical_failure':(r.get('critical_failure')=='1')}
        by.setdefault(ident,[]).append(x)
    summarized=[]
    for ident,rs in by.items():
        if len({x['reviewer'] for x in rs})<args.min_reviewers:continue
        m=statistics.mean(x['score_mean'] for x in rs)
        summarized.append({**key[ident],'rating':m,'critical_failure':any(x['critical_failure'] for x in rs),
                           'reviewers':len({x['reviewer'] for x in rs})})
    def diff(condition):
        groups={}
        for x in summarized:
            g=(x['provider'],x['model'],x['case_id'],x['repeat'])
            groups.setdefault(g,{})[x['condition']]=x['rating']
        pairs=[(g,v['axi']-v[condition]) for g,v in groups.items() if 'axi' in v and condition in v]
        if not pairs:return {'pairs':0,'mean_difference':None,'ci95':None}
        mean=statistics.mean(x for _,x in pairs)
        # Case-level cluster bootstrap, not independent-item confidence intervals.
        bycase={}
        for g,v in pairs:bycase.setdefault((g[0],g[1],g[2]),[]).append(v)
        values=list(bycase.values());rng=random.Random(20261104);boot=[]
        for _ in range(2000):
            sample=[rng.choice(values) for _ in values]
            boot.append(statistics.mean(y for z in sample for y in z))
        boot.sort();return {'pairs':len(pairs),'mean_difference':round(mean,3),
                            'ci95':[round(boot[50],3),round(boot[1949],3)]}
    report={'status':'human-review-analysis','response_count_with_required_reviews':len(summarized),
            'min_reviewers':args.min_reviewers,'unknown_ids':bad,
            'comparisons':{'axi_vs_baseline':diff('baseline'),'axi_vs_generic':diff('generic')},
            'critical_failures_by_condition':{c:sum(x['critical_failure'] for x in summarized if x['condition']==c)
                                              for c in ['baseline','generic','axi']},
            'note':'Exploratory only; not proof of causal effects or universal superiority. Case-level cluster bootstrap; model and prompt equivalence limitations apply.'}
    Path(args.output).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))

def main():
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='action',required=True)
    a=s.add_parser('prepare');a.add_argument('--input',required=True);a.add_argument('--output',required=True)
    a.add_argument('--seed',type=int,default=20261104);a.set_defaults(func=pack)
    b=s.add_parser('aggregate');b.add_argument('--key',required=True);b.add_argument('--ratings',required=True)
    b.add_argument('--output',required=True);b.add_argument('--min-reviewers',type=int,default=2);b.set_defaults(func=aggregate)
    args=p.parse_args();args.func(args)
if __name__=='__main__':main()
