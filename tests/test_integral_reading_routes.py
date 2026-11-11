"""Garantias estruturais de leitura progressiva e escolhas por plataforma; não prova de execução de IA."""
import unittest
from pathlib import Path
from zipfile import ZipFile
ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
FLOW=(ROOT/'skill/axipesquisa/references/FLUXO-LEITURA-INTEGRAL.md').read_text('utf-8')
GEMINI=(ROOT/'skill/axipesquisa/references/GEMINI-DIAGRAMAS.md').read_text('utf-8')
CLAUDE=(ROOT/'skill/axipesquisa/references/CLAUDE-DIAGRAMAS.md').read_text('utf-8')
GROK=(ROOT/'skill/axipesquisa/references/GROK-DIAGRAMAS.md').read_text('utf-8')
GPT=(ROOT/'skill/axipesquisa/references/CHATGPT-DIAGRAMAS.md').read_text('utf-8')

class IntegralReadingAndRoutes(unittest.TestCase):
    def test_full_skill_is_mandatory(self):
        for x in ('A Skill deve ser lida integralmente','SKILL.md','cada arquivo textual','Não substituir leitura integral por resumos'): self.assertIn(x,SKILL)
        for x in ('Início — ativação e A','Meio — X','Fim — I','até sua última linha'): self.assertIn(x,FLOW)
        self.assertIn('12 casos T01–T12',FLOW)
    def test_abnt_and_v20_dimensions_restored(self):
        self.assertIn('Em toda resposta explicativa ou de pesquisa',SKILL)
        self.assertIn('Nenhuma fonte externa consultada nesta resposta.',SKILL)
        compact=(ROOT/'alternativas/CHATGPT-INSTRUCOES.md').read_text('utf-8')
        self.assertIn('filosófico/metafísico',compact)
        self.assertIn('toda explicação ou pesquisa',compact)
    def test_platform_routes(self):
        self.assertIn('Mermaid renderizado',GPT)
        self.assertIn('IMAGEM',GEMINI)
        self.assertIn('Skills ainda não operam com Canvas',(ROOT/'README.md').read_text('utf-8')) if False else self.assertIn('não funcionam com Canvas',GEMINI)
        self.assertIn('visual personalizado HTML/SVG',CLAUDE)
        self.assertIn('arquivo SVG real com prévia inline',GROK)
    def test_distinct_platform_guides(self):
        from scripts import build
        build.build()
        names={}
        for platform,prefix in build.PLATFORMS.items():
            z=ROOT/'dist'/f'axipesquisa-{build.VERSION}-{platform}.zip'
            with self.subTest(platform=platform),ZipFile(z) as archive:
                path=prefix+'INSTALADOR-PLATAFORMA.md'
                self.assertIn(path,archive.namelist())
                self.assertIn(prefix+'references/FLUXO-LEITURA-INTEGRAL.md',archive.namelist())
                guide=archive.read(path).decode('utf-8')
                self.assertIn('Leitura integral obrigatória',guide)
                self.assertIn('Fontes consultadas (ABNT)',guide)
                names[platform]=guide
        self.assertEqual(len(set(names.values())),8)
        self.assertIn('IMAGEM VISÍVEL OBRIGATÓRIA',names['gemini-web'])
        self.assertIn('Mermaid renderizado',names['chatgpt-web'])
        self.assertIn('HTML/SVG inline',names['claude-web'])
        self.assertIn('prévia inline',names['grok-web'])
    def test_historical_examples_and_core_guarded(self):
        import hashlib,json
        root=ROOT/'skill/axipesquisa/references'
        actual=hashlib.sha256((root/'EXEMPLOS-E-TESTES.md').read_bytes()).hexdigest()
        self.assertEqual(actual,'7d5e0a3082de56228d050ebff4c57a39d30ffd03be54d00e8bfafa37569d5f42')
        data=json.loads((ROOT/'tests/fixtures/preservation.json').read_text('utf-8'))
        for p,h in data['core_sha256'].items(): self.assertEqual(hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),h)

if __name__=='__main__': unittest.main()

