# Relatório de Testes — AXI Pesquisa v2.4.0 (Issue #19)

**Disciplina:** `TESTES` ([Issue #19](https://github.com/wilkermaa/axipesquisa/issues/19)) · **PR:** [#23](https://github.com/wilkermaa/axipesquisa/pull/23)  
**SHA candidato avaliado (código de produção):** `f2c3e81c18030770c1790b01f48489bbf5fa8d8a` (`feat/axi-v2.4.0-markmap-fase-a`)  
**Executor:** Antigravity — Orchestrator (Argon) sob delegação expressa da Direção Humana (`19/11/2026`).  
**Regra disciplinar cumprida:** **nenhum arquivo de produção (`skill/**`, `scripts/**`) ou `tests/cases.json` foi alterado nesta issue.**

---

## 1. Ambiente e comandos executados

- **Sistema operacional:** Windows · **Python:** `3.12.10` (`PyYAML==6.0.3`)
- **Comandos executados localmente no workspace `c:\Users\forja\Documents\Skill-AXIPesquisa`:**
  1. `python scripts/verificar_versao.py` → `AXI: versão consistente: 2.4.0` (`PASS`)
  2. `python scripts/validate.py` → `status: "passed-static-only"`, `files: 21`, `cases_defined: 36` (`PASS`)
  3. `python -m unittest discover -s tests -v` → **`Ran 124 tests in 2.129s — OK`** (`124 PASS`, `0 FAIL`, `0 ERROR`, incluindo 13 testes novos em `tests/test_markmap_phase_a_v240.py` e 111 testes de regressão preservados)
  4. `python scripts/build.py` → 8 pacotes ZIP de plataforma + candidato a ChatGPT Plugin + snapshot GitHub + `dist/manifest-sha256.json` (`PASS`)
  5. `python scripts/validate.py` (pós-build) → `platform_packages_checked: 8`, `plugin_candidates_checked: 1` (`PASS`)
  6. `python scripts/verificar_versao.py --dist` → `AXI: oito instaladores e manifesto SHA256 verificados` (`PASS`)

---

## 2. Matriz de Cenários do Contrato Visual A/I (`A01–A08`, `I01–I03`, `X01`, `F01`)

Oráculo de referência: `docs/REQUISITOS-VISUAIS-AXI-v2.4.0.md` e `tests/test_markmap_phase_a_v240.py`.

| Caso | Entrada / Escopo | Oráculo esperado | Veredicto estrutural / local | Evidência observada |
|---|---|---|---|---|
| `A01` | Hierarquia fiel (`Escola → Gestão/Ensino/Infraestrutura/Comunidade`) | Markmap `layout: tree` + `theme: cards` (esquerda→direita) visível na tela ou prévia | **PASS** (estrutural) | `test_a01_hierarchical_requires_markmap_tree_cards_rendered` (`SKILL.md`, `FLUXO-LEITURA-INTEGRAL.md`, `ROTEAMENTO-VISUAL-ANALISE.md`) |
| `A02` | `A01` sem Markmap nativo, com recurso gráfico local disponível | Figura SVG/PNG equivalente exibida e identificada como equivalente | **PASS** (estrutural + prévia local PNG) | `test_a02_visual_fallback_when_markmap_unavailable`; geração e inspeção visual direta de PNG estático local no Antigravity via `read_file` |
| `A03` | `A01` sem quaisquer meios visuais funcionais | Decomposição textual + aviso `ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO` | **PASS** (estrutural) | `test_a03_textual_fallback_declares_partial_delivery` |
| `A04` | `A01` entregue só como bloco Markdown/YAML ou arquivo sem prévia | Reprovado (`NÃO CONFORME`) | **PASS** (estrutural) | `test_a04_code_snippet_only_is_non_compliant` |
| `A05` | Questão direta sem hierarquia útil | Sem árvore obrigatória; resposta proporcional | **PASS** (estrutural) | `test_a05_non_hierarchical_question_no_forced_tree` |
| `A06` | Objeto com múltiplos pais / arestas cruzadas essenciais | Delimitar perspectiva ou evitar árvore enganosa | **PASS** (estrutural) | `test_a06_cross_cutting_or_multiple_parents_limit` |
| `A07` | Dados sigilosos com renderer remoto não autorizado | Não transmitir dados sem autorização; usar meio local ou fallback | **PASS** (estrutural) | `test_a07_privacy_no_unauthorized_external_renderer` |
| `A08` | Diagrama exibido com partes/filiações inventadas | Reprovado (`NÃO CONFORME`) | **PASS** (estrutural) | `test_a08_fabricated_parts_non_compliant` |
| `I01–I03` | Fluxos reais vs. código isolado vs. objeto estático na Fase I | Preserva Mermaid/imagem obrigatória em fluxo real; reprova código isolado; não inventa fluxo | **PASS** (estrutural) | `test_i01_i02_i03_phase_i_mermaid_regression_preserved` + suíte v2.3.8 (`111` testes intactos) |
| `X01` | Analogia com diferenças e limites na Fase X | Correspondências, diferenças e limites sem impor gráfico | **PASS** (estrutural) | `test_x01_expansion_no_mandatory_second_chart` |
| `F01` | Saída fechada estrita (`JSON`/`CSV`/código) | Respeitar formato sem injetar imagem ou rodapé | **PASS** (estrutural) | `test_f01_closed_format_json_csv_code_exemption` + `test_deterministic_oracles` |

---

## 3. Verificação por Plataforma (oito ambientes) e Protocolo Científico

| Plataforma | Pacote e guia v2.4.0 | Veredicto estrutural / ZIP | Teste em UI externa real | Critério pendente / Limitação |
|---|---|---|---|---|
| `chatgpt-web` | `axipesquisa-2.4.0-chatgpt-web.zip` | **PASS** | **SKIP** | Sem sessão Web externa autenticada no runner; validar prévia Markmap/equivalente e Mermaid na UI ChatGPT |
| `gemini-web` | `axipesquisa-2.4.0-gemini-web.zip` | **PASS** | **SKIP** | Sem sessão Gemini Web no runner; validar invocação direta de imagem SVG/PNG com Skill ativa |
| `claude-web` | `axipesquisa-2.4.0-claude-web.zip` | **PASS** | **SKIP** | Sem sessão Claude Web no runner; validar visual personalizado HTML/SVG ou Artifact renderizado |
| `grok-web` | `axipesquisa-2.4.0-grok-web.zip` | **PASS** | **SKIP** | Sem sessão Grok Web no runner; validar cartão SVG inline ou HTML Preview em Projects |
| `codex` | `axipesquisa-2.4.0-codex.zip` | **PASS** | **SKIP** | Sem execução em sessão Codex CLI/IDE distinta; validar prévia local ou aviso `ENTREGA PARCIAL` |
| `claude-code` | `axipesquisa-2.4.0-claude-code.zip` | **PASS** | **SKIP** | Sem sessão Claude Code no runner; validar visualizador local da IDE |
| `antigravity` | `axipesquisa-2.4.0-antigravity.zip` | **PASS** | **PASS (parcial local PNG)** | Geração e exibição visual de PNG estático local verificada via `read_file`; renderização nativa de Markmap em chat não testada |
| `grok-build-cli` | `axipesquisa-2.4.0-grok-build-cli.zip` | **PASS** | **SKIP** | Sem sessão Grok Build CLI no runner; validar renderer local |

- **Preservação do protocolo científico (`C0/C1/C2` em `v2.2.0-rc2`):** `test_frozen_scientific_protocol_and_core_hashes_preserved` → **`PASS`**. Todos os 7 arquivos em `tests/fixtures/preservation.json` + `EXEMPLOS-E-TESTES.md` mantêm seus hashes SHA-256 exatos e os 36 casos em `tests/cases.json` permanecem com `status: "not-run-on-llm"`.
- **Resumo numérico:** `124` testes unitários executados → **`124 PASS`**, **`0 FAIL`**, **`0 ERROR`**; `7` plataformas externas marcadas **`SKIP`** (não executadas por ausência de sessão Web/CLI externa). **Testes estruturais não equivalem a validação científica empírica nem a homologação nativa em contas Web.**

---

## 4. Fontes consultadas (ABNT)

- AXI PESQUISA. **Contrato visual A/I (`docs/REQUISITOS-VISUAIS-AXI-v2.4.0.md`) e suíte de testes (`tests/test_markmap_phase_a_v240.py`)**. 2026. Disponível em: https://github.com/wilkermaa/axipesquisa/pull/23. Acesso em: 19 nov. 2026.

◌ SOPRO GPDO
