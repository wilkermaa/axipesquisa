"""Contratos de execução visual no Gemini: testes estáticos, não de frontend."""
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
GEMINI=(ROOT/'skill/axipesquisa/references/GEMINI-DIAGRAMAS.md').read_text('utf-8')
POLICY=(ROOT/'docs/POLITICA-VISUAL.md').read_text('utf-8')
ROUTE=(ROOT/'skill/axipesquisa/references/ROTEAMENTO-VISUAL.md').read_text('utf-8')

class GeminiSvgPreviewContract(unittest.TestCase):
    def test_gemini_required_in_primary_skill(self):
        self.assertIn('Gemini Web — renderização visual explícita antes da resposta final',SKILL)
        self.assertIn('produza e abra efetivamente',SKILL)
        self.assertLess(SKILL.index('## I. Integração'),SKILL.index('Gemini Web — renderização visual explícita'))
    def test_svg_priority_not_dogma(self):
        self.assertIn('SVG realmente renderizado',SKILL)
        self.assertIn('PNG ou uma visualização nativa',SKILL)
        self.assertIn('escolha tecnológica permanece da IA executora',GEMINI)
        self.assertIn('não prescrever tecnologia às outras IAs',POLICY)
    def test_rendering_before_finish(self):
        self.assertIn('Acione a geração ou abertura da prévia',SKILL)
        self.assertIn('Verifique antes de responder',GEMINI)
        self.assertIn('tente uma alternativa gráfica funcional',SKILL)
    def test_snippet_must_not_pass(self):
        self.assertIn('Snippet de código',GEMINI)
        self.assertIn('flowchart TD',SKILL)
        self.assertIn('Reprovado',GEMINI)
        self.assertIn('somente código',SKILL)
    def test_no_pdf_requirement_or_false_canvas_claim(self):
        self.assertIn('Não exige PDF',SKILL)
        self.assertIn('Não obrigar PDF nem download',GEMINI)
        self.assertIn('não presumir',SKILL.lower())
    def test_structural_not_product_validation(self):
        self.assertIn('não demonstram renderização real',GEMINI)
        self.assertIn('homologação funcional', (ROOT/'docs/RELEASE-v2.3.8.md').read_text('utf-8').lower())
    def test_economy_and_privacy(self):
        self.assertIn('minimizar tokens',GEMINI)
        self.assertIn('privacidade',GEMINI.lower())

if __name__=='__main__': unittest.main()
