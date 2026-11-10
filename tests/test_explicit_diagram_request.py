from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
REF=(ROOT/'skill/axipesquisa/references/EDICAO-E-CULTURA.md').read_text('utf-8')

class ExplicitDiagramTests(unittest.TestCase):
    def test_prompt_explicit_is_not_optional(self):
        self.assertIn('Pedido explícito prevalece', SKILL)
        self.assertIn('não considere a tarefa concluída apenas por escrever código Mermaid', SKILL)
    def test_attempt_native_then_available_fallback(self):
        self.assertIn('renderer Mermaid nativo', SKILL)
        self.assertIn('Canvas/artefatos', SKILL)
        self.assertIn('tentativa concreta', REF)
    def test_exports_are_real(self):
        self.assertIn('valide a existência dos arquivos/links', SKILL)
        self.assertIn('SVG e PNG para download', SKILL)
    def test_not_mislabel_equivalent_render(self):
        self.assertIn('representação visual equivalente', SKILL)
        self.assertIn('não uma renderização nativa de Mermaid', SKILL)
    def test_no_arbitrary_status(self):
        self.assertIn('hipotético / a validar', SKILL)
    def test_wireframes_distinct(self):
        self.assertIn('Wireframe de interface e diagrama de relações', SKILL)
    def test_missing_tools_reported_specifically(self):
        self.assertIn('qual limitação específica', SKILL)
    def test_optional_is_maintained_for_unrequested(self):
        self.assertIn('não crie imagem ou diagrama se texto bastar', SKILL)

if __name__=='__main__': unittest.main()
