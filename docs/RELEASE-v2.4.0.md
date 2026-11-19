# AXI Pesquisa v2.4.0 — Markmap Tree + Cards na fase A e Mermaid preservado na fase I

**MINOR · 19 nov. 2026.** Escopo: introdução da microfase visual da **Análise (fase A)** com **Markmap** no padrão `layout: tree` + `theme: cards` (leitura da esquerda para a direita em cartões), preservando integralmente a microfase **Diagramação do Fluxo de Aplicação (Mermaid/imagem obrigatória na fase I)** e todas as regras da baseline aprovada [v2.3.8](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.8).

## O que muda nesta versão

- **Fase A — Análise hierárquica (`references/ROTEAMENTO-VISUAL-ANALISE.md` e `SKILL.md`):**
  - Havendo decomposição hierárquica fiel (`todo → partes → subpartes`), priorizar **Markmap** com `layout: tree` e `theme: cards` **efetivamente renderizado e visível na tela ou em prévia gráfica aberta**.
  - Código Markdown/YAML, snippet Markmap, tabela, ASCII ou arquivo criado em disco sem prévia **não** satisfazem o aceite visual.
  - **Fallback visual:** quando Markmap estiver indisponível, gerar e exibir figura equivalente (`SVG`/`PNG`/visual nativo) com leitura esquerda→direita e identificá-la como equivalente.
  - **Fallback textual:** sem qualquer meio visual disponível após tentativa alternativa, entregar decomposição textual explícita declarando **`ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO`** e a limitação observada.
  - **Limites:** não inventar árvore em pergunta trivial, relações transversais/múltiplos pais incompatíveis com árvore ou formatos fechados (`JSON`, `CSV`, `SQL`, código puro). Proibido enviar dados privados a renderizadores externos sem autorização.
- **Fase I — Integração (`references/ROTEAMENTO-VISUAL.md`):** preserva integralmente a microfase de fluxos reais (Mermaid renderizado em prévia ou imagem equivalente exibida), fontes ABNT e protocolo jurídico (`PROTOCOLO-JURIDICO-ABNT.md`). O mapa da A **não substitui** o fluxograma da I.
- **Oito plataformas (`references/PLATAFORMAS-VISUAIS.md`, guias dedicados, `docs/PLATAFORMAS.md` e `scripts/build.py`):** cada um dos oito instaladores inclui `INSTALADOR-PLATAFORMA.md` com rotas específicas de Fase A e Fase I, sem presumir suporte nativo de Markmap não comprovado e sem exigir aplicativo interativo.

## Rastreabilidade, testes e ressalvas obrigatórias

- **Fila PEC-001 executada (`#16` a `#22`):** contrato visual (`docs/REQUISITOS-VISUAIS-AXI-v2.4.0.md`), desenvolvimento (`#17`–`#18`), regressão (`docs/RELATORIO-TESTES-v2.4.0.md`), revisão de qualidade e Red Team (`docs/PARECER-QUALIDADE-v2.4.0.md`) e decisão de governança (`docs/DECISAO-GOVERNANCA-v2.4.0.md`, sob mandato expresso da Direção Humana em `19/11/2026`).
- **Verificações executadas:** `124/124` testes unitários/estruturais **`PASS`** (`tests/test_markmap_phase_a_v240.py` + suíte regressiva), validação estática (`scripts/validate.py`) e construção/verificação SHA-256 dos oito pacotes (`scripts/build.py` e `scripts/verificar_versao.py --dist`). No ambiente `Antigravity`, foi validada geração e inspeção visual local de diagrama PNG estático.
- **Limitações e ressalvas (obrigatórias):**
  1. **Testes automatizados são estruturais/estáticos:** **não comprovam eficácia científica** nem garantem renderização nativa automática em contas externas.
  2. **Homologação em UIs externas pendente (`SKIP`):** `ChatGPT Web`, `Gemini Web`, `Claude Web`, `Grok Web`, `Codex CLI`, `Claude Code` e `Grok Build CLI` não foram executadas em contas externas nesta release e permanecem pendentes de teste funcional em produto.
  3. **Preservação científica e histórica:** protocolo experimental `C0/C1/C2` (`v2.2.0-rc2`, `tests/cases.json`), hashes protegidos (`tests/fixtures/preservation.json`) e todas as tags anteriores (`v2.3.8`, `v2.3.9` etc.) permanecem intactos.

## Fontes consultadas (ABNT)

- MARKMAP. *Themes and layouts*. [s.d.]. Disponível em: https://markmap.js.org/docs/guide/themes-and-layouts. Acesso em: 19 nov. 2026.
- MARKMAP. *Options*. [s.d.]. Disponível em: https://markmap.js.org/docs/guide/options. Acesso em: 19 nov. 2026.
- MERMAID. *About Mermaid*. [s.d.]. Disponível em: https://mermaid.js.org/intro/. Acesso em: 19 nov. 2026.
