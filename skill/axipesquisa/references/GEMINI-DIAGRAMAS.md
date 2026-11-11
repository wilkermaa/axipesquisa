# Gemini Web — PNG primeiro, não snippet Mermaid (v2.3.10)

**REGRA INEGOCIÁVEL:** quando a microfase I — Diagramação do Fluxo de Aplicação — encontrar um fluxo juridicamente fiel, **ACIONAR DE FATO A GERAÇÃO DE IMAGEM PNG, MOSTRAR A FIGURA NO CHAT e SÓ DEPOIS CONCLUIR A RESPOSTA**. O código Mermaid, SVG ou HTML pode ser usado internamente, mas **NUNCA pode ser exibido como substituto do PNG**, nem sob a expressão “Registro de Entrega Visual Parcial”. O objetivo é imagem renderizada, não snippet.

## Procedimento em ordem obrigatória: EXECUTAR → MOSTRAR → VERIFICAR → FINALIZAR

0. **Analisar e pesquisar:** confirmar fontes jurídicas locais, artigos, modalidades, condições e fluxo antes do desenho; fazer A e X; não inventar requisitos, prazos, anuências, portarias, autoridades ou caminhos. Pesquisa jurídica, ABNT e imagem são deveres independentes.
1. **EXECUTAR PNG AGORA:** invocar/acionar efetivamente a ferramenta de criação de imagens do Gemini, se acessível na sessão com Skill ativa. Prompt instrumental: **“Gere e EXIBA AGORA uma imagem PNG de fluxograma estático, com blocos e setas apenas das etapas verificadas abaixo. Não escreva código, Mermaid, SVG XML, HTML, tabela nem arte ASCII. Apenas apresente a imagem desenhada: [etapas e decisões confirmadas].”** Se precisar, Mermaid é apenas representação **interna**, nunca saída ao usuário. Não usar como ação suficiente a simples frase “vou gerar” ou uma instrução que não invoque ferramenta.
2. **MOSTRAR E VERIFICAR PNG:** certificar-se de que uma imagem renderizada foi realmente apresentada no chat ou em prévia gráfica aberta. **A presença do botão de imagem não prova invocação**; a frase “indisponibilidade gráfica” tampouco prova falha concreta. **Verifique antes de responder**.
3. **ESTÉTICA APÓS O PNG:** seguir o estilo visual Mermaid minimalista, **CAIXAS SÓ COM TÍTULOS CURTOS**, ideal uma linha, no máximo duas linhas curtas; **SEM ÍCONES, SEM DESCRIÇÕES, SEM SUBTÍTULOS, SEM MICROTEXTOS OU PARÁGRAFOS DENTRO DAS CAIXAS**. Decisões e setas com rótulos curtos como `Sim`, `Não`, `De ofício`, `A pedido`, `Permuta`. Detalhes jurídicos e **Fontes consultadas (ABNT) fora da imagem**. Se houver excesso, **tentar uma única regeneração simplificada**, mantendo os nós e as conexões; a exigência estética não pode bloquear a geração inicial.
4. **RECUPERAR, SEM MOSTRAR SNIPPET:** se o PNG não aparecer, **tente uma alternativa gráfica funcional** que produza imagem **visível**. Exemplo: SVG já renderizado ou PNG de renderizador realmente disponível, prévia nativa estática. Se o motor usar internamente `flowchart TD`, renderizar antes da entrega; **não enviar bloco ```mermaid, XML SVG como texto, HTML como texto, ASCII ou tabela**. **SVG já renderizado ou PNG**, nunca código. Canvas com SVG e prévia pode ser fallback estático somente se realmente acessível, mas o Google documenta que Canvas **não funciona com Skills**; isso não autoriza presumir bloqueio sem observar uma tentativa.
5. **FALHA OBSERVADA E HONESTIDADE:** só declarar falta de recurso após tentativa real ou impossibilidade efetivamente verificada. **Não inventar prévias** ou ações; **não declarar impossível** sem verificar a sessão. Se nenhum mecanismo produzir imagem visível, responder em uma frase: **“Entrega visual não realizada: não foi possível produzir uma imagem nesta sessão.”** **Não acrescentar código Mermaid/SVG/HTML** e não alegar conclusão. Essa condição é **entrega parcial**; a Skill não habilita ferramentas que não estão disponíveis no produto.
6. **ENTREGAR AXI COMPLETA APENAS COM IMAGEM:** depois de conferir o gráfico, concluir texto A/X/I de forma concisa, mantendo pesquisa jurídica fundamentada e fontes reais em ABNT fora da imagem. **Não obrigar PDF nem download**; **PDF não é obrigatório**; aplicativo interativo apenas se o usuário pedir expressamente. **Privacidade**, legibilidade, fidelidade e **minimizar tokens** prevalecem.

## Oráculo de aceitação

| Saída vista no Gemini | Resultado |
|---|---|
| PNG visível com caixas de títulos curtos e conexões corretas | **Aceito visualmente** |
| PNG visível, mas caixas poluídas | **Corrigir estética uma vez** |
| SVG efetivamente renderizado na prévia, PNG indisponível após tentativa real | **Aceito como imagem de fallback, registrar formato** |
| “Registro de Entrega Visual Parcial” seguido de ```mermaid ou `flowchart TD` | **Reprovado**: código não é imagem |
| Texto dizendo indisponibilidade, sem tentativa observável | **Reprovado**: não comprova execução |
| Falha real da ferramenta + tentativa gráfica alternativa sem imagem | **Entrega parcial**, frase sem código |

**Regressão concreta (Guaratuba, 11/11/2026):** a resposta apresentou “Registro de Entrega Visual Parcial” e trecho Mermaid após afirmar indisponibilidade gráfica. O material fornecido pelo usuário **não prova que o modelo acionou qualquer ferramenta**; também não prova que estava indisponível. Esse comportamento reprova v2.3.9. O novo contrato exige executar PNG e proíbe snippet como compensação.

**Limite externo:** o Google documenta que Skills não funcionam com determinados recursos, inclusive Canvas, mas não garante nem exclui genericamente o acionamento de imagens em todas as contas/modelos. **Testes estáticos não demonstram renderização real** no Gemini; homologação precisa de captura, modelo/esforço, versão instalada e ação de ferramenta observada. A v2.3.8 teve sucesso relatado após novo pedido com esforço máximo; essa observação não estabelece causalidade nem permite à Skill selecionar esforço por conta própria.

GOOGLE. *Gerar e editar imagens com os apps do Gemini*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/14286560?hl=pt-BR. Acesso em: 11 nov. 2026.
GOOGLE. *Sobre a transição dos Gems para habilidades*. 2026. Disponível em: https://support.google.com/gemini/answer/18560919?hl=pt-BR. Acesso em: 11 nov. 2026.
