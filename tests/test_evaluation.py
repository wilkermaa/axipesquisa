import importlib.util,json,tempfile,unittest
from pathlib import Path
from unittest import mock
ROOT=Path(__file__).resolve().parents[1]

def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
run=load('run_eval');oracles=load('check_outputs');review=load('eval_review')

class EvaluationTests(unittest.TestCase):
    def test_cases_unique_and_36(self):
        cases=json.loads((ROOT/'tests/cases.json').read_text())
        self.assertEqual(len(cases),36)
        self.assertEqual(len(set(c['id'] for c in cases)),36)
        self.assertTrue(all(c['status']=='not-run-on-llm' for c in cases))
    def test_preparation_three_conditions_and_repeat(self):
        with tempfile.TemporaryDirectory() as d:
            path=str(Path(d)/'manifest.jsonl')
            args=type('A',(),dict(seed=20261104,provider='openai',model='fictional-model-for-static-test',repeats=2,output=path))()
            run.prepare(args)
            rows=review.load(path)
            self.assertEqual(len(rows),216)
            self.assertEqual({x['condition'] for x in rows},set(run.CONDITIONS))
            self.assertEqual(len({x['job_id'] for x in rows}),216)
            self.assertEqual(len({x['system_sha256'] for x in rows}),3)
            self.assertTrue(all(x['test_mode']=='prompt-equivalent-no-tools' for x in rows))
    def test_cannot_run_without_confirmation(self):
        with self.assertRaises(SystemExit) as c:
            run.run(type('A',(),{'confirm_billable':False})())
        self.assertIn('confirm-billable',str(c.exception))
    def test_deterministic_oracles(self):
        positives={'T17':'{"resultado":4}','T18':'nome,valor\nA,1','T19':'def soma(a,b):\n    return a+b',
                   'T20':'olá','T29':'4','T34':'Primeiro entra sai'}
        for c,a in positives.items():
            with self.subTest(case=c): self.assertTrue(oracles.check(c,a)['passed'])
        for c,a in {'T17':'Exemplo: {"resultado":4}','T18':'nome,valor\nA,1\n◌ AXI','T19':'texto\ndef soma(a,b): return a+b',
                    'T20':'Olá\n◌ AXI','T29':'4.','T34':'FIFO é uma fila'}.items():
            with self.subTest(case=c):self.assertFalse(oracles.check(c,a)['passed'])
    def test_unscorable_cases_do_not_become_successes(self):
        for case in ['T01','T04','T13','T21','T30','T36']:
            self.assertIsNone(oracles.check(case,'foo')['passed'])
    def test_blind_pack_avoids_condition_on_review_sheet(self):
        with tempfile.TemporaryDirectory() as d:
            infile=Path(d)/'responses.jsonl';dest=Path(d)/'blind'
            rows=[{'status':'ok','case_id':'T29','category':'short','prompt':'2+2?',
                  'response':'4','job_id':'abc','condition':'axi','provider':'openai','model':'demo','repeat':1}]
            infile.write_text(''.join(json.dumps(x)+'\n' for x in rows))
            review.pack(type('A',(),{'input':str(infile),'output':str(dest),'seed':2})())
            self.assertNotIn('condition',(dest/'blind_responses.csv').read_text())
            self.assertIn('condition',(dest/'PRIVATE_BLIND_KEY.json').read_text())
    def test_external_requests_not_required_for_unit_tests(self):
        self.assertFalse(any((ROOT/'evals').glob('real-responses-*')))
if __name__=='__main__':unittest.main()
