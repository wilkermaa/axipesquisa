# ChatGPT Web — Mermaid na I e Markmap Tree + Cards na A

## Microfase A — Visualização do Todo e das Partes (v2.4.0)

Quando a análise identificar decomposição hierárquica fiel (`todo → partes → subpartes`), **priorizar Markmap com `layout: tree` e `theme: cards`** (leitura esquerda→direita com cartões) **efetivamente renderizado e visível** na sessão, caso a interface/ferramenta ativa disponibilize renderização Markmap.

1. **Sem suposição de suporte nativo:** o ChatGPT Web suporta prévia de Mermaid e execução de código/arquivos conforme a conta, mas **não possui garantia universal de renderização nativa de Markmap**; nunca declarar suporte nativo sem observação real.
2. **Fallback visual equivalente:** se Markmap não renderizar visualmente na sessão, produzir **e exibir** árvore gráfica equivalente esquerda→direita (ex.: `SVG`/`PNG` renderizado na conversa ou diagrama equivalente em prévia aberta), identificando-a como **representação visual equivalente** (não Markmap nativo). **Não enviar dados privados a renderizadores externos sem autorização.**
3. **Reprovação de texto isolado:** bloco Markdown/YAML, snippet Markmap, lista ou arquivo `.svg`/`.png` criado sem prévia visível **não** satisfaz a entrega visual.
4. **Fallback textual honesto:** se nem Markmap nem imagem equivalente puderem ser exibidos, entregar decomposição textual explícita com **`ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO`** e a limitação observada. Sem app interativo nem instalação extra por padrão.

## Microfase I — Mermaid como caminho padrão da microfase I

Na microfase **Diagramação do Fluxo de Aplicação**, fase I — Integração, **preferir Mermaid renderizado e com prévia visual verificada** para fluxos reais, **mesmo sem pedido explícito**. Preservar A/X/I, leitura integral progressiva e fontes ABNT. O usuário escolheu Mermaid como padrão do ChatGPT.

1. Preparar apenas nós, conexões e decisões verificadas e escrever Mermaid sintaticamente correto.
2. **Acionar o recurso de Prévia** quando disponível na interface. O código `flowchart TD` ou `graph TD` **sem desenho visível não é entrega visual**. O próprio ChatGPT pode exibir uma prévia compatível; conferir que ela foi criada.
3. Se a prévia Mermaid não puder ser acionada, tentar **um mecanismo gráfico realmente habilitado** (SVG/HTML ou arquivo gráfico verdadeiro) sem prometer o que não existe.
4. Validar fidelidade, legibilidade e privacidade; diferenciar um Mermaid realmente renderizado de diagrama equivalente gerado por outro motor.
5. Não exigir PNG/SVG/PDF ou download adicional se a figura já está visível. Não criar três alternativas em paralelo sem necessidade.

**Resultado:** imagem do fluxograma Mermaid **efetivamente visível no chat ou em prévia aberta** é obrigatória quando houver fluxo fiel. Código Mermaid isolado, HTML em texto ou arquivo sem prévia = **entrega parcial**, não conclusão. Se a prévia Mermaid não funcionar, gerar imagem verdadeira por outro mecanismo acessível. Não fabricar gráficos para objetos sem fluxo.

OPENAI. *Como trabalhar com blocos de escrita e blocos de código no ChatGPT*. [s.d.]. Disponível em: https://help.openai.com/pt-br/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt. Acesso em: 11 nov. 2026.

