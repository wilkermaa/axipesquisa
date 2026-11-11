"""Testes estruturais da microfase visual; não simulam renderização nas IAs."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
BASE = ROOT/'skill/axipesquisa/references'
ROUTER = (BASE/'ROTEAMENTO-VISUAL.md').read_text('utf-8')
GEMINI = (BASE/'GEMINI-DIAGRAMAS.md').read_text('utf-8')
CHATGPT = (BASE/'CHATGPT-DIAGRAMAS.md').read_text('utf-8')
REST = (BASE/'PLATAFORMAS-VISUAIS.md').read_text('utf-8')

class VisualRoutingContract(unittest.TestCase):
    def test_microphase_scoped_under_integration(self):
        self.assertLess(SKILL.index('## I. Integração'),SKILL.index('Microfase exclusiva da Integração'))
        self.assertIn('somente esta microfase',SKILL)
        for doc in (SKILL,ROUTER,GEMINI,CHATGPT,REST):
            self.assertIn('Diagramação do Fluxo de Aplicação',doc)
        self.assertIn('Gestão e Coordenação',SKILL)
    def test_visual_result_and_unrequested_flow(self):
        for doc in (SKILL,ROUTER,GEMINI,CHATGPT,REST):
            self.assertIn('mesmo sem pedido explícito',doc)
        self.assertIn('NÃO satisfazem a obrigação visual',SKILL)
        self.assertIn('somente código',SKILL)
        self.assertIn('entrega parcial',SKILL)
    def test_no_fixed_renderer(self):
        self.assertIn('decide autonomamente',SKILL)
        self.assertIn('mecanismo futuro ainda desconhecido',SKILL)
        self.assertIn('Não obrigar Mermaid, SVG, HTML, Canvas, PNG',ROUTER)
        self.assertIn('não uma ordem fixa',GEMINI)
    def test_safety_and_economy(self):
        self.assertIn('tokens de saída/código',SKILL)
        self.assertIn('uma tentativa principal',ROUTER)
        self.assertIn('Privacidade',SKILL)
        for name in ('Claude Web','Grok Web','Codex CLI','Claude Code','Antigravity','Grok Build'):
            self.assertIn(name,REST)
    def test_version_and_technical_basis(self):
        self.assertEqual((ROOT/'VERSION').read_text('utf-8').strip(),'2.3.2')
        self.assertTrue((ROOT/'docs/RELEASE-v2.3.2.md').is_file())
        b=(ROOT/'docs/FUNDAMENTACAO-TECNICA.md').read_text('utf-8')
        self.assertIn('Semantic Versioning 2.0.0',b)
        self.assertIn('não constitui evidência experimental',b)

if __name__=='__main__': unittest.main()

