"""Teste estático da política de seleção; não simula renderizadores das IAs."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / 'skill/axipesquisa/SKILL.md').read_text('utf-8')
BASE = ROOT / 'skill/axipesquisa/references'
ROUTER = (BASE / 'ROTEAMENTO-VISUAL.md').read_text('utf-8')
GEMINI = (BASE / 'GEMINI-DIAGRAMAS.md').read_text('utf-8')
CHATGPT = (BASE / 'CHATGPT-DIAGRAMAS.md').read_text('utf-8')
REST = (BASE / 'PLATAFORMAS-VISUAIS.md').read_text('utf-8')

class VisualRoutingContract(unittest.TestCase):
    def test_phase_i_routes_by_actual_capability(self):
        self.assertIn('## I. Integração', SKILL)
        self.assertIn('Pré-verificação econômica da fase I', SKILL)
        self.assertIn('renderizadores **realmente habilitados nesta sessão**', SKILL)
        self.assertIn('ROTEAMENTO-VISUAL.md', SKILL)

    def test_no_visual_for_trivial_text(self):
        self.assertIn('não crie imagem ou diagrama se texto bastar', SKILL)
        self.assertIn('Sem necessidade visual', ROUTER)

    def test_type_aware_rendering(self):
        for item in ('Relações/fluxo', 'Dados numéricos', 'Exploração interativa', 'Vega-Lite'):
            self.assertIn(item, ROUTER + CHATGPT)

    def test_cost_proxy_and_bounded_fallback(self):
        for item in ('sem chamadas externas', 'menor custo incremental', 'uma tentativa', 'alternativa'):
            self.assertIn(item.casefold(), (ROUTER + SKILL).casefold())
        self.assertIn('não alegar maior eficiência', ROUTER)

    def test_gemini_routes_without_mermaid_assumption(self):
        for item in ('Gráfico quantitativo', 'Deep Research', 'SVG vetorial autossuficiente', 'Canvas 2D'):
            self.assertIn(item, GEMINI)
        self.assertIn('não encerra', SKILL)

    def test_chatgpt_native_preview_and_numbers(self):
        self.assertIn('Mermaid', CHATGPT)
        self.assertIn('Vega/Vega-Lite', CHATGPT)
        self.assertIn('Prévia ausente', CHATGPT)

    def test_six_platforms_all_covered(self):
        for name in ('Claude Web', 'Grok Web', 'Codex CLI', 'Claude Code', 'Antigravity', 'Grok Build'):
            with self.subTest(platform=name): self.assertIn(name, REST)

    def test_privacy_and_real_exports(self):
        for item in ('Privacidade', 'SVG', 'PNG', 'verificáveis'):
            self.assertIn(item, ROUTER + REST)
        self.assertIn('não inventar', ROUTER)

    def test_version_and_release_policy(self):
        self.assertEqual((ROOT / 'VERSION').read_text('utf-8').strip(), '2.3.0')
        self.assertIn('v2.3.0', (ROOT / 'CHANGELOG.md').read_text('utf-8'))
        self.assertTrue((ROOT / 'docs/RELEASE-v2.3.0.md').is_file())

if __name__ == '__main__': unittest.main()
