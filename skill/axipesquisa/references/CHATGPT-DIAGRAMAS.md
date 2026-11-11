# ChatGPT — seleção econômica do renderizador visual (fase I)

Aplicar após `references/ROTEAMENTO-VISUAL.md`. **Não confundir disponibilidade anunciada com recurso presente na sessão.** A prévia pode depender de dispositivo, plano e workspace.

1. **Texto suficiente e sem pedido explícito:** não criar imagem/diagrama.
2. **Fluxo, sequência, arquitetura, grafo de relações:** quando a interface habilitar prévia de bloco Mermaid, gerar **um bloco Mermaid mínimo e válido** e usar a prévia. Não criar HTML, PNG e SVG em paralelo sem pedido.
3. **Dados quantitativos:** quando disponível, preferir gráfico integrado ou **Vega/Vega-Lite** com unidades, legendas e escalas verificáveis; não forçar Mermaid para números.
4. **Interatividade expressamente necessária:** preferir visualização interativa nativa habilitada, com controles reais; não criar aplicação somente por ser tecnicamente possível.
5. **Prévia ausente:** tentar uma alternativa comprovadamente disponível, como SVG exibível ou arquivo SVG local; HTML/React só se necessário para visualização/controles. Caso nenhuma esteja habilitada, oferecer fonte válida e declarar entrega visual parcial.
6. **Exportação:** SVG/PNG apenas conforme pedido e ferramenta real; links verificáveis. Se exigidos ambos, tentar produzi-los; não confundir código SVG com arquivo baixável.

**Economia e fidelidade:** uma tentativa nativa adequada + uma alternativa viável; evitar pesquisa externa, gerações de imagem rasterizada desnecessárias e novos plugins. Preservar nós, arestas, valores, acessibilidade, privacidade e limites das ferramentas.

**Verificação de uso:** um fluxograma Mermaid visível e um gráfico numérico Vega-Lite visível, em testes independentes, com registro de prévia, exportação e recursos efetivos. A Skill não controla o renderer do frontend.

OPENAI. *Working with writing blocks and code blocks in ChatGPT*. [s.d.]. Disponível em: https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt. Acesso em: 11 nov. 2026.
