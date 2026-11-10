# Solicitação de reprodução independente: AXI-Pesquisa

**Responsável pelo projeto:** Wilker M. de Araujo Alexandre.
**Pesquisador convidado:** Rafaell (aluno do autor).
**Versão congelada para comparação:** 2.2.0-rc2. **Situação em 10/11/2026:** a distribuição atual é 2.2.1; o benchmark original mantém o congelamento da rc2. Não misturar intervenções entre condições.
**Situação científica:** hipótese metodológica, não eficácia comprovada.

## Objetivo

Testar de modo reproduzível se instruções AXI melhoram respostas em comparação às condições sem AXI (C0) e orientação genérica (C1). Não presumir superioridade.

## Atividades e critérios de entrega

1. Inspecionar os 36 cenários em `tests/cases.json`, confirmar gabaritos e detectar ambiguidade. Não alterar cenários congelados; registrar erratas separadamente.
2. Garantir a mesma pergunta em C0, C1 e C2 para cada cenário, em chats novos, com a mesma versão/modelo e ferramentas equivalentes.
3. Usar C0 sem instruções; C1 com prompt genérico congelado; C2 com o AXI completo congelado (2.2.0-rc2), sem skill nativa ativada. Não misturar variantes.
4. Registrar **216 execuções por plataforma**, quando viável (36 × 3 × 2), com data, modelo, prompt, condições, resposta integral, links ou capturas, falhas e ferramentas disponíveis. Nunca fabricar conversas não executadas.
5. Executar validações de formatos e de registros; apresentar logs e relatório dos dados ausentes ou invalidados.
6. Planejar avaliação cega por pelo menos dois avaliadores que não participaram da elaboração do AXI, e documentar o vínculo acadêmico entre Rafaell e o autor.
7. Reportar tanto resultados favoráveis quanto desfavoráveis e os intervalos de incerteza; separar desempenho textual, segurança e aprendizagem por leitores.
8. Apresentar um estudo adicional com cenários novos, pré-registro do desfecho primário e critérios de sucesso antes de ver os resultados.

## Entregáveis aceitos

- `executions.jsonl` ou equivalente com rastreabilidade por `job_id`;
- arquivos originais sem edição;
- manifesto SHA-256 das respostas e anexos;
- relatório de resultados e exclusões;
- rubrica de avaliação e registro de divergências;
- limitações e conflitos de interesse (inclusive vínculo acadêmico);
- recomendação sobre próxima versão, **sem chamar o método de cientificamente comprovado sem evidência**.

## Estado de execução

As 432 respostas oficiais **não estão coletadas** nesta release. Os testes estruturais de software não substituem os resultados experimentais.

Este documento é um plano para execução; não constitui encomenda de dados fictícios nem compromisso de autoria de publicação.
