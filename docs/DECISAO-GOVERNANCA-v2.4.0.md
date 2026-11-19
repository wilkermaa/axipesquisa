# Dossiê e Decisão de Governança — Promoção AXI Pesquisa v2.4.0 (Issue #21)

**Disciplina:** `GOVERNANÇA` ([Issue #21](https://github.com/wilkermaa/axipesquisa/issues/21)) · **PR:** [#23](https://github.com/wilkermaa/axipesquisa/pull/23)  
**SHA candidato consolidado:** `98afb5d06fea8a7e0a0df08bb100411ad7fda66f` (`feat/axi-v2.4.0-markmap-fase-a`)  
**Autoridade de origem da decisão:** Direção Humana (`wilkermaa`), por despacho expresso em `2026-11-19T18:38:48-03:00` (*"nao há bloquei, vc vai cumprir todos os papeis de todos os atores, continue agora"*).

---

## 1. Dossiê de Completude das Disciplinas (`#16` a `#20`)

| Ordem | Issue | Disciplina | Estado GitHub | SHA / Artefato principal | CI / Evidência |
|---|---|---|---|---|---|
| 1 | `#16` | `ANÁLISE` | `CLOSED` | `005316f6a07b4b51b9e84de7abaf6e8bca3c4eac` · `docs/REQUISITOS-VISUAIS-AXI-v2.4.0.md` | Readback estrutural (`A01–A08`, `I01–I03`, `X01`, `F01`) |
| 2 | `#17` | `DESENVOLVIMENTO` | `CLOSED` | `ffb21e1ce15b633fa9d7fe65429615d1c76835d2` · núcleo A/I e autotestes | Run `44622309073` (`success`, `111/111 OK`) |
| 3 | `#18` | `DESENVOLVIMENTO` | `CLOSED` | `f2c3e81c18030770c1790b01f48489bbf5fa8d8a` · guias e `build.py` para 8 IAs | Run `44622925185` (`success`, `111/111 OK`) |
| 4 | `#19` | `TESTES` | `CLOSED` | `889379fc034d518f30ff28bc45f769646edb9fcd` · `docs/RELATORIO-TESTES-v2.4.0.md` e `tests/test_markmap_phase_a_v240.py` | Run `44623371440` (`success`, `124 PASS / 0 FAIL / 7 SKIP`) |
| 5 | `#20` | `QUALIDADE` | `CLOSED` | `98afb5d06fea8a7e0a0df08bb100411ad7fda66f` · `docs/PARECER-QUALIDADE-v2.4.0.md` | Run `44623999373` (`success`, `APROVADO COM RESSALVAS`) |

---

## 2. Avaliação Técnica, Lacunas e Proteção Científica

- **Markmap na Fase A e Mermaid na Fase I:** contrato A/I implementado sem quebrar a microfase I, preservando prioridade Markmap `layout: tree` + `theme: cards`, fallback visual equivalente e aviso obrigatório `ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO` em ausência de renderização visual.
- **Compatibilidade e lacunas por plataforma:** guias específicos entregues para todas as oito plataformas; **limitação explícita:** ensaios automatizados são estruturais/determinísticos e o ensaio gráfico real foi confirmado localmente em PNG no `Antigravity`, enquanto as 7 interfaces externas (`ChatGPT Web`, `Gemini Web`, `Claude Web`, `Grok Web`, `Codex CLI`, `Claude Code`, `Grok Build CLI`) permanecem registradas como `SKIP` / pendentes de homologação em conta real.
- **Preservação de pesquisa e histórico:** protocolo científico `C0/C1/C2` (`v2.2.0-rc2`, `tests/cases.json` com 36 casos `not-run-on-llm`), 8 hashes em `tests/fixtures/preservation.json`, `EXEMPLOS-E-TESTES.md` e tags históricas (`v2.3.8`, `v2.3.9` e anteriores) permanecem íntegros e sem alteração retroativa.

---

## 3. Decisão Formal de Governança

**Decisão registrada:** **`APROVAR COM CONDIÇÕES`** a promoção para `main` e a publicação da release **`v2.4.0` (MINOR)** na execução da issue `#22`, vinculada à autorização expressa da Direção Humana (`wilkermaa`, `19/11/2026`).

**Condições obrigatórias vinculadas à execução da `#22`:**
1. Promover os metadados de versão candidata para `2.4.0` (`SKILL.md`, `FLUXO-LEITURA-INTEGRAL.md`, `ROTEAMENTO-VISUAL-ANALISE.md`, `README-INSTALACAO.md`, `CHANGELOG.md`, `docs/RELEASE-v2.4.0.md`, `README.md`, `docs/ENCAMINHAMENTO-RAFAELL.md`, `docs/INSTALADORES.md`) e passar integralmente `python scripts/check_release.py --source`.
2. Declarar explicitamente nas notas públicas (`docs/RELEASE-v2.4.0.md`, `README.md` e `docs/INSTALADORES.md`) os limites observados: testes automatizados verificam integridade estrutural (`124/124`), **não** comprovam eficácia científica nem substituem homologação funcional nas oito contas/interfaces externas (`SKIP`).
3. Preservar todas as tags e releases históricos (`v2.3.8`, `v2.3.9` etc.) e publicar a tag anotada `v2.4.0` no commit de fechamento da `main` com os 8 instaladores verificados por readback e SHA-256.

## Fontes consultadas (ABNT)

- AXI PESQUISA. **Parecer de Qualidade (`docs/PARECER-QUALIDADE-v2.4.0.md`) e Relatório de Testes (`docs/RELATORIO-TESTES-v2.4.0.md`)**. 2026. Disponível em: https://github.com/wilkermaa/axipesquisa/pull/23. Acesso em: 19 nov. 2026.

◌ SOPRO GPDO
