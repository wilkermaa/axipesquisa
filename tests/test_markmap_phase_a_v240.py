"""Regressão estrutural e de oráculos determinísticos do contrato visual A/I (AXI v2.4.0).

Não simula execução em LLMs externos nem homologa renderização nativa em UIs Web.
"""
import hashlib
import json
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skill" / "axipesquisa"
REF_DIR = SKILL_DIR / "references"

SKILL = (SKILL_DIR / "SKILL.md").read_text("utf-8")
FLOW = (REF_DIR / "FLUXO-LEITURA-INTEGRAL.md").read_text("utf-8")
ANALISE_ROUTER = (REF_DIR / "ROTEAMENTO-VISUAL-ANALISE.md").read_text("utf-8")
INTEGRACAO_ROUTER = (REF_DIR / "ROTEAMENTO-VISUAL.md").read_text("utf-8")
PLATFORMS_GUIDE = (REF_DIR / "PLATAFORMAS-VISUAIS.md").read_text("utf-8")
CHATGPT = (REF_DIR / "CHATGPT-DIAGRAMAS.md").read_text("utf-8")
GEMINI = (REF_DIR / "GEMINI-DIAGRAMAS.md").read_text("utf-8")
CLAUDE = (REF_DIR / "CLAUDE-DIAGRAMAS.md").read_text("utf-8")
GROK = (REF_DIR / "GROK-DIAGRAMAS.md").read_text("utf-8")
CONTRATO = (ROOT / "docs" / "REQUISITOS-VISUAIS-AXI-v2.4.0.md").read_text("utf-8")
PLATFORMS_DOC = (ROOT / "docs" / "PLATAFORMAS.md").read_text("utf-8")
VISUAL_POLICY = (ROOT / "docs" / "POLITICA-VISUAL.md").read_text("utf-8")


