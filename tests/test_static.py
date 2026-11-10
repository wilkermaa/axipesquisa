import json
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import validate
import build

class AXIStaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf8')
        cls.sources=(ROOT/'skill/axipesquisa/references/PROTOCOLO-DE-FONTES.md').read_text('utf8')
        cls.critique=(ROOT/'docs/EMBASAMENTO-CIENTIFICO.md').read_text('utf8')
        cls.cases=json.loads((ROOT/'tests/cases.json').read_text('utf8'))

    def test_yaml_frontmatter(self): self.assertEqual(validate.check_skill()['name'],'axipesquisa')
    def test_axi_phases(self):
        for p in ['A. Análise','X. eXpansão','I. Integração']:self.assertIn(p,self.skill)
    def test_definition_whole_parts(self):
        for s in ['O que é?','todo','partes','função']:self.assertIn(s,self.skill)
    def test_analogical_limit(self): self.assertIn('Uma analogia **não prova causalidade',self.skill)
    def test_no_forced_analogy(self): self.assertIn('Se não houver comparação esclarecedora',self.skill)
    def test_no_false_dynamics(self): self.assertIn('Em objetos estáticos ou abstratos',self.skill)
    def test_no_universal_efficacy(self): self.assertIn('não validada empiricamente',self.skill)
    def test_pnl_limited(self): self.assertIn('não comprovada',self.skill)
    def test_no_stereotypes(self): self.assertIn('estereótipos culturais',self.skill)
    def test_abnt_before_signature(self):
        self.assertLess(self.skill.index('**`Fontes consultadas (ABNT)`**'),self.skill.index('Ao final da **resposta natural**'))
    def test_real_sources_only(self): self.assertIn('efetivamente consultadas',self.skill)
    def test_no_web_no_fake_sources(self): self.assertIn('não inventar',self.sources.casefold())
    def test_code_json_format(self): self.assertIn('*somente JSON válido*',self.skill)
    def test_privacy_config_neutral(self):
        s=(ROOT/'skill/axipesquisa/assets/config.example.json').read_text('utf8')
        self.assertIsNone(json.loads(s)['email_do_usuario'])
        self.assertIsNone(json.loads(s)['nome_do_usuario'])
    def test_no_email_public_skill(self):
        for p in (ROOT/'skill/axipesquisa').rglob('*'):
            if p.is_file():self.assertFalse(validate.EMAIL_PATTERN.findall(p.read_text('utf8')))
    def test_injection_guard(self): self.assertIn('dados não confiáveis',self.skill)
    def test_dual_license_documented(self):
        self.assertIn('MIT License',(ROOT/'LICENSE').read_text('utf8'))
        self.assertIn('CC BY 4.0',(ROOT/'LICENSE-CONTENT.md').read_text('utf8'))
        self.assertIn('CC BY 4.0',(ROOT/'skill/axipesquisa/LICENSE-CONTENT.md').read_text('utf8'))
        self.assertIn('Wilker M. de Araujo Alexandre',(ROOT/'ATTRIBUTION.md').read_text('utf8'))
    def test_evaluation_vs_validation(self): self.assertIn('Não há',self.critique)
    def test_cases_many(self): self.assertGreaterEqual(len(self.cases),24)
    def test_all_case_ids_unique(self): self.assertEqual(len({x['id'] for x in self.cases}),len(self.cases))
    def test_cases_have_expectations(self):
        self.assertTrue(all(len(x['expected'])>18 for x in self.cases))
    def test_all_eight_packages_have_only_expected_files(self):
        build.build()
        for p in (ROOT/'dist').glob('axipesquisa-*.zip'):validate.check_zip(p)
        self.assertEqual(len(list((ROOT/'dist').glob('axipesquisa-*.zip'))),8)

if __name__=='__main__':unittest.main()
