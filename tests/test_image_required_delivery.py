"""AXI v2.3.9: imagem visual exibida é portão da microfase I. Teste de fonte, não de execução de frontend."""
import unittest
from pathlib import Path
from zipfile import ZipFile
ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
REF=ROOT/'skill/axipesquisa/references'
GEMINI=(REF/'GEMINI-DIAGRAMAS.md').read_text('utf-8')
ROUTE=(REF/'ROTEAMENTO-VISUAL.md').read_text('utf-8')
POLICY=(ROOT/'docs/POLITICA-VISUAL.md').read_text('utf-8')

class RequiredImageDelivery(unittest.TestCase):
    def test_image_is_required_in_main_skill(self):
        self.assertIn('IMAGEM OBRIGATÓRIA',SKILL)
        self.assertIn('ENTREGAR O DIAGRAMA COMO IMAGEM',SKILL)
        self.assertIn('imagem efetivamente desenhada e visível na tela',SKILL)
        self.assertLess(SKILL.index('Microfase exclusiva da Integração'),SKILL.index('Fundamento de entrega')) if False else self.assertLess(SKILL.index('Microfase exclusiva da Integração'),SKILL.index('Fundamento de entrega — IMAGEM OBRIGATÓRIA'))
    def test_no_ascii_table_code_or_unpreviewed_file(self):
        for x in ('Tabela, lista numerada','ASCII','flowchart TD','arquivo gráfico apenas criado sem prévia','HTML/app interativo'):
            self.assertIn(x,SKILL)
        self.assertIn('Arquivo gráfico apenas criado, sem prévia/exibição',ROUTE)
        self.assertIn('Arquivo gráfico real e acessível, mas não mostrado em prévia',ROUTE)
        self.assertIn('imagem do fluxograma realmente exibida',POLICY.lower())
    def test_gemini_is_image_first_not_app_first(self):
        self.assertIn('Solicitar/acionar geração DIRETA DE IMAGEM',GEMINI)
        self.assertIn('SVG realmente renderizado',GEMINI)
        self.assertIn('PNG',GEMINI)
        self.assertIn('aplicativo interativo apenas se o usuário pedir expressamente',GEMINI)
        self.assertIn('Canvas',GEMINI)
        self.assertIn('não funciona com Skills',GEMINI)
    def test_failure_is_partial_not_success(self):
        self.assertIn('entrega parcial',SKILL)
        self.assertIn('Sem imagem, registrar',GEMINI)
        self.assertIn('imagem do diagrama',ROUTE.lower())
        self.assertIn('não demonstram renderização real',(ROOT/'docs/RELEASE-v2.3.9.md').read_text('utf-8'))
    def test_all_eight_installers_convey_rule(self):
        from scripts import build
        build.build()
        for platform,prefix in build.PLATFORMS.items():
            with self.subTest(platform=platform), ZipFile(ROOT/'dist'/f'axipesquisa-{build.VERSION}-{platform}.zip') as z:
                self.assertIsNone(z.testzip())
                self.assertIn('ENTREGAR O DIAGRAMA COMO IMAGEM',z.read(prefix+'SKILL.md').decode('utf-8'))
                self.assertIn('IMAGEM renderizada na tela ou em prévia',z.read(prefix+'INSTALADOR-PLATAFORMA.md').decode('utf-8'))

if __name__=='__main__': unittest.main()
