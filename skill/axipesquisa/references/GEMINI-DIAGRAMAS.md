# Gemini Web — escolha econômica de diagramas e gráficos na Integração

Aplicar depois de `references/ROTEAMENTO-VISUAL.md`. O suporte documentado do produto não prova disponibilidade em qualquer conta. O primeiro passo é **reconhecimento leve dos recursos realmente visíveis na sessão**, sem fazer chamadas pagas ou pesquisas para sondar capacidades.

## Prioridade adaptativa Gemini (fase I)

1. **Sem necessidade visual:** resposta textual. Se o usuário não pedir gráfico e o texto resolver, não criar diagrama.
2. **Gráfico quantitativo:** utilizar visualização/gráfico integrado do Gemini **somente quando a sessão realmente oferecer**; não usar Deep Research exclusivamente para renderizar um gráfico. Preservar eixos, unidades, escalas e fonte dos números.
3. **Fluxo ou relações:** se houver visualizador Mermaid verificável nesta sessão, usar a prévia nativa. Não presumir que um bloco `mermaid` será renderizado só por ter sintaxe válida.
4. **Sem prévia Mermaid:** se a tarefa aceitar arquivo `.svg`, construir um **SVG vetorial autossuficiente** fiel aos nós, arestas e condições. Preferir SVG simples a imagem generativa ou múltiplos serviços externos; abrir a prévia quando possível e verificar o arquivo.
5. **Sem arquivo gráfico direto, mas com Canvas:** usar HTML mínimo com `<svg>` inline e prévia do Canvas; inserir botões locais para SVG e, **quando solicitado**, PNG via Canvas 2D. Empregar `assets/GEMINI-CANVAS-TEMPLATE.md` apenas quando necessário; não produzir um aplicativo complexo para um fluxograma simples.
6. **Canvas não aberto:** caso seja realmente necessária ação manual, orientar **Adicionar arquivos (+) → Canvas** com HTML/SVG pronto. Se a sessão não oferecer nenhum visualizador, fornecer fonte SVG/Mermaid com limitação explicada; código sozinho não completa pedido de visual.

## Restrições e critérios de entrega

- **Não use `fetch` externo** nem CDN para renderizar dados confidenciais. Não transmitir dados privados sem autorização.
- Limite padrão a um gráfico útil; múltiplos apenas por necessidade distinta ou solicitação explícita.
- Não afirmar que qualquer capacidade existe **sem evidência específica**; documentação e exemplo são **não execução comprovada**.
- Se SVG ou PNG solicitado, afirmar sucesso apenas com arquivo real e link verificável. Identificar separadamente prévia, arquivo SVG, arquivo PNG e fonte Mermaid.
- Preservar nós, arestas, rótulos e decisões; sem fabricação de status. Dados sem confirmação permanecem `a validar`.
- Recriar SVG com outras técnicas é representação visual equivalente, não compilação Mermaid.

## Teste manual obrigatório para homologação

Prompt: “Mostre Entrada → Validação → Decisão → Sucesso ou Correção em um diagrama visível; se possível, exporte SVG e PNG.” Registrar renderer selecionado, gráfico realmente visto, exportações disponíveis, passos adicionais e qualquer falha. Repetir com um conjunto de valores numéricos e pedido de gráfico de barras. **Sem resultado de uso real, não chamar a integração de homologada.**

## Documentação oficial consultada em 11 nov. 2026

GOOGLE. *Manage your tasks & workflows in Gemini Apps*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/17094507?co=GENIE.Platform%3DDesktop&hl=en. Acesso em: 11 nov. 2026.

GOOGLE. *Turn sketches into apps with Gemini*. 2026. Disponível em: https://blog.google/innovation-and-ai/products/gemini-app/turn-drawings-into-apps-gemini/. Acesso em: 11 nov. 2026.

GOOGLE. *Use Deep Research in Gemini Apps*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/15719111?hl=en. Acesso em: 11 nov. 2026.
