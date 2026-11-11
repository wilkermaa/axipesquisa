"""Regressão v2.3.10: padrão visual mínimo da imagem no Gemini. Não testa a UI real."""
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
GEMINI=(ROOT/'skill/axipesquisa/references/GEMINI-DIAGRAMAS.md').read_text('utf-8')
POLICY=(ROOT/'docs/POLITICA-VISUAL.md').read_text('utf-8')

class GeminiMinimalStyle(unittest.TestCase):
    def test_essential_rules_in_primary_skill(self):
        self.assertIn('SOMENTE TÍTULOS CURTOS', SKILL)
        self.assertIn('SEM ÍCONES', SKILL)
        self.assertIn('SEM DESCRIÇÕES internas', SKILL)
        self.assertIn('Fontes consultadas (ABNT) ficam FORA da imagem', SKILL)
    def test_visual_guide_and_prompt(self):
        for term in ('CAIXAS SÓ COM TÍTULOS CURTOS','SEM ÍCONES','SEM DESCRIÇÕES','no máximo duas linhas curtas','Sim','Não','De ofício'):
            self.assertIn(term,GEMINI)
        self.assertIn('tentar uma única', GEMINI)
        self.assertIn('Fontes consultadas (ABNT) fora da imagem',GEMINI)
    def test_policy(self):
        self.assertIn('Cada caixa somente com título curto',POLICY)
        self.assertIn('refei', 'refeito') if False else self.assertIn('regeneração simplificada',POLICY)
    def test_gemini_installer(self):
        from scripts import build
        build.build()
        with ZipFile(ROOT/'dist'/'axipesquisa-2.3.10-gemini-web.zip') as z:
            self.assertIsNone(z.testzip())
            self.assertIn('INSTALADOR-PLATAFORMA.md',z.namelist())
            self.assertEqual(z.read('SKILL.md').decode('utf-8'), SKILL)
            guide=z.read('INSTALADOR-PLATAFORMA.md').decode('utf-8')
            for term in ('SOMENTE TÍTULO CURTO','SEM ÍCONES','SEM DESCRIÇÕES'):
                self.assertIn(term,guide)
    def test_version(self):
        self.assertEqual((ROOT/'VERSION').read_text('utf-8').strip(),'2.3.10')
        self.assertTrue((ROOT/'docs/RELEASE-v2.3.10.md').is_file())

if __name__=='__main__': unittest.main()
