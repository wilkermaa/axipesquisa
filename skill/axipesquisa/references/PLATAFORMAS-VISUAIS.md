# Lote de seis ambientes — roteamento visual da fase I

Consultar `references/ROTEAMENTO-VISUAL.md` antes da tabela. A presença do nome da plataforma **não** é prova de que a prévia está habilitada. Distinguir chat Web, CLI, terminal e IDE.

| Ambiente | Primeiro caminho quando comprovadamente disponível | Alternativa de menor dependência |
|---|---|---|
| **Claude Web** | Visualização nativa ou artefato Mermaid para fluxos; gráfico integrado para dados | Artifact HTML/SVG, sem bibliotecas externas por padrão |
| **Grok Web** | SVG exibível no chat para gráfico simples; prévia Mermaid em Projects se realmente disponível | Código SVG fiel + instrução curta, reconhecendo saída parcial |
| **Codex CLI** | Mermaid no terminal compatível para relações; renderizador textual/terminal para casos simples | Arquivo SVG local verificável, se ferramentas de arquivo estiverem habilitadas |
| **Claude Code** | SVG/HTML gerado e aberto em visualizador local disponível | Mermaid com plugin **já instalado**; não instalar dependências sem autorização |
| **Antigravity IDE/CLI** | Mermaid no visualizador de artefatos ou CLI compatível | SVG local ou resumo textual fiel se a prévia falhar |
| **Grok Build CLI** | Mermaid integrado para diagramas; gráfico interativo somente se realmente necessário e suportado | SVG local, evitando dependência de rede |

## Regras comuns do lote

1. Verificar na própria sessão se o visualizador existe; não usar uma capacidade da CLI como prova de suporte no chat Web.
2. O visual deve corresponder ao pedido: Mermaid para relações, visual numérico para séries/valores, HTML interativo apenas para exploração.
3. Escolher **uma** saída principal de baixo custo; evitar múltiplas tentativas, instalações, serviços de terceiros e renderizadores remotos não autorizados.
4. Preservar rótulos, conexões e decisões; cores de status somente com evidência e sempre acompanhadas de texto.
5. Se SVG/PNG forem pedidos, entregar arquivos reais quando possível, senão declarar a limitação precisa; não prometer links ou renderização imaginários.
6. Para homologar, executar pelo menos um teste de fluxo e um quantitativo em cada produto real; registrar disponibilidade, custos observáveis (passos/chamadas), sucesso da prévia e exportação.

**A documentação do fabricante é indício de suporte, não certificação do instalador AXI.**
