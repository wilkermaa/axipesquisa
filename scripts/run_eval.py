#!/usr/bin/env python3
"""Reproducible AXI benchmark runner. NO credentials in source/logs. Requires explicit paid-run consent.

The 'axi' arm is a *prompt-equivalent* API condition, NOT an actual installed Skill test.
Web user interface acceptance must be tested separately. External searches/tools are disabled.
"""
import argparse, hashlib, json, os, random, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CASES=ROOT/'tests/cases.json'
SKILL=ROOT/'skill/axipesquisa'
CONDITIONS=('baseline','generic','axi')
GENERIC=('Responda em português de forma clara e organizada. Quando útil, explique conceitos, use exemplos e seja conciso. '
         'Baseie afirmações em evidências disponíveis, evite inventar fontes ou fatos. '
         'Respeite rigorosamente o formato solicitado pelo usuário.')
BASE='Você é um assistente prestativo. Responda ao pedido em português, respeitando os requisitos do usuário.'
PROVIDER_KEYS={'openai':'OPENAI_API_KEY','anthropic':'ANTHROPIC_API_KEY',
               'gemini':'GEMINI_API_KEY','xai':'XAI_API_KEY'}

def sha(v):return hashlib.sha256(v.encode('utf-8')).hexdigest()

def axi_instructions():
    parts=[(SKILL/'SKILL.md').read_text(encoding='utf-8')]
    for p in sorted((SKILL/'references').glob('*.md')):
        parts.append('\n## Material auxiliar: '+p.name+'\n'+p.read_text(encoding='utf-8'))
    return '\n'.join(parts)

def system_prompt(condition):
    if condition=='baseline':return BASE
    if condition=='generic':return BASE+'\n\n'+GENERIC
    if condition=='axi':return BASE+'\n\n'+axi_instructions()
    raise ValueError(condition)

def prepare(args):
    cases=json.loads(CASES.read_text(encoding='utf-8'))
    rng=random.Random(args.seed)
    jobs=[{'case_id':c['id'],'category':c['category'],'prompt':c['prompt'],
           'condition':v, 'repeat':rep, 'provider':args.provider,'model':args.model,
           'test_mode':'prompt-equivalent-no-tools'}
          for c in cases for rep in range(1,args.repeats+1) for v in CONDITIONS]
    rng.shuffle(jobs)
    for job in jobs:
        job['job_id']=sha('|'.join([job['provider'],job['model'],job['case_id'],
                                  str(job['repeat']),job['condition']]))[:24]
        job['prompt_sha256']=sha(job['prompt'])
        job['system_sha256']=sha(system_prompt(job['condition']))
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in jobs),encoding='utf-8')
    print(json.dumps({'status':'manifest-ready-no-inference-executed','file':str(dest),'jobs':len(jobs),
                      'cases':len(cases),'conditions':list(CONDITIONS),'provider':args.provider,
                      'model':args.model,'repeats':args.repeats,'seed':args.seed},ensure_ascii=False))

def call_api(provider,model,system,user,timeout):
    token=os.environ[PROVIDER_KEYS[provider]]
    if provider in ('openai','xai'):
        host={'openai':'https://api.openai.com/v1/chat/completions',
              'xai':'https://api.x.ai/v1/chat/completions'}[provider]
        payload={'model':model,'messages':[{'role':'system','content':system},
                                            {'role':'user','content':user}]}
        headers={'Authorization':'Bearer '+token}
    elif provider=='anthropic':
        host='https://api.anthropic.com/v1/messages'
        payload={'model':model,'max_tokens':1800,'system':system,
                 'messages':[{'role':'user','content':user}]}
        headers={'x-api-key':token,'anthropic-version':'2023-06-01'}
    else:
        host='https://generativelanguage.googleapis.com/v1beta/models/'+urllib.parse.quote(model,safe='')+':generateContent'
        payload={'systemInstruction':{'parts':[{'text':system}]},
                 'contents':[{'role':'user','parts':[{'text':user}]}],
                 'generationConfig':{'maxOutputTokens':1800}}
        headers={'x-goog-api-key':token}
    raw=json.dumps(payload,ensure_ascii=False).encode('utf-8')
    req=urllib.request.Request(host,data=raw,headers={'Content-Type':'application/json',**headers},method='POST')
    with urllib.request.urlopen(req,timeout=timeout) as resp:
        data=json.loads(resp.read().decode('utf-8'))
    if provider in ('openai','xai'):
        c=data['choices'][0]['message']['content']
        value=c if isinstance(c,str) else '\n'.join(p.get('text','') for p in c if isinstance(p,dict))
        usage=data.get('usage')
    elif provider=='anthropic':
        value='\n'.join(p.get('text','') for p in data['content'] if p.get('type')=='text')
        usage=data.get('usage')
    else:
        value='\n'.join(p.get('text','') for part in data.get('candidates',[])[:1]
                         for p in part.get('content',{}).get('parts',[]) if 'text' in p)
        usage=data.get('usageMetadata')
    if not value.strip(): raise RuntimeError('Empty model response (or unsupported content shape)')
    return value,usage

