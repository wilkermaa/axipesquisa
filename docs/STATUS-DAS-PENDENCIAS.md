# Status verificável das quatro pendências (v2.2.1)

Status revisto em: 06/11/2026. Plano experimental original de 04/11/2026 preservado. **Não declarar aprovação definitiva.**

| Pendência | Entrega realizada | Condição ainda não demonstrada |
|---|---|---|
| 36 cenários adversariais em modelos reais | Casos versionados, executor multi-API, oráculos limitados e testes de infraestrutura | **0/36 cenários executados nos provedores reais neste ambiente**. Sem chaves de API, logo sem chamadas cobradas. |
| Comparar sem AXI / orientação genérica / AXI | Experimento balanceado 36×3×2, aleatorização, mesmo prompt e modelo, exportação cega, rubrica e análise | Nenhuma resposta nem nota humana real coletada. Não há ganho científico comprovado. |
| Licença | Proposta MIT para scripts e CC BY 4.0 para textos registrada | Nome público confirmado em 04/11/2026; resta revisão final de direitos de terceiros. |
| ChatGPT Web e Plugins | Compatibilidade separada para skill carregada localmente e plugin publicado; pacote de plugin com manifesto preparado | Aceitação da conta e aprovação da publicação não testadas. |

## Contagens

- 36 casos únicos em `tests/cases.json`.
- 3 condições: baseline, genérica e AXI.
- 2 repetições planejadas: **216 solicitações por modelo** (não executadas).
- OpenAI, Anthropic, Gemini, xAI: **864 solicitações planejadas se executar um modelo de cada provedor** (não executadas).
- A execução nas APIs **não verifica instalação da skill em cada interface Web**; o modo é `prompt-equivalent-no-tools`.
- Ferramentas externas e busca foram desativadas para preservar simetria entre condições; o cenário T13 deve avaliar honestidade de acesso e não a capacidade de pesquisa ao vivo.

## Decisão de release

O projeto é **publicável como pesquisa experimental, após revisar direitos de terceiros e credenciais**, com declaração explícita de eficácia ainda não demonstrada. Não é elegível para selo “comportamento validado”, “cientificamente superior” ou “blindado”.

## Correção pré-publicação (05/11/2026) e política visual (06/11/2026)

A auditoria de nomenclatura separa relatórios históricos da v2.1.0-rc1 da versão atual v2.2.1. Nenhum teste em LLM real é declarado por essa revisão documental. As respostas do piloto ChatGPT/Gemini permanecem exploratórias e não são contabilizadas nos 432 trabalhos oficiais por falta de comprovação de isolamento, paridade de prompts e execução.

Rafaell poderá coordenar o teste de reprodutibilidade, mas sua condição de aluno do autor exige declaração de vínculo e recrutamento de avaliadores adicionais para a etapa de avaliação independente.

## Regra de compatibilidade com os experimentos em andamento

A política Mermaid foi incorporada à **v2.2.1** para novos usos da Skill. O benchmark comparativo iniciado com a **v2.2.0-rc2** permanece congelado nessa versão. Não substituir os prompts de C2 por rc3 durante as 432 tarefas planejadas sem criar outro braço de estudo ou reiniciar todo o protocolo com registro explícito.
