# AXI-Pesquisa v2.2.2

**Escopo:** correção de desenho de diagramas no Gemini Web sem renderer Mermaid nativo.

- Prioriza SVG vetorial equivalente quando não existir prévia Mermaid.
- Prioriza prévia Gemini Canvas de HTML autocontido com SVG inline, caso a ferramenta esteja disponível.
- Propõe exportação real para SVG/PNG pelo navegador quando suportada, sem inventar arquivos.
- Preserva política editorial da v2.2.1, sem alterar o método AXI ou os cenários do experimento científico já congelado.
- Testes locais estáticos não comprovam funcionamento na interface real do Gemini Web.
