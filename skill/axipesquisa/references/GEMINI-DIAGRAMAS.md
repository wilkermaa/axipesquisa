# Guia operacional: diagramas visuais no Gemini Web

Este guia complementa a **fase I — Integração** do AXI. Use quando o usuário pedir diagrama visual, Mermaid, SVG ou PNG no Gemini. Não transforma funcionalidades de outras IAs em ferramentas do Gemini.

## Ordem de tentativas

1. **Verifique se há visualização Mermaid** no cliente atual. Se sim, exiba o diagrama e entregue a fonte Mermaid quando útil.
2. **Se a prévia não existir, mude o meio sem mudar o modelo de relações**: SVG vetorial autossuficiente, com flechas, caixas, decisões e rótulos. Se o Gemini permitir criar arquivo na conversa/tarefa, entregue `diagrama.svg` para abrir/baixar.
3. **Se houver Gemini Canvas**, use-o para criar um arquivo `diagrama.html` com `<svg>` inline, visualização na prévia e botão de salvar SVG. Opcionalmente crie botão de salvar PNG que rasterize o SVG **localmente** no `canvas` do navegador, usando `Blob`, `URL.createObjectURL`, `Image`, `canvas.toBlob` e download com link temporário. Não use `fetch` externo nem CDNs de Mermaid por padrão.
4. **Se não for possível iniciar Canvas pela resposta**, instrua: **Gemini Web → Adicionar arquivos (+) → Canvas** e forneça o HTML autocontido para colar em novo Canvas. Essa orientação é uma ação do usuário, não execução comprovada da IA.
5. **Se a tarefa tiver recurso de criação de arquivos SVG/PNG**, use-o. Links inexistentes são proibidos. Se nada disso for possível, entregue Mermaid e SVG completos como código + indicação de que não houve renderização.

## Regras de qualidade

- O pedido de *visualização* não está satisfeito por código Mermaid sem prévia nem por um wireframe de interface.
- Fidelidade primeiro: os nós, arestas, rótulos e condições no gráfico devem corresponder aos dados fornecidos; nenhuma dependência pode ser criada por estética.
- Não identificar componentes como concluídos, bloqueados ou em atenção sem evidência específica; usar estado neutro `a validar`.
- Manter proporções e hierarquia e evitar cruzamentos, cores de estado com rótulos textuais e contraste legível.
- Não afirmar "SVG gerado", "PNG criado", "Canvas aberto" ou "prévia disponível" quando só existe texto orientativo.

## Teste de aceitação sugerido

Solicitação: **“Gere um diagrama do fluxo Entrada → Validação → Decisão → Sucesso/Correção. Quero vê-lo e receber SVG e PNG.”**

Evidências separadas: (i) Mermaid sintaticamente válido; (ii) visual na prévia ou arquivo SVG; (iii) link do SVG; (iv) link do PNG. Um teste local de estrutura não comprova que qualquer recurso visual foi executado em Gemini Web.

## Fontes oficiais

GOOGLE. *Criar documentos, apps e muito mais com o Canvas*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/16047321?hl=pt-BR. Acesso em: 10 nov. 2026.

GOOGLE. *Gerenciar tarefas e fluxos de trabalho nos apps do Gemini*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/17094507?hl=pt-BR. Acesso em: 10 nov. 2026.