def run(args):
    if not args.confirm_billable: raise SystemExit('Blocked: pass --confirm-billable only when you authorize API charges.')
    jobs=[json.loads(x) for x in Path(args.input).read_text(encoding='utf-8').splitlines() if x.strip()]
    if not jobs:raise SystemExit('Empty manifest')
    provider=jobs[0]['provider'];model=jobs[0]['model']
    if not all(j['provider']==provider and j['model']==model for j in jobs):raise SystemExit('Mixed provider/model not allowed')
    key=PROVIDER_KEYS[provider]
    if not os.getenv(key):raise SystemExit('Missing '+key+' in execution environment; no API calls made.')
    dest=Path(args.output); dest.parent.mkdir(parents=True,exist_ok=True)
    seen=set()
    if dest.exists():
        for line in dest.read_text(encoding='utf-8').splitlines():
            try:
                r=json.loads(line)
                if r.get('status')=='ok':seen.add(r['job_id'])
            except json.JSONDecodeError:continue
    attempts=0;success=0
    with dest.open('a',encoding='utf-8') as f:
        for j in jobs:
            if j['job_id'] in seen:continue
            if args.max_calls and attempts>=args.max_calls:break
            attempts+=1; start=time.monotonic()
            r={k:j[k] for k in ['job_id','case_id','category','prompt','condition','repeat','provider','model','test_mode','prompt_sha256','system_sha256']}
            r['timestamp_utc']=datetime.now(timezone.utc).isoformat()
            try:
                if j['system_sha256']!=sha(system_prompt(j['condition'])):
                    raise RuntimeError('Skill/instruction changed after manifest generation; regenerate manifest.')
                answer,usage=call_api(provider,model,system_prompt(j['condition']),j['prompt'],args.timeout)
                r.update({'status':'ok','response':answer,'usage':usage});success+=1
            except (urllib.error.URLError,urllib.error.HTTPError,RuntimeError,KeyError,ValueError) as ex:
                # Sanitize HTTP exception; never capture request headers or API tokens.
                r.update({'status':'error','error_type':type(ex).__name__,
                          'error':'Provider request failed or response was invalid; see local API diagnostics.'})
            r['elapsed_seconds']=round(time.monotonic()-start,3)
            f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
    print(json.dumps({'status':'execution-finished','attempted':attempts,'success':success,
                      'errors':attempts-success,'output':str(dest),'resume_supported':True},ensure_ascii=False))

def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='action',required=True)
    a=sub.add_parser('prepare',help='prepare randomized 36x3xN calls, no API use')
    a.add_argument('--provider',choices=PROVIDER_KEYS,required=True)
    a.add_argument('--model',required=True)
    a.add_argument('--repeats',type=int,default=2)
    a.add_argument('--seed',type=int,default=20261104)
    a.add_argument('--output',default='evals/manifest.jsonl')
    a.set_defaults(func=prepare)
    b=sub.add_parser('run',help='send billable requests from manifest')
    b.add_argument('--input',required=True);b.add_argument('--output',required=True)
    b.add_argument('--confirm-billable',action='store_true',required=True)
    b.add_argument('--max-calls',type=int,default=0,help='0=all; small N recommended for smoke test')
    b.add_argument('--timeout',type=int,default=120);b.set_defaults(func=run)
    args=p.parse_args()
    if getattr(args,'repeats',1)<1 or getattr(args,'max_calls',0)<0: p.error('Invalid counts')
    args.func(args)
if __name__=='__main__':main()
