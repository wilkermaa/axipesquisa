import csv,json,tempfile,unittest
from pathlib import Path
import importlib.util
P=Path(__file__).resolve().parents[1]/'scripts/eval_review.py'
spec=importlib.util.spec_from_file_location('eval_review_for_test',P)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

class AggregateTests(unittest.TestCase):
    def test_paired_comparison_with_two_independent_reviewers(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d);key=folder/'key.json';ratings=folder/'ratings.csv';out=folder/'out.json'
            maps=[{'blind_id':'B01','job_id':'a','case_id':'T01','condition':'baseline','provider':'openai','model':'test','repeat':1},
                  {'blind_id':'B02','job_id':'b','case_id':'T01','condition':'generic','provider':'openai','model':'test','repeat':1},
                  {'blind_id':'B03','job_id':'c','case_id':'T01','condition':'axi','provider':'openai','model':'test','repeat':1}]
            key.write_text(json.dumps(maps))
            with ratings.open('w',newline='',encoding='utf8') as f:
                writer=csv.DictWriter(f,fieldnames=['blind_id','reviewer','factual','critical_failure']);writer.writeheader()
                for item,score in zip(maps,[1,2,3]):
                    for reviewer in ['R1','R2']:writer.writerow({'blind_id':item['blind_id'],'reviewer':reviewer,'factual':score,'critical_failure':0})
            mod.aggregate(type('A',(),{'key':str(key),'ratings':str(ratings),'output':str(out),'min_reviewers':2})())
            result=json.loads(out.read_text())
            self.assertEqual(result['comparisons']['axi_vs_baseline']['mean_difference'],2)
            self.assertEqual(result['comparisons']['axi_vs_generic']['mean_difference'],1)
            self.assertEqual(result['response_count_with_required_reviews'],3)
    def test_no_fabricated_ratings(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d);key=folder/'key.json';ratings=folder/'ratings.csv';out=folder/'out.json'
            key.write_text(json.dumps([{'blind_id':'B1','job_id':'a','case_id':'T01','condition':'axi',
                                        'provider':'openai','model':'test','repeat':1}]))
            ratings.write_text('blind_id,reviewer,factual\nB1,R1,4\n')
            mod.aggregate(type('A',(),{'key':str(key),'ratings':str(ratings),'output':str(out),'min_reviewers':2})())
            self.assertEqual(json.loads(out.read_text())['response_count_with_required_reviews'],0)
if __name__=='__main__':unittest.main()
