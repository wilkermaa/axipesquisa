"""Regressão v2.3.7: Canvas deixou de ser rota obrigatória quando imagem direta virou prioridade."""
import unittest
from pathlib import Path
from zipfile import ZipFile
ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
GEMINI=(ROOT/'skill/axipesquisa/references/GEMINI-DIAGRAMAS.md').read_text('utf-8')
HISTORY=(ROOT/'docs/RELEASE-v2.3.7.md').read_text('utf-8')

class CanvasFallbackNotDefault(unittest.TestCase):
    def test_old_design_remains_versioned(self):
        self.assertIn('Canvas como ferramenta de saída',HISTORY)
    def test_image_first_supersedes_canvas(self):
        self.assertIn('geração DIRETA DE IMAGEM',GEMINI)
        self.assertIn('Canvas com SVG e prévia',GEMINI)
        self.assertIn('pode ser fallback estático',GEMINI)
        self.assertIn('não funciona com Skills',GEMINI)
        self.assertIn('IMAGEM do diagrama',SKILL)
    def test_packaged_gemini_route_is_image_first(self):
        from scripts import build
        build.build()
        p=ROOT/'dist'/f'axipesquisa-{build.VERSION}-gemini-web.zip'
        with ZipFile(p) as z:
            self.assertIsNone(z.testzip())
            self.assertEqual(z.read('SKILL.md').decode('utf-8'),SKILL)
            route=z.read('INSTALADOR-PLATAFORMA.md').decode('utf-8')
            self.assertIn('IMAGEM VISÍVEL OBRIGATÓRIA',route)
            self.assertIn('DIRETA DE IMAGEM',route)
            self.assertIn('não substituir por tabela',route.lower())

if __name__=='__main__': unittest.main()
