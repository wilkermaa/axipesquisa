# Auditoria de restauração v2.0.0 → v2.3.6

**Base histórica:** `v2.0.0/fonte-canonica/references/AXI-METODO.md`, `v2.0.0/alternativas/CHATGPT-INSTRUCOES-PERSONALIZADAS.md`, `v2.0.0/fonte-canonica/references/FONTES-E-ABNT.md`. **Ponto atual:** `v2.3.6/skill/axipesquisa/SKILL.md`. O inventário estático não demonstra desempenho funcional de modelos.

| Instrução | Estado na v2.3.5 | Restauração v2.3.6 |
|---|---|---|
| Leitura completa do método | Guia detalhado condicional e histórico Grok requeria integral | `SKILL.md` inteiro + referências/anexos faseados e completos, sem resumos |
| ABNT ao final de cada explicação ou pesquisa | Redação mais restrita à pesquisa | `Fontes consultadas (ABNT)` obrigatório em ambos os tipos; ausência de consulta explicitada |
| Comparações reais, virtuais, conceituais, metafísicas | Metafísico preservado no core, omitido no fallback ChatGPT | Quatro domínios novamente citados no fallback |
| 12 exemplos da v2.0 | Arquivo preservado por SHA-256; leitura opcional | Leitura integral do arquivo obrigatória, **sem executar ou reproduzir** 12 exemplos à toa |
| Erin Meyer e oito perguntas | Conteúdo preservado | Leitura integral no meio/X sem estereótipos, não aplicação automática |
| Diagramação I | Genérica com Gemini SVG sem acionamento garantido | Rotas priorizadas por produto, aceitação por visual real |
| Assinatura | Config neutra em vez de dados pessoais históricos | Preservada assinatura escolhida pelo usuário, sem redistribuir PII |

**Compatibilidade documentada:** Skills no Gemini ainda não funcionam com Canvas; exigir Canvas+SVG como caminho de execução futuro/caso habilitado não é garantia técnica. Modelos devem verificar a integração e não afirmar sucesso inexistente. Não forçar JavaScript em Skills.

**Proteções históricas:** não modificar SHA-256 original de `references/EXEMPLOS-E-TESTES.md` e dos 7 arquivos congelados da v2.2.2; C0/C1/C2 v2.2.0-rc2 intacto. CI testa integridade e instruções, não execução completa em oito interfaces.

