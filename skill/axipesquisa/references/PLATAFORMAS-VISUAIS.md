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

## Matriz v2.4.0 — oito plataformas para Fase A (Markmap Tree + Cards) e Fase I (Mermaid/Fluxo)

A matriz abaixo resume as rotas das **oito plataformas**, sem presumir que Markmap seja nativo em todas, sem exigir app interativo ou instalação adicional por padrão, e proibindo envio de dados privados a serviços públicos não autorizados.

| Plataforma | Fase A — Rota prioritária e fallback visual | Fase I — Rota preservada (fluxos reais) | Fallback textual e verificação |
|---|---|---|---|
| **ChatGPT Web** | Markmap `tree`+`cards` se renderizado em prévia; fallback **equivalente** via SVG/PNG/Mermaid em prévia | Mermaid renderizado em prévia | Conferir imagem/prévia aberta; arquivo ou código sem prévia = `ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO` |
| **Gemini Web** | Markmap se habilitado; fallback prioritário: **geração direta de imagem** (SVG renderizado/PNG) esquerda→direita | Geração direta de imagem SVG/PNG; Canvas só fallback estático se abrir figura | Sem app HTML por padrão; conferir figura exibida na conversa; falha = `ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO` |
| **Claude Web** | Markmap se habilitado; fallback **visual personalizado HTML/SVG inline** ou **Artifact** com prévia | Visual personalizado HTML/SVG inline; Artifact com prévia | Conferir figura visível no chat/Artifact; snippet isolado não aceito; falha = `ENTREGA PARCIAL` |
| **Grok Web** | Markmap se habilitado; fallback **cartão SVG com prévia inline** ou **HTML Preview em Projects** | Cartão SVG com prévia inline; Projects HTML Preview | Conferir cartão/prévia aberta; XML isolado não aceito; falha = `ENTREGA PARCIAL` |
| **Codex CLI** | Markmap/prévia se IDE suportar; fallback **SVG/PNG local** gerado e exibido em visualizador autorizado | Visualização terminal, arquivo gráfico local com prévia | Distinguir arquivo criado em disco de imagem efetivamente aberta/exibida; terminal puro = `ENTREGA PARCIAL` |
| **Claude Code** | Markmap/SVG/HTML estático local em **visualizador da IDE** com prévia aberta | HTML/SVG local, visualizador da IDE, Mermaid local | Não entregar apenas código-fonte; se sem preview aberto, registrar `ENTREGA PARCIAL` |
| **Antigravity IDE/CLI** | Markmap se suportado; fallback **PNG/SVG/artefato local** gerado e inspecionado/exibido inline na IDE | Prévia de artefato, Mermaid, SVG ou PNG local exibido | Em sessão com visualização inline (ex.: `read_file`/prévia), conferir imagem; sem exibição = `ENTREGA PARCIAL` |
| **Grok Build CLI** | Markmap/renderer local se disponível; fallback SVG/PNG local em prévia da IDE/terminal gráfico | Mermaid visível ou renderer gráfico local | Sem renderer gráfico ativo, não simular figura; registrar `ENTREGA PARCIAL` |

**Regra de privacidade e exportação:** nunca enviar dados sigilosos a servidores públicos de renderização (ex.: APIs externas de diagramas) sem autorização expressa; priorizar renderização local ou nativa da sessão. Exportação para SVG/PNG ou PDF é opcional quando a figura já está visível, salvo pedido explícito do usuário.

