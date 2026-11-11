"""Detect loss of historical AXI teaching material and release integrity."""
import hashlib
import json
import re
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT/'skill/axipesquisa'
EXAMPLES = SKILL/'references/EXEMPLOS-E-TESTES.md'
EDITORIAL = SKILL/'references/EDICAO-E-CULTURA.md'
BASELINE = json.loads((ROOT/'tests/fixtures/preservation.json').read_text('utf-8'))

class ContentPreservationTests(unittest.TestCase):
    def test_historic_examples_byte_identical_to_v20(self):
        self.assertEqual(hashlib.sha256(EXAMPLES.read_bytes()).hexdigest(),
                         '7d5e0a3082de56228d050ebff4c57a39d30ffd03be54d00e8bfafa37569d5f42')
    def test_twelve_examples_present(self):
        text=EXAMPLES.read_text('utf-8')
        self.assertEqual(re.findall(r'^## Teste (T\d{2})',text,re.M),[f'T{i:02}' for i in range(1,13)])
    def test_example_acceptance_and_human_scoring_preserved(self):
        text=EXAMPLES.read_text('utf-8')
        for expected in ('**Prompt:**','**Esperado:**','0 = não atende, 1 = parcial, 2 = atende', 'Total máximo 24', 'não métrica cientificamente validada'):
            self.assertIn(expected,text)
    def test_eight_editorial_questions_preserved(self):
        text=EDITORIAL.read_text('utf-8')
        expected=['Comunicar','Avaliar','Persuadir','Liderar','Decidir','Confiar','Discordar','Agendar']
        section=text.split('## As oito perguntas editoriais (recuperadas da v2.0)')[1].split('## Sweller e Mayer',1)[0]
        self.assertEqual(re.findall(r'^\d+\. \*\*(\w+):\*\*',section,re.M),expected)
        self.assertIn('não',section.casefold())
        self.assertIn('país',section)
    def test_examples_required_for_integral_reading(self):
        body=(SKILL/'SKILL.md').read_text('utf-8')
        self.assertIn('EXEMPLOS-E-TESTES.md',body)
        self.assertIn('**leitura integral obrigatória**',body)
        self.assertIn('12 casos T01–T12',(SKILL/'references/FLUXO-LEITURA-INTEGRAL.md').read_text('utf-8'))
    def test_eight_platforms_contain_same_skill_and_historic_material(self):
        from scripts import build
        build.build()
        for platform,prefix in build.PLATFORMS.items():
            p=ROOT/'dist'/f'axipesquisa-2.3.6-{platform}.zip'
            with self.subTest(platform=platform), ZipFile(p) as z:
                self.assertIsNone(z.testzip())
                for name in ['SKILL.md','README-INSTALACAO.md','references/EXEMPLOS-E-TESTES.md','references/EDICAO-E-CULTURA.md']:
                    self.assertIn(prefix+name,z.namelist())
                self.assertEqual(z.read(prefix+'SKILL.md'),(SKILL/'SKILL.md').read_bytes())
                self.assertEqual(z.read(prefix+'references/EXEMPLOS-E-TESTES.md'),EXAMPLES.read_bytes())
    def test_critical_core_files_unchanged_from_v222(self):
        for rel, digest in BASELINE['core_sha256'].items():
            with self.subTest(file=rel):
                self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),digest)
    def test_release_policy_is_explicit(self):
        t=(ROOT/'docs/POLITICA-ORGANIZACIONAL-VERSOES.md').read_text('utf-8')
        for k in ['Toda modificação','nova tag Git anotada','Não modificar nem substituir tags', 'v2.2.0-rc2']:
            self.assertIn(k,t)
    def test_source_release_consistency(self):
        from scripts.check_release import check_source
        self.assertEqual(check_source(),'2.3.6')
    def test_no_premature_scientific_validation(self):
        t=(ROOT/'README.md').read_text('utf-8')
        self.assertIn('sem execuções comprovadas',t)
        self.assertIn('não significa validação científica',t)

if __name__=='__main__':unittest.main()
