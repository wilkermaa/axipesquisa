#!/usr/bin/env python3
"""Narrow deterministic oracles for a subset of test cases; NOT proof of general quality."""
import argparse,ast,csv,io,json
from pathlib import Path
STRICT={'T17','T18','T19','T20','T29','T34'}

def check(case,answer):
    raw=answer.strip()
    if case not in STRICT:return {'status':'requires-human-review','passed':None}
    if case=='T17':
        try: ok=json.loads(raw)=={'resultado':4}
        except (json.JSONDecodeError,TypeError):ok=False
    elif case=='T18':
        try:ok=list(csv.reader(io.StringIO(raw)))==[['nome','valor'],['A','1']]
        except (csv.Error,TypeError):ok=False
    elif case=='T19':
        try:
            tree=ast.parse(raw)
            ok=(len(tree.body)==1 and isinstance(tree.body[0],(ast.FunctionDef,ast.AsyncFunctionDef))
                and len(tree.body[0].args.args)==2)
        except (SyntaxError,TypeError):ok=False
    elif case=='T20':ok=raw.casefold().strip('.!') in ('olá','ola')
    elif case=='T29':ok=raw=='4'
    else:ok=len(raw.split())==3
    return {'status':'auto-checked','passed':bool(ok)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--output',required=True)
    args=ap.parse_args();r=[]
    for line in Path(args.input).read_text(encoding='utf-8').splitlines():
        if not line.strip():continue
        x=json.loads(line)
        if x.get('status')!='ok':continue
        r.append({'job_id':x['job_id'],'case_id':x['case_id'], 'condition':x['condition'],**check(x['case_id'],x['response'])})
    Path(args.output).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in r),encoding='utf-8')
    print(json.dumps({'responses_checked':len(r),'auto_checked':sum(x['status']=='auto-checked' for x in r),
                      'auto_fail':sum(x['status']=='auto-checked' and not x['passed'] for x in r)}))
if __name__=='__main__':main()
