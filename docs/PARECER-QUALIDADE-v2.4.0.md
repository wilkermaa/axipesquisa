# Parecer Técnico de Qualidade e Red Team — AXI Pesquisa v2.4.0 (Issue #20)

**Disciplina:** `QUALIDADE` ([Issue #20](https://github.com/wilkermaa/axipesquisa/issues/20)) · **PR:** [#23](https://github.com/wilkermaa/axipesquisa/pull/23)  
**SHA auditado:** `889379fc034d518f30ff28bc45f769646edb9fcd` (`feat/axi-v2.4.0-markmap-fase-a`)  
**Baseline comparada:** tag `v2.3.8` (`a59f99bc5d0af0c5d0c67f38f6ac0151aa327970` na `main`)  
**Atuação e transparência:** auditoria realizada pelo **Orchestrator (Argon)** sob delegação expressa da Direção Humana em `19/11/2026` (*"nao há bloquei, vc vai cumprir todos os papeis de todos os atores, continue agora"*). Este documento **não** simula um avaliador humano distinto; registra integralmente os achados verificáveis por SHA e mantém reservadas as limitações empíricas e de UI.

---

## 1. Inventário do Diff (`v2.3.8..889379fc034d518f30ff28bc45f769646edb9fcd`) e Integridade Histórica

- **Escopo alterado desde `v2.3.8` (22 arquivos):**
  - Contrato e documentação: `CHANGELOG.md`, `VERSION`, `docs/REQUISITOS-VISUAIS-AXI-v2.4.0.md`, `docs/PLATAFORMAS.md`, `docs/POLITICA-VISUAL.md`, `docs/RELATORIO-TESTES-v2.4.0.md`.
  - Skill e guias de plataforma: `skill/axipesquisa/SKILL.md`, `README-INSTALACAO.md`, `references/FLUXO-LEITURA-INTEGRAL.md`, `references/ROTEAMENTO-VISUAL-ANALISE.md` (novo), `references/ROTEAMENTO-VISUAL.md`, `references/CHATGPT-DIAGRAMAS.md`, `references/GEMINI-DIAGRAMAS.md`, `references/CLAUDE-DIAGRAMAS.md`, `references/GROK-DIAGRAMAS.md`, `references/PLATAFORMAS-VISUAIS.md`.
  - Build e validação: `scripts/build.py`, `scripts/check_release.py` (com suporte `allow_candidate=True` apenas nos testes, mantendo o gate estrito de release `--source` intacto).
  - Suíte de testes: `tests/test_content_regression.py`, `tests/test_legal_sources_regression.py`, `tests/test_renderer_routing.py` e `tests/test_markmap_phase_a_v240.py`.
- **Integridade do núcleo preservado (`MATCH` 100%):**
  - `skill/axipesquisa/references/METODO-AXI.md`: `aabb096170e6b44332be01691bd157c311c2719972be9fe512f16257eab7d459`
  - `skill/axipesquisa/references/PROTOCOLO-DE-FONTES.md`: `e2ce4f78f1b71e2162d22ce087fc18c8226fa7cfe2c9ae4f1b3332cf8e77aad2`
  - `skill/axipesquisa/references/LIMITES-E-SEGURANCA.md`: `5329aca2b175fa7813bd842247ab21755415f62a94d427859b2fe514c385d938`
  - `skill/axipesquisa/references/EXEMPLOS-E-TESTES.md`: `7d5e0a3082de56228d050ebff4c57a39d30ffd03be54d00e8bfafa37569d5f42`
  - `tests/cases.json`: `5a92d9034c97617f22f1caecd8e98f0f887084ca9cac5f3044dfb44f7eb75b17` (`36` casos `not-run-on-llm`, protocolo `v2.2.0-rc2` intacto)
  - `docs/EMBASAMENTO-CIENTIFICO.md`, `docs/RED-TEAM.md`, `scripts/make_cases.py`: hashes preservados byte a byte.

---

## 2. Matriz Red Team — Riscos Específicos da v2.4.0

| ID | Vetor de risco avaliado | Gravidade | Mitigação verificada no SHA `889379f` | Estado |
|---|---|---|---|---|
| `RT-240-01` | Árvore hierárquica artificial em pergunta trivial ou conceito não divisível | Média | `SKILL.md` ("Limites da A: não inventar árvore em pergunta trivial"), `FLUXO-LEITURA-INTEGRAL.md` ("Sem hierarquia útil, não inventar diagrama") e `ROTEAMENTO-VISUAL-ANALISE.md` item 6 | Mitigado no contrato; depende de aderência do modelo em runtime |
| `RT-240-02` | Partes ou filiações inventadas para preencher o mapa Markmap | Alta | `ROTEAMENTO-VISUAL-ANALISE.md` ("Árvore com partes/filiações inventadas → NÃO CONFORME") e `docs/REQUISITOS-VISUAIS-AXI-v2.4.0.md` (`A08`) | Mitigado no contrato |
| `RT-240-03` | Distorção de grafos com múltiplos pais / relações transversais em árvore estrita | Média | `SKILL.md` ("múltiplos vínculos incompatíveis com uma árvore") e `docs/REQUISITOS-VISUAIS-AXI-v2.4.0.md` regra 8 (`A06`) | Mitigado no contrato |
| `RT-240-04` | Vazamento de dados privados para renderizadores externos públicos | Alta | `SKILL.md`, `ROTEAMENTO-VISUAL-ANALISE.md` item 7, `PLATAFORMAS-VISUAIS.md`, `docs/PLATAFORMAS.md` e `scripts/build.py` proíbem envio sem autorização | Mitigado no contrato e validado por `test_a07_privacy_no_unauthorized_external_renderer` |
| `RT-240-05` | Falso preview: entregar snippet Markdown/YAML/SVG ou arquivo oculto como imagem entregue | Alta | `SKILL.md`, `ROTEAMENTO-VISUAL-ANALISE.md`, `CHATGPT/GEMINI/CLAUDE/GROK-DIAGRAMAS.md` e `INSTALADOR-PLATAFORMA.md` reprovam snippet isolado e arquivo não exibido | Mitigado no contrato (`test_a04_code_snippet_only_is_non_compliant`) |
| `RT-240-06` | Omissão do aviso `ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO` após falha visual | Média | `SKILL.md`, `ROTEAMENTO-VISUAL-ANALISE.md` e todos os 8 guias exigem declaração explícita e descrição da limitação | Mitigado no contrato (`test_a03_textual_fallback_declares_partial_delivery`) |
| `RT-240-07` | Regressão da Fase I (Mermaid substituído por Markmap) ou quebra de saídas fechadas (`JSON`/`CSV`) | Alta | `ROTEAMENTO-VISUAL.md` mantém exclusividade de fluxo na I; `SKILL.md` afirma "Markmap da A não substitui Mermaid da I" e prevalência de formatos fechados | Mitigado e verificado em 124 testes unitários (`test_i01_i02_i03`, `test_f01`) |
| `RT-240-08` | Alegação falsa de suporte nativo a Markmap nas oito IAs ou contaminação do experimento `C0/C1/C2` | Alta | Guias e `docs/PLATAFORMAS.md` registram explicitamente "não testado em conta real" e não presumem suporte nativo; `C0/C1/C2` `v2.2.0-rc2` preservado | Mitigado; **ressalva mantida para notas de release** |

---

## 3. Auditoria das Evidências de Testes (`docs/RELATORIO-TESTES-v2.4.0.md`)

- **Suíte determinística:** `124/124` testes `PASS` em `2.129s`, `0 FAIL`, `0 ERROR` (`test_markmap_phase_a_v240.py` + suíte de regressão `v2.3.8`), CI remoto `44623371440` `success`, `validate.py` `passed-static-only` (zero e-mails pessoais em `skill/axipesquisa/**`, YAML válido, sem symlinks ou referências quebradas).
- **Coerência `SKIP` / limitações:** o relatório de testes declara honestamente `SKIP` nas 7 plataformas externas sem sessão Web/CLI autenticada e `PASS (parcial local)` em geração/exibição estática PNG no Antigravity, sem falsos `PASS`.
- **Gate de publicação:** `scripts/check_release.py` continua bloqueando promoção até que a `#22` remova a marcação `(candidata)` e atualize `docs/RELEASE-v2.4.0.md`, `README.md` e `docs/ENCAMINHAMENTO-RAFAELL.md`.

---

## 4. Parecer Final de Qualidade

**Veredicto:** **`APROVADO COM RESSALVAS`** no SHA `889379fc034d518f30ff28bc45f769646edb9fcd`.

**Condições obrigatórias para `#21` e `#22`:**
1. Registrar nas notas da release (`docs/RELEASE-v2.4.0.md`), `README.md` e `docs/INSTALADORES.md` que as verificações automatizadas são **estruturais/estáticas** e que os testes funcionais de renderização nas oito interfaces Web/CLI permanecem pendentes de homologação em conta real (`SKIP` nos ambientes externos).
2. Manter inalterados o protocolo científico `v2.2.0-rc2` (`tests/cases.json`) e todas as tags históricas (`v2.3.8`, `v2.3.9` e anteriores).
3. Não mesclar na `main` nem publicar tag/release sem concluir `#21` (`GOVERNANÇA`) e passar `python scripts/check_release.py --source` na `#22`.

## Fontes consultadas (ABNT)

- AXI PESQUISA. **Relatório de Testes (`docs/RELATORIO-TESTES-v2.4.0.md`) e diff `v2.3.8..889379fc034d518f30ff28bc45f769646edb9fcd`**. 2026. Disponível em: https://github.com/wilkermaa/axipesquisa/pull/23. Acesso em: 19 nov. 2026.

◌ SOPRO GPDO
