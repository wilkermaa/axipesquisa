"""Regressão jurídica+ABNT sem afirmar que o Gemini fez pesquisa real."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
SOURCES=(ROOT/'skill/axipesquisa/references/PROTOCOLO-JURIDICO-ABNT.md').read_text('utf-8')
GEMINI=(ROOT/'skill/axipesquisa/references/GEMINI-DIAGRAMAS.md').read_text('utf-8')
VISUAL=(ROOT/'docs/POLITICA-VISUAL.md').read_text('utf-8')

class LegalResearchRegression(unittest.TestCase):
    def test_legal_research_precedes_claim_and_diagram(self):
        self.assertLess(SKILL.index('Portão obrigatório de pesquisa'), SKILL.index('## A. Análise'))
        self.assertIn('pesquisar o ordenamento',SKILL)
        self.assertIn('fonte oficial',SKILL)
        self.assertIn('Não produzir fluxograma juridicamente assertivo',SKILL)
    def test_citations_and_abnt_are_required(self):
        self.assertIn('Referências ABNT não são opcionais',SKILL)
        self.assertIn('Fontes consultadas (ABNT)',SKILL)
        self.assertIn('data efetiva de consulta',SKILL)
        self.assertIn('bibliografia ABNT',GEMINI)
    def test_no_fabricated_legal_procedure(self):
        for term in ('Procuradoria','prazos','não afirmar como obrigatório','prática administrativa a confirmar'):
            self.assertIn(term,SKILL)
        self.assertIn('não elevar prática plausível',SOURCES)
    def test_matinhos_article_57_difference(self):
        for term in ('1.165/2008','art. 57','inciso I','inciso II','Portaria','Ofício','§ 1º','§ 2º','§ 3º'):
            self.assertIn(term,SOURCES)
        self.assertIn('não generalizar portaria',SOURCES.lower()) if False else self.assertIn('não converter automaticamente',SOURCES.lower())
    def test_research_abnt_diagram_are_independent(self):
        self.assertIn('três deveres independentes',SKILL)
        self.assertIn('pesquisa jurídica, citações ABNT e entrega visual',SKILL)
        self.assertIn('não dispensa consulta à legislação',VISUAL)
        self.assertIn('diagrama',GEMINI.lower())
    def test_no_fake_sources_and_secondary_limit(self):
        self.assertIn('não simular pesquisa nem bibliografia',SKILL)
        self.assertIn('fonte secundária',SOURCES)
        self.assertIn('confirmação oficial',SOURCES)
    def test_version_and_release(self):
        self.assertEqual((ROOT/'VERSION').read_text('utf-8').strip(),'2.3.10')
        self.assertIn('homologação real',(ROOT/'docs/RELEASE-v2.3.10.md').read_text('utf-8').lower())

if __name__=='__main__': unittest.main()