class MarkmapPhaseAContractTests(unittest.TestCase):
    def test_a01_hierarchical_requires_markmap_tree_cards_rendered(self):
        self.assertLess(SKILL.index("## A. Análise"), SKILL.index("## X. eXpansão"))
        self.assertIn("Microfase A — Visualização do Todo e das Partes", SKILL)
        self.assertIn("Markmap Tree + Cards", SKILL)
        self.assertIn("layout `tree`", SKILL)
        self.assertIn("theme `cards`", SKILL)
        self.assertIn("raiz à esquerda, partes à direita", SKILL)
        self.assertIn("realmente renderizado na tela ou em prévia gráfica aberta", SKILL)
        self.assertIn("ROTEAMENTO-VISUAL-ANALISE.md", FLOW)
        self.assertIn("layout: tree", ANALISE_ROUTER)
        self.assertIn("theme: cards", ANALISE_ROUTER)

    def test_a02_visual_fallback_when_markmap_unavailable(self):
        self.assertIn("Recuperação da A", SKILL)
        self.assertIn("mapa equivalente", SKILL)
        self.assertIn("SVG/PNG", ANALISE_ROUTER)
        self.assertIn("Identificar corretamente o desenho como equivalente", ANALISE_ROUTER)
        self.assertIn("CONFORME COM FALLBACK", ANALISE_ROUTER)

    def test_a03_textual_fallback_declares_partial_delivery(self):
        self.assertIn("ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO", SKILL)
        self.assertIn("ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO", ANALISE_ROUTER)
        self.assertIn("ENTREGA PARCIAL", CONTRATO)

    def test_a04_code_snippet_only_is_non_compliant(self):
        self.assertIn("Código Markdown/YAML ou SVG/HTML isolado", SKILL)
        self.assertIn("arquivo criado sem prévia não são entrega visual", SKILL)
        self.assertIn("Somente código/tabela/ASCII/arquivo sem prévia", ANALISE_ROUTER)
        self.assertIn("NÃO CONFORME", ANALISE_ROUTER)

    def test_a05_non_hierarchical_question_no_forced_tree(self):
        self.assertIn("Limites da A", SKILL)
        self.assertIn("não inventar árvore em pergunta trivial", SKILL)
        self.assertIn("Não inventar divisões para assuntos triviais", ANALISE_ROUTER)
        self.assertIn("Sem hierarquia útil, não inventar diagrama", FLOW)

    def test_a06_cross_cutting_or_multiple_parents_limit(self):
        self.assertIn("hierarquia enganosa ou múltiplos vínculos incompatíveis com uma árvore", SKILL)
        self.assertIn("relações de múltiplo pertencimento", ANALISE_ROUTER)
        self.assertIn("múltiplos pais/arestas cruzadas", CONTRATO)

    def test_a07_privacy_no_unauthorized_external_renderer(self):
        self.assertIn("Não enviar dados privados a serviços gráficos externos sem autorização", SKILL)
        self.assertIn("Não transferir dados privados para renderizadores externos sem autorização", ANALISE_ROUTER)
        self.assertIn("nunca enviar dados sigilosos a servidores públicos", PLATFORMS_GUIDE)

    def test_a08_fabricated_parts_non_compliant(self):
        self.assertIn("Árvore com partes/filiações inventadas", ANALISE_ROUTER)
        self.assertIn("NÃO CONFORME", ANALISE_ROUTER)
        self.assertIn("não inferir relações sem evidência", CONTRATO)

    def test_i01_i02_i03_phase_i_mermaid_regression_preserved(self):
        self.assertIn("Markmap da A não substitui Mermaid da I", SKILL)
        self.assertIn("O mapa da A **não substitui** a I", ANALISE_ROUTER)
        self.assertIn("Exclusividade desta microfase de fluxo", INTEGRACAO_ROUTER)
        self.assertIn("ROTEAMENTO-VISUAL-ANALISE.md", INTEGRACAO_ROUTER)
        self.assertIn("não substitui", VISUAL_POLICY)

    def test_x01_expansion_no_mandatory_second_chart(self):
        self.assertIn("Sem imposição de segundo gráfico", CONTRATO)
        self.assertIn("analogias úteis com limites, sem imagens compulsórias", ANALISE_ROUTER)
        self.assertIn("não se estende às fases A e X", SKILL)

    def test_f01_closed_format_json_csv_code_exemption(self):
        self.assertIn("formatos fechados prevalecem", SKILL)
        self.assertIn("saída estritamente fechada", ANALISE_ROUTER)
        self.assertIn("F01", CONTRATO)

    def test_eight_platform_guides_and_packages_include_phase_a_and_i(self):
        from scripts import build

        for doc in (CHATGPT, GEMINI, CLAUDE, GROK, PLATFORMS_GUIDE, PLATFORMS_DOC):
            self.assertIn("Microfase A", doc) if doc in (CHATGPT, GEMINI, CLAUDE, GROK) else self.assertIn("Fase A", doc)
            self.assertIn("ENTREGA PARCIAL", doc)

        for name in (
            "ChatGPT Web",
            "Gemini Web",
            "Claude Web",
            "Grok Web",
            "Codex CLI",
            "Claude Code",
            "Antigravity IDE/CLI",
            "Grok Build CLI",
        ):
            self.assertIn(name, PLATFORMS_GUIDE)
            self.assertIn(name, PLATFORMS_DOC)

        build.build()
        for platform, prefix in build.PLATFORMS.items():
            archive_path = ROOT / "dist" / f"axipesquisa-{build.VERSION}-{platform}.zip"
            with self.subTest(platform=platform), ZipFile(archive_path) as zf:
                names = set(zf.namelist())
                self.assertIn(prefix + "references/ROTEAMENTO-VISUAL-ANALISE.md", names)
                self.assertIn(prefix + "INSTALADOR-PLATAFORMA.md", names)
                guide = zf.read(prefix + "INSTALADOR-PLATAFORMA.md").decode("utf-8")
                self.assertIn("Fase A:", guide)
                self.assertIn("Fase I:", guide)
                self.assertIn("ROTEAMENTO-VISUAL-ANALISE.md", guide)
                self.assertIn("ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO", guide)
                self.assertNotIn("suporte nativo garantido", guide.casefold())

    def test_frozen_scientific_protocol_and_core_hashes_preserved(self):
        baseline = json.loads((ROOT / "tests" / "fixtures" / "preservation.json").read_text("utf-8"))
        for rel, expected_sha in baseline["core_sha256"].items():
            with self.subTest(file=rel):
                actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
                self.assertEqual(actual, expected_sha)
        cases = json.loads((ROOT / "tests" / "cases.json").read_text("utf-8"))
        self.assertEqual(len(cases), 36)
        self.assertTrue(all(case["status"] == "not-run-on-llm" for case in cases))


if __name__ == "__main__":
    unittest.main()
