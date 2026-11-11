# Seis ambientes — microfase I: rotas próprias de renderização

Escopo: exclusivamente **Diagramação do Fluxo de Aplicação**, sob a fase **I — Integração** e o nível de Gestão e Coordenação. Identificar fluxo e tentar gráfico **mesmo sem pedido explícito**. A IA aplica obrigatoriamente a **rota prioritária de cada plataforma** quando a capacidade está efetivamente acessível, com fallback honesto. Ver `references/CLAUDE-DIAGRAMAS.md`, `references/GROK-DIAGRAMAS.md`, `references/CHATGPT-DIAGRAMAS.md` e `references/GEMINI-DIAGRAMAS.md`; executar só a rota apropriada, não só código.

| Ambiente | Exemplos não obrigatórios de mecanismos |
|---|---|
| Claude Web | **Visual personalizado HTML/SVG inline; Artifact com prévia como fallback** |
| Grok Web | **SVG real em cartão de prévia inline; HTML Preview em Projects como fallback** |
| Codex CLI | Visualização terminal, arquivo gráfico local ou prévia habilitada |
| Claude Code | HTML/SVG local, visualizador da IDE, Mermaid já instalado |
| Antigravity IDE/CLI | Prévia de artefato, Mermaid, SVG ou PNG local |
| Grok Build CLI | Mermaid visível, visual interativo ou renderer nativo |

**Regra universal:** se houver fluxo fiel, **a imagem do diagrama é obrigatória na entrega visual**: inline ou prévia realmente aberta. Arquivo gráfico apenas criado sem exibição, tabela, ASCII, código Mermaid/HTML isolado ou app desnecessário não satisfazem; declarar parcial quando falhar. Quando o terminal/IDE não puder exibir a imagem, registrar a limitação e abrir prévia via mecanismo autorizado, sem simular sucesso.

**Regra:** a rota preferida é vinculante como primeira opção quando habilitada, não é licença para inventar capacidade; alternativa real só após falha concreta. Nenhum nome de ferramenta garante suporte. Preferir visual real, fiel e econômico; apenas código/texto é entrega parcial. Não inventar arquivos, recursos, links ou status. Verificar acesso à prévia antes de alegar sucesso. Preservar privacidade e registrar custo observável. Qualquer solução futura equivalente pode ser usada.

**Validação:** duas solicitações, uma de fluxo e uma numérica, em cada frontend real. Testes estruturais não certificam renderização.

