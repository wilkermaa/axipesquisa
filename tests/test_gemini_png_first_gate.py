"""Regressão v2.3.10: Gemini deve tentar PNG visível; snippet Mermaid nunca é entrega. Teste estrutural."""
from pathlib import Path
from zipfile import ZipFile
import unittest

ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
GEMINI=(ROOT/'skill/axipesquisa/references/GEMINI-DIAGRAMAS.md').read_text('utf-8')
POLICY=(ROOT/'docs/POLITICA-VISUAL.md').read_text('utf-8')

class PNGFirstGate(unittest.TestCase):
    def test_executable_gate_in_primary_skill_near_top(self):
        self.assertIn('Portão crítico Gemini — EXECUTAR PNG antes de finalizar',SKILL)
        self.assertLess(SKILL.index('Portão crítico Gemini'),SKILL.index('## A. Análise'))
        self.assertIn('ACIONAR a ferramenta de geração de IMAGEM',SKILL)
        self.assertIn('NUNCA os mostrar como entrega gráfica',SKILL)
    def test_prioritize_png_before_mermaid_aesthetics(self):
        self.assertIn('EXECUTAR PNG AGORA',GEMINI)
        self.assertIn('MOSTRAR E VERIFICAR PNG',GEMINI)
        self.assertIn('ESTÉTICA APÓS O PNG',GEMINI)
        self.assertLess(GEMINI.index('EXECUTAR PNG AGORA'),GEMINI.index('ESTÉTICA APÓS O PNG'))
        self.assertIn('CAIXAS SÓ COM TÍTULOS CURTOS',GEMINI)
        self.assertIn('SEM ÍCONES',GEMINI)
    def test_guaratuba_snippet_banned_even_partial(self):
        self.assertIn('Registro de Entrega Visual Parcial',GEMINI)
        self.assertIn('NUNCA pode ser exibido como substituto do PNG',GEMINI)
        self.assertIn('não enviar bloco',GEMINI)
        self.assertIn('flowchart TD',GEMINI)
        self.assertIn('sem código',POLICY.lower())
    def test_no_fake_tool_availability_or_fake_success(self):
        self.assertIn('tentativa efetiva',SKILL)
        self.assertIn('não declarar impossível',GEMINI)
        self.assertIn('não demonstra',GEMINI)
        self.assertIn('não constitui prova de execução no Gemini',(ROOT/'docs/RELEASE-v2.3.10.md').read_text('utf-8'))
    def test_eight_packaging_and_gemini_specific_route(self):
        from scripts import build
        build.build()
        self.assertEqual(len(build.PLATFORMS),8)
        z=ROOT/'dist'/f'axipesquisa-{build.VERSION}-gemini-web.zip'
        with ZipFile(z) as arch:
            self.assertIsNone(arch.testzip())
            self.assertEqual(arch.read('SKILL.md').decode('utf-8'),SKILL)
            guide=arch.read('INSTALADOR-PLATAFORMA.md').decode('utf-8')
            self.assertIn('ACIONAR EFETIVAMENTE',guide)
            self.assertIn('NUNCA emitir snippet',guide)
    def test_version_and_historical_controls(self):
        self.assertEqual((ROOT/'VERSION').read_text('utf-8').strip(),'2.3.10')
        self.assertTrue((ROOT/'docs/RELEASE-v2.3.9.md').exists())
        self.assertTrue((ROOT/'docs/RELEASE-v2.3.10.md').exists())

if __name__=='__main__': unittest.main()
