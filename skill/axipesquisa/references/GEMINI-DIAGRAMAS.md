# Gemini Web — guia não vinculante da microfase I

**Âmbito:** somente a microfase **Diagramação do Fluxo de Aplicação**, dentro da **Integração**, no nível de Gestão e Coordenação. Acionar **mesmo sem pedido explícito** quando houver fluxo fiel.

**Escolha livre pela IA executora:** verificar recursos já disponíveis na conversa e optar pelo mecanismo que realmente exiba o gráfico. Mermaid, SVG, visualização nativa, HTML com prévia, PNG ou outros são possibilidades, **não uma ordem fixa nem tecnologia obrigatória**. O modo de maior esforço e a documentação do produto não comprovam acesso a renderizador.

**Fidelidade:** mostrar nós e decisões; não inventar passos. Gráfico quantitativo deve preservar valores, escala e unidades. Entre alternativas aptas, escolher a que minimize tokens, dependências, conversões e passos; não usar Deep Research só para desenhar.

**Canvas:** não afirmar que uma Skill pode abrir Canvas dentro da mesma sessão sem recurso disponível. Se necessário, orientar **Adicionar arquivos (+) → Canvas** em conversa separada, mas não registrar essa alternativa manual como gráfico já entregue. O modelo de HTML/SVG (`assets/GEMINI-CANVAS-TEMPLATE.md`) é opcional, não default. PNG via Canvas 2D é exemplo de exportação, não obrigação.

**Entrega verificável:** visual na interface, preview efetivo ou arquivo SVG vetorial autossuficiente / PNG real. Somente texto ou código não é gráfico. Sem capacidade efetiva, descrever a limitação e marcar **entrega parcial**; não afirmar que Canvas foi aberto, nem gerar links fictícios. **Sem fetch/CDN externos** com dados privados.

## Homologação real

Verificar fluxo sem pedido de gráfico, pedido explícito de gráfico e tentativa de arquivo SVG real; caso Canvas só funcione fora da Skill, registrar separadamente. Nenhuma dessas provas é substituída por teste estático.

GOOGLE. *Manage your tasks & workflows in Gemini Apps*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/17094507?co=GENIE.Platform%3DDesktop&hl=en. Acesso em: 11 nov. 2026.
GOOGLE. *Create docs, apps & more with Canvas*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/16047321?hl=en. Acesso em: 11 nov. 2026.

