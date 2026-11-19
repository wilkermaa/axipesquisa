# AXI Pesquisa v2.4.0 — Perfil de condução por Orchestrator (Argon)

**Perfil:** AXI240-ARGON-1.0.0 · **Decisão da direção:** 19/11/2026, solicitação expressa de operar as issues pelo Orchestrator (Argon).  
**Estado:** execução da fila `#16 → #22` conduzida e consolidada sob mandato expresso da Direção Humana em `19/11/2026`.  
**Repositório:** https://github.com/wilkermaa/axipesquisa  
**Baseline anterior:** v2.3.8 na `main`; **release preparada na #22:** v2.4.0 (PR #23).

## Modelo e papel

**Canal de operação:** Google Antigravity, opção **Orchestrator (Argon)**.

**Unidade operacional:** uma conversa/tarefa do Antigravity, com planner Gemini 4 Argon e executor de implementação Gemini 4 Hydrogen. **Esforço: não ajustável no modo Orchestrator** — não usar `--effort High` ou rótulos de esforço inventados. A alternância interna é um comportamento documentado do produto; não cria autorização para múltiplas issues paralelas. Confirmar modelo disponível e limites/cota na conta antes de iniciar cada issue.

**Operador do disparo:** direção humana. **Orquestrador/execução técnica:** Antigravity Orchestrator (Argon), com pareamento gerenciado (Argon + Hydrogen).

## Fila PEC — WIP global=1

| Ordem | Issue | Disciplina | Condução | Gate |
| --- | --- | --- | --- | --- |
| 1 | #16 | ANÁLISE | ChatGPT, histórico concluído | CLOSED (`005316f6`) |
| 2 | #17 | DESENVOLVIMENTO | ChatGPT (início) + Argon (reconciliação autorizada em 19/11/2026) | CLOSED (`ffb21e1c`, CI `44622309073`) |
| 3 | #18 | DESENVOLVIMENTO | Orchestrator (Argon) | CLOSED (`f2c3e81c`, CI `44622925185`) |
| 4 | #19 | TESTES | Orchestrator (Argon) | CLOSED (`889379fc`, CI `44623371440`) |
| 5 | #20 | QUALIDADE | Orchestrator (Argon) sob delegação expressa de 19/11/2026 | CLOSED (`98afb5d0`, CI `44623999373`) |
| 6 | #21 | GOVERNANÇA | Direção humana (`19/11/2026`) / registro Argon | CLOSED (`791567b6`, CI `44624278500`) |
| 7 | #22 | CONFIGURAÇÃO | Orchestrator (Argon) sob autorização expressa | Em execução até fechamento de tag/release e readback |

## Registro de deliberação soberana de 19/11/2026

- Em `19/11/2026`, após o bloqueio inicial G2 registrado na issue `#17` (`issuecomment-7022765426`), a Direção Humana (`wilkermaa`) determinou expressamente: *"nao há bloquei, vc vai cumprir todos os papeis de todos os atores, continue agora"*.
- Nos termos da `PEC-001 §11` (precedência de decisões explícitas da direção) e `§5`, o Orchestrator (Argon) preservou integralmente os commits anteriores do ChatGPT/GPT-6 (`005316f`, `04a33c4`, `9031697`, `bb36e7b`), manteve `WIP global = 1` estrito, segregou os entregáveis por disciplina e executou toda a fila até `#22`, deixando explícito nas atas de `#20`, `#21` e `#22` que a revisão de qualidade não pretendeu substituir auditoria externa independente e que os ensaios nas UIs Web externas permanecem `SKIP` / pendentes de homologação em produto.

**Políticas canônicas:** [PEC-001](https://github.com/wilkermaa/politica-de-execucao-continua/blob/main/politica/PEC-001-POLITICA-EXECUCAO-CONTINUA-v1.0.0.md); [Política de issues](https://github.com/wilkermaa/politica-issues); [AXI Pesquisa](https://github.com/wilkermaa/axipesquisa/blob/main/POLITICA-ORGANIZACIONAL.md).

**Docs de modelo:** https://antigravity.google/docs/models.

## Restrições de produto

- Na A com hierarquia real, Markmap Tree + Cards como visualização prioritária, imagem efetivamente desenhada/aberta; sem Markmap, imagem equivalente, e, se nenhum visual possível, decomposição textual com ENTREGA PARCIAL.
- Na I com fluxo real, Mermaid/visual equivalente realmente renderizado; não trocar imagem por código.
- Não alegar eficácia científica nem homologação em oito plataformas só por ZIP/teste textual.
- Não reescrever tags anteriores (`v2.3.8`, `v2.3.9`, `v2.2.0-rc2` etc.).

◌ SOPRO GPDO AXI
