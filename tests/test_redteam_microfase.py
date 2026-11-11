"""Red team da microfase: contrato e matriz de ameaças; não é homologação Gemini."""
from pathlib import Path
import re
import unittest
ROOT=Path(__file__).resolve().parents[1]
SKILL=(ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
ROUTER=(ROOT/'skill/axipesquisa/references/ROTEAMENTO-VISUAL.md').read_text('utf-8')
GEMINI=(ROOT/'skill/axipesquisa/references/GEMINI-DIAGRAMAS.md').read_text('utf-8')
RED=(ROOT/'docs/REDTEAM-MICROFASE-v2.3.3.md').read_text('utf-8')

class RedteamMicrofase(unittest.TestCase):
    def test_twenty_risks_documented(self):
        self.assertEqual([int(n) for n in re.findall(r'^\s*\|\s*(\d+)\s*\|',RED,re.M)],list(range(1,21)))
    def test_pdf_is_evidence_not_deliverable(self):
        self.assertIn('PDF não é obrigatório',SKILL)
        self.assertIn('PDF de auditoria é evidência opcional',ROUTER)
        self.assertIn('PDF não é obrigatório',GEMINI)
    def test_action_precedes_completion(self):
        self.assertIn('Ação concreta antes de concluir',SKILL)
        self.assertIn('invocar',ROUTER)
        self.assertIn('graph TD',GEMINI)
    def test_code_only_is_failure(self):
        self.assertIn('NÃO satisfazem a obrigação visual',SKILL)
        self.assertIn('Reprovado: apenas fonte',ROUTER)
    def test_preview_alone_is_sufficient(self):
        self.assertIn('prévia visual efetivamente produzida',SKILL)
        self.assertIn('não exigir PDF, PNG, SVG',ROUTER)
    def test_privacy_limits_unknown_tooling(self):
        self.assertIn('não transferir dados internos',SKILL)
        self.assertIn('não instalar',SKILL)
    def test_gemini_no_false_capability_assumption(self):
        self.assertIn('não declarar impossível',GEMINI)
        self.assertIn('capacidade',GEMINI.lower())

if __name__=='__main__': unittest.main()
