"""Contrato documental: coordenação AXI, ferramenta Canvas e prévia, sem comprovação de suporte Gemini."""
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
GEMINI=(ROOT/'skill/axipesquisa/references/GEMINI-DIAGRAMAS.md').read_text('utf-8')
ROUTER=(ROOT/'skill/axipesquisa/references/ROTEAMENTO-VISUAL.md').read_text('utf-8')
RELEASE=(ROOT/'docs/RELEASE-v2.3.7.md').read_text('utf-8')

class CanvasDispatchContract(unittest.TestCase):
    def test_canvas_as_output_not_skill_execution_inside_canvas(self):
        self.assertIn('a Skill coordena o pedido na conversa',SKILL)
        self.assertIn('solicitar/acionar expressamente o Canvas como ferramenta de saída',SKILL)
        self.assertIn('Não é necessário executar a Skill dentro do Canvas',SKILL)
        self.assertIn('Não colocar a Skill para funcionar dentro do Canvas',GEMINI)
        self.assertIn('a Skill não executa dentro do Canvas',ROUTER)
    def test_preview_not_interaction_or_code(self):
        self.assertIn('Não é necessária interação após a geração',GEMINI)
        self.assertIn('abrir a Prévia',GEMINI)
        self.assertIn('verifique que está visível',SKILL)
        self.assertIn('Snippet de código',GEMINI)
        self.assertIn('não é necessário exportar pdf',RELEASE.lower())
    def test_gemini_compatibility_is_uncertain_not_promised(self):
        self.assertIn('não comprova que o modelo possa encaminhar automaticamente',GEMINI)
        self.assertIn('hipótese operacional a testar',GEMINI)
        self.assertIn('não presumir',SKILL.lower())
        self.assertIn('não executam o gemini real',RELEASE.lower())
    def test_other_platforms_and_abnt_unchanged(self):
        for text in ('ChatGPT → Mermaid renderizado','Claude Web → visual personalizado','Grok Web → arquivo SVG','Fontes consultadas (ABNT)'): self.assertIn(text,SKILL)
        self.assertIn('leitura integral',SKILL)
    def test_gemini_installer_has_separation_and_preserved_skill(self):
        from scripts import build
        build.build()
        file=ROOT/'dist'/f'axipesquisa-{build.VERSION}-gemini-web.zip'
        with ZipFile(file) as z:
            self.assertIsNone(z.testzip())
            self.assertEqual(z.read('SKILL.md').decode('utf-8'),SKILL)
            g=z.read('INSTALADOR-PLATAFORMA.md').decode('utf-8')
            self.assertIn('Canvas com SVG',g)
            self.assertIn('não executar a Skill dentro do Canvas',g)
            self.assertIn('Prévia',g)

if __name__=='__main__': unittest.main()
