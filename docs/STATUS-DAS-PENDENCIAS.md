# Status verificável das quatro pendências (v2.2.0-rc2)

Data: 04/11/2026. **Não declarar aprovação definitiva.**

| Pendência | Entrega realizada | Condição ainda não demonstrada |
|---|---|---|
| 36 cenários adversariais em modelos reais | Casos versionados, executor multi-API, oráculos limitados e testes de infraestrutura | **0/36 cenários executados nos provedores reais neste ambiente**. Sem chaves de API, logo sem chamadas cobradas. |
| Comparar sem AXI / orientação genérica / AXI | Experimento balanceado 36×3×2, aleatorização, mesmo prompt e modelo, exportação cega, rubrica e análise | Nenhuma resposta nem nota humana real coletada. Não há ganho científico comprovado. |
| Licença | Matriz de decisão e recomendação documentadas | Titular ainda precisa autorizar uma licença e identificação de copyright. **Não existe LICENSE concedida.** |
| ChatGPT Web e Plugins | Compatibilidade separada para skill carregada localmente e plugin publicado; pacote de plugin com manifesto preparado | Aceitação da conta e aprovação da publicação não testadas. |

## Contagens

- 36 casos únicos em `tests/cases.json`.
- 3 condições: baseline, genérica e AXI.
- 2 repetições planejadas: **216 solicitações por modelo** (não executadas).
- OpenAI, Anthropic, Gemini, xAI: **864 solicitações planejadas se executar um modelo de cada provedor** (não executadas).
- A execução nas APIs **não verifica instalação da skill em cada interface Web**; o modo é `prompt-equivalent-no-tools`.
- Ferramentas externas e busca foram desativadas para preservar simetria entre condições; o cenário T13 deve avaliar honestidade de acesso e não a capacidade de pesquisa ao vivo.

## Decisão de release

O projeto é **publicável como pesquisa experimental, apenas após resolver licença e revisar credenciais**, com declaração explícita de eficácia ainda não demonstrada. Não é elegível para selo “comportamento validado”, “cientificamente superior” ou “blindado”.
