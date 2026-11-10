from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT/'skill/axipesquisa/SKILL.md').read_text('utf-8')
VERSION = (ROOT/'VERSION').read_text('utf-8').strip()
REF = (ROOT/'skill/axipesquisa/references/EDICAO-E-CULTURA.md').read_text('utf-8')

class VisualPolicyTests(unittest.TestCase):
    def test_current_patch_version(self):
        self.assertIn(f'version: "{VERSION}"', SKILL)
    def test_mermaid_integration(self):
        self.assertLess(SKILL.index('## I. Integração'), SKILL.index('Mermaid renderizado'))
        self.assertIn('fluxos, decisões, arquiteturas, sequências', SKILL)
    def test_conditional_rendering(self):
        self.assertIn('não crie imagem ou diagrama se texto bastar', SKILL)
        self.assertIn('recursos existentes de Canvas', SKILL)
    def test_exports_not_promised(self):
        for item in ('SVG', 'PNG', 'sem afirmar que criou arquivos inexistentes'):
            self.assertIn(item, SKILL)
    def test_accessible_status(self):
        for item in ('verde = concluído', 'amarelo = atenção', 'vermelho = bloqueado', 'sempre com rótulo textual'):
            self.assertIn(item, SKILL)
    def test_privacy_and_fallback(self):
        self.assertIn('serviços externos de renderização', SKILL)
        self.assertIn('código Mermaid válido', REF)
    def test_visual_policy_reference(self):
        self.assertIn('docs/POLITICA-VISUAL.md', (ROOT/'README.md').read_text('utf-8'))

if __name__ == '__main__':
    unittest.main()

class DistributionVisualPolicyTests(unittest.TestCase):
    def test_eight_packages_match_canonical_visual_policy(self):
        from zipfile import ZipFile
        from scripts import build
        for platform, prefix in build.PLATFORMS.items():
            p = ROOT/'dist'/f'axipesquisa-{VERSION}-{platform}.zip'
            if not p.exists():
                continue  # the builder has its own test; this test inspects packages when present
            with ZipFile(p) as zipf:
                text = zipf.read(prefix+'SKILL.md').decode('utf-8')
                self.assertEqual(SKILL, text)
                self.assertIn('SVG e PNG', text)
