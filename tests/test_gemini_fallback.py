from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
VERSION=(ROOT/'VERSION').read_text('utf-8').strip()
REF=(ROOT/'skill/axipesquisa/references/GEMINI-DIAGRAMAS.md').read_text('utf-8')
DOC=(ROOT/'docs/GEMINI-DIAGRAMAS-E-EXPORTACAO.md').read_text('utf-8')

class GeminiFallbackPolicy(unittest.TestCase):
    def test_html_template_export_buttons(self):
        demo=(ROOT/'examples/GEMINI-CANVAS-DIAGRAMA.html').read_text('utf-8')
        self.assertIn('svgDownload',demo)
        self.assertIn('pngDownload',demo)
        self.assertIn('canvas.toBlob',demo)
        self.assertIn('XMLSerializer',demo)
        self.assertNotIn('<script src=',demo)
    def test_template_packaged(self):
        self.assertIn('assets/GEMINI-CANVAS-TEMPLATE.md',SKILL)
        self.assertTrue((ROOT/'skill/axipesquisa/assets/GEMINI-CANVAS-TEMPLATE.md').is_file())
    def test_current_version(self): self.assertIn(f'version: "{VERSION}"',SKILL)
    def test_gemini_explicit_branch(self): self.assertIn('Prioridade de saída para Gemini Web', SKILL)
    def test_svg_without_mermaid_renderer(self): self.assertIn('SVG vetorial autossuficiente', SKILL)
    def test_html_canvas_inline(self): self.assertIn('`<svg>` incorporado',SKILL)
    def test_png_local_canvas_export(self): self.assertIn('Canvas 2D',SKILL)
    def test_no_lies_about_execution(self): self.assertIn('não encerra',SKILL)
    def test_renderer_is_not_mandatory_if_text_better(self): self.assertIn('não crie imagem ou diagrama se texto bastar',SKILL)
    def test_privacy(self): self.assertIn('Não use `fetch` externo',REF)
    def test_source_guide(self): self.assertIn('support.google.com/gemini',DOC)
    def test_model_status_unverified(self): self.assertIn('sem evidência específica',REF)
    def test_canvas_user_action(self): self.assertIn('Adicionar arquivos (+) → Canvas',SKILL)
    def test_app_not_assumed(self): self.assertIn('não execução comprovada',REF)

if __name__=='__main__':unittest.main()
