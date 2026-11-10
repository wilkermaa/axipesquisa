# Relatório de regressão — AXI-Pesquisa v2.2.3

**Data:** 10 nov. 2026. **Base comparada:** código local v2.2.2, material histórico v2.0 e matriz de auditoria de 10/11/2026. **Finalidade:** controle de regressão textual e estrutural, não avaliação humana ou de modelo.

## Recuperações executadas

1. `skill/axipesquisa/references/EXEMPLOS-E-TESTES.md` restaurado **byte a byte** da v2.0: 12 casos T01–T12, prompts, critérios esperados e escore de revisão editorial 0/1/2, máximo 24. SHA-256 `7d5e0a3082de56228d050ebff4c57a39d30ffd03be54d00e8bfafa37569d5f42`.
2. Oito perguntas editoriais de Erin Meyer (Comunicar, Avaliar, Persuadir, Liderar, Decidir, Confiar, Discordar, Agendar) recuperadas no guia de edição; não são diagnósticos de indivíduos nem prova de eficácia.
3. Novo `README-INSTALACAO.md` na skill, presente em cada ZIP; explica as oito plataformas, ressalva de capacidade e isolamento do benchmark.
4. Documentação corrente corrigida para `v2.2.3`, eliminada afirmação de publicação remota não verificada e mantida a versão do protocolo científico original **2.2.0-rc2**.
5. Criada política obrigatória de versão/tag anotada em cada alteração versionada, com ferramenta `scripts/check_release.py` e CI GitHub para comparar versão no PR e exigir tag anotada no HEAD da `main`/release. **A regra só é exigível em GitHub após publicação e execução real do workflow.**
6. Dez novos testes `tests/test_content_regression.py` bloqueiam perda de 12 exemplos, oito perguntas, guardas científicas, paridade de oito pacotes e sete arquivos essenciais; manifesto de hashes salvo em `tests/fixtures/preservation.json`.

## Preservação intencional

As fases A, X e I não foram reescritas. Os sete arquivos críticos são idênticos aos da v2.2.2 (hashes controlados); os 36 cenários continuam congelados. Política Mermaid/Gemini Canvas permanece, com pedido explícito de diagrama visual e exportação SVG/PNG somente quando há recurso real.

## Execução local

**71 testes unitários/estruturais aprovados (61 anteriores + 10 novos).** `scripts/validate.py` aprovado, 8 ZIPs estruturados e candidato a Plugin gerados, arquivos ZIP validados. Nenhuma instalação Web ou teste independente de modelo foi realizada por essa atualização.

## Pendências reconhecidas

- A versão da Skill deve ser testada pelo usuário em Gemini/ChatGPT para validar a exportação de SVG/PNG, não substituída por promessa textual.
- Não existe demonstração de superioridade do AXI ou avaliação humana independente.
- A tag Git local precisa ser enviada e verificada no GitHub; não declarar release remoto antes disso.
- Importação de ZIP com referências adicionais depende da interface e do plano. A presença de arquivos em pacote não comprova aceitação em cada plataforma.
