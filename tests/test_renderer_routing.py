"""Testes estruturais do contrato de entrega visual (não reproduzem uma UI real)."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
REF = ROOT/'skill/axipesquisa/references'
ROUTER = (REF/'ROTEAMENTO-VISUAL.md').read_text('utf-8')
GEMINI = (REF/'GEMINI-DIAGRAMAS.md').read_text('utf-8')
CHATGPT = (REF/'CHATGPT-DIAGRAMAS.md').read_text('utf-8')
REST = (REF/'PLATAFORMAS-VISUAIS.md').read_text('utf-8')

class VisualRoutingContract(unittest.TestCase):
    def test_only_in_microphase(self):
        self.assertLess(SKILL.index('## I. Integração'), SKILL.index('Microfase exclusiva da Integração'))
        self.assertIn('Gestão e Coordenação',SKILL)
        self.assertIn('fases A e X',SKILL)
        for doc in (SKILL,ROUTER,GEMINI,CHATGPT,REST):
            self.assertIn('Diagramação do Fluxo de Aplicação',doc)
    def test_visual_result_even_without_request(self):
        for doc in (SKILL,ROUTER,GEMINI,CHATGPT,REST):
            self.assertIn('mesmo sem pedido explícito',doc)
        self.assertIn('NÃO satisfazem a obrigação visual',SKILL)
        self.assertIn('entrega parcial',SKILL)
        self.assertIn('graph TD',SKILL)
    def test_no_fixed_format(self):
        self.assertIn('decide autonomamente',SKILL)
        self.assertIn('tecnologia futura',SKILL)
        self.assertIn('não sequência obrigatória',ROUTER)
        self.assertIn('decide livremente',GEMINI)
    def test_concrete_render_and_pdf_optional(self):
        self.assertIn('Ação concreta antes de concluir',SKILL)
        self.assertIn('PDF não é obrigatório',SKILL)
        self.assertIn('prévia visual efetivamente produzida',SKILL)
        self.assertIn('Não inventar telas abertas',SKILL)
        self.assertIn('PDF de auditoria é evidência opcional',ROUTER)
    def test_cost_and_security(self):
        self.assertIn('minimizar tokens',SKILL)
        self.assertIn('uma alternativa viável',ROUTER)
        self.assertIn('Privacidade',SKILL)
        for name in ('Claude Web','Grok Web','Codex CLI','Claude Code','Antigravity','Grok Build'):
            self.assertIn(name,REST)
    def test_version_and_scientific_limits(self):
        self.assertEqual((ROOT/'VERSION').read_text('utf-8').strip(),'2.3.6')
        self.assertTrue((ROOT/'docs/RELEASE-v2.3.6.md').is_file())
        self.assertIn('não constitui evidência experimental',(ROOT/'docs/FUNDAMENTACAO-TECNICA.md').read_text('utf-8'))
        self.assertIn('homologação',(ROOT/'docs/RELEASE-v2.3.6.md').read_text('utf-8').casefold())

if __name__=='__main__': unittest.main()
