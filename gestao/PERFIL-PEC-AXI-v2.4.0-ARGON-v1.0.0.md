# AXI Pesquisa v2.4.0 — Perfil de condução por Orchestrator (Argon)

**Perfil:** AXI240-ARGON-1.0.0 · **Decisão da direção:** 19/11/2026, solicitação expressa de operar as issues pelo Orchestrator (Argon).  
**Estado:** configuração de roteiro autorizada pela direção; **não é sessão iniciada** nem atesta quota, execução em curso, homologação ou release.  
**Repositório:** https://github.com/wilkermaa/axipesquisa  
**Baseline aprovada:** v2.3.8 na `main`; **candidata:** v2.4.0 no PR #23.

## Modelo e papel

**Canal de operação:** Google Antigravity, opção **Orchestrator (Argon)**.

**Unidade operacional:** uma conversa/tarefa do Antigravity, com planner Gemini 4 Argon e executor de implementação Gemini 4 Hydrogen. **Esforço: não ajustável no modo Orchestrator** — não usar `--effort High` ou rótulos de esforço inventados. A alternância interna é um comportamento documentado do produto; não cria autorização para múltiplas issues paralelas. Confirmar modelo disponível e limites/cota na conta antes de iniciar cada issue.

**Operador do disparo:** direção humana. **Orquestrador/execução técnica das issues futuras:** Antigravity Orchestrator (Argon), com pareamento gerenciado (Argon + Hydrogen). **Revisão independente de produto:** outro avaliador humano indicado na #20; a revisão do próprio Orchestrator não substitui auditor independente. **Homologação e autorização de release:** autor/direção na #21.

## Fila PEC — WIP global=1

| Ordem | Issue | Disciplina | Condução | Gate |
| --- | --- | --- | --- | --- |
| 1 | #16 | ANÁLISE | ChatGPT, histórico concluído | CLOSED; não reexecutar |
| 2 | #17 | DESENVOLVIMENTO | Argon a partir de transição documentada | PR #23 e CI devem ser corrigidos; não fechar por relato |
| 3 | #18 | DESENVOLVIMENTO | Orchestrator (Argon) | iniciar somente após #17 CLOSED + DoD |
| 4 | #19 | TESTES | Orchestrator (Argon) | iniciar somente após #18 CLOSED + DoD; falha de teste pode ser resultado legítimo da disciplina, não de aprovação do produto |
| 5 | #20 | QUALIDADE | Revisor independente humano, com Argon apenas apoio de coleta/síntese | iniciar após #19 CLOSED; parecer por SHA, sem autocertificação |
| 6 | #21 | GOVERNANÇA | Direção humana; Argon apenas prepara dossiê | decidir após #20 CLOSED; nunca homologar automaticamente |
| 7 | #22 | CONFIGURAÇÃO | Orchestrator (Argon), executando apenas com autorização | iniciar após #21 CLOSED + DoD e decisão autoral favorável |

**A #17 já recebeu trabalho de ChatGPT.** A direção solicitou agora condução via Argon. Essa transição é **uma exceção de continuidade a reconciliar antes de G3**: preservar commits, PR, autoria, falhas de CI e checkpoint da origem. A PEC-001 v1.0.0 restringe troca de executor em issue ativa; portanto, o Argon **não deve ignorar esse conflito**. Deve registrar em #17 a reconciliação efetiva do perfil da fila e a decisão expressa de transferência do escopo remanescente (sem apagar o executor anterior). Se o projeto adotar a proibição absoluta sem exceção, **BLOQUEAR #17** e devolver proposta de divisão mínima/encerramento legítimo à direção em vez de fingir conformidade.

## Portões G0–G7 obrigatórios

1. **G0:** reler GitHub ao vivo (issues, PR #23, branch, HEAD, CI e comentários), não usar um resumo como fonte de estado. Conferir credenciais/permissões e quota.
2. **G1–G2:** primeira pendente #17; verificar #16 CLOSED e artefato, precondições próprias, reconciliação da troca de executor e DoR da #17.
3. **G3:** iniciar **somente #17** após gate de prontidão; nada de corrida paralela ou disparo de #18 para esconder falhas.
4. **G4:** usar o corpo vigente da issue como prompt técnico integral; seguir mudanças mínimas, KISS, DRY, SemVer e AXI. Registrar checkpoint por issue.
5. **G5:** produzir commits/PR, executar CI, corrigir falhas sob responsabilidade da disciplina e submeter revisões cabíveis, sem autocertificação de QA.
6. **G6:** encerrar issue apenas com própria DoD evidenciada e estado CLOSED confirmado por readback.
7. **G7:** reconsultar GitHub e prosseguir na ordem; parar quando houver bloqueio, quota indisponível, necessidade de aprovação, desacordo de versão ou falta de autorização.

**Políticas canônicas:** [PEC-001](https://github.com/wilkermaa/politica-de-execucao-continua/blob/main/politica/PEC-001-POLITICA-EXECUCAO-CONTINUA-v1.0.0.md); [Política de issues](https://github.com/wilkermaa/politica-issues); [AXI Pesquisa](https://github.com/wilkermaa/axipesquisa/blob/main/POLITICA-ORGANIZACIONAL.md).

**Docs de modelo:** https://antigravity.google/docs/models.

## Restrições de produto

- Na A com hierarquia real, Markmap Tree + Cards como visualização prioritária, imagem efetivamente desenhada/aberta; sem Markmap, imagem equivalente, e, se nenhum visual possível, decomposição textual com ENTREGA PARCIAL.
- Na I com fluxo real, Mermaid/visual equivalente realmente renderizado; não trocar imagem por código.
- Não alegar eficácia científica nem homologação em oito plataformas só por ZIP/teste textual.
- Não reescrever tags anteriores; não publicar tag v2.4.0 ou GitHub Release sem decisão da #21 e integridade verificada.
- Operação de Argon precisa ser **iniciada pelo usuário no Antigravity**; o simples perfil/issue no GitHub não inicia nenhuma sessão.

◌ SOPRO GPDO AXI
