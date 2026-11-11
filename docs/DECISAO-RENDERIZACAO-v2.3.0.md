# AXI-Pesquisa v2.3.0 — decisão de renderização econômica da fase I

**Data:** 11 nov. 2026. **Escopo:** nova funcionalidade compatível (MINOR). **Ordem de implementação:** 1. Gemini Web; 2. ChatGPT Web; 3. Claude Web, Grok Web, Codex CLI, Claude Code, Antigravity e Grok Build.

## Problema

O histórico priorizava Mermaid e fallback Canvas/SVG. Em certas interfaces Mermaid não aparece como prévia, enquanto um gráfico nativo ou um SVG local pode resolver a tarefa com menos passos. O novo contrato **não adivinha capacidades**, apenas orienta agentes a observar o que já está habilitado.

## Contrato testável

- Classificar pedido: nenhum visual, diagrama de relações, dados quantitativos ou interativo necessário.
- Inspecionar recursos da sessão sem chamadas externas, testes de rede, instalações, Deep Research ou API cobrada para descobrir capacidades.
- Ordenar opções pelo requisito e pela adequação semântica; entre opções viáveis minimizar passos, chamadas, dependências e arquivos.
- Preferir um visual útil; múltiplos somente quando distintos e necessários ou explicitamente pedidos.
- Escolher uma tentativa principal + no máximo uma alternativa adequada antes de relatar limitação.
- Guardar fidelidade, privacidade, acessibilidade e diferença entre código, prévia e arquivo baixável.
- Não declarar ganho de latência, tokens ou dinheiro antes de medir nas interfaces reais.

## Matriz por produto

| Plataforma | Caminho preferido se habilitado | Fallback |
|---|---|---|
| Gemini Web | Visualização nativa para números; Mermaid se prévia comprovada | SVG local, Canvas HTML/SVG |
| ChatGPT | Mermaid para fluxos; Vega-Lite ou gráfico nativo para números | SVG local / HTML se necessário |
| Claude Web | Visual nativo ou artefato Mermaid | Artifact HTML/SVG |
| Grok Web | SVG no chat; Mermaid em Projects quando acessível | SVG como fonte com limitação |
| Codex CLI | Mermaid no terminal compatível | SVG local |
| Claude Code | SVG/HTML em visualizador local | Mermaid com extensão já disponível |
| Antigravity | Mermaid em artefatos/CLI suportada | SVG local |
| Grok Build | Mermaid integrado para fluxos | SVG local / interativo somente se útil |

## Medidas para homologação

Em cada IA, dois prompts controlados: (1) Entrada → Validação → Decisão → Sucesso/Correção com visual visível; (2) barras para A=3, B=5, C=2 com eixos e valores. Registrar data, versão, plano, nome de renderer, ferramenta invocada, chamadas observáveis, intervenções manuais, latência observada, visual realmente exibido, downloads quando solicitados e eventuais falhas. O protocolo empírico C0/C1/C2 **v2.2.0-rc2 permanece congelado**. Estes são testes de produto separados.

## Fontes oficiais (consulta em 11/11/2026)

OPENAI. *Working with writing blocks and code blocks in ChatGPT*. [s.d.]. Disponível em: https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt. Acesso em: 11 nov. 2026.

OPENAI. *Using Codex with your ChatGPT plan*. [s.d.]. Disponível em: https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan. Acesso em: 11 nov. 2026.

GOOGLE. *Manage your tasks & workflows in Gemini Apps*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/17094507?co=GENIE.Platform%3DDesktop&hl=en. Acesso em: 11 nov. 2026.

GOOGLE. *Turn sketches into apps with Gemini*. 2026. Disponível em: https://blog.google/innovation-and-ai/products/gemini-app/turn-drawings-into-apps-gemini/. Acesso em: 11 nov. 2026.

GOOGLE. *Use Deep Research in Gemini Apps*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/15719111?hl=en. Acesso em: 11 nov. 2026.
