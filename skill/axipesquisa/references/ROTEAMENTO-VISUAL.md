# Fase I — roteamento visual por capacidades (AXI v2.3.1)

**Âmbito:** instrução funcional adaptativa; não instala nem ativa renderizadores. Aplicar antes de construir diagramas ou gráficos, sem pesquisas pagas para descobrir ferramentas. Resultado sempre condicionado às capacidades reais da sessão.

## Pré-verificação de custo mínimo (sem chamadas externas)

1. **Necessidade:** aplicar a Diagramação do Fluxo de Aplicação. Se houver fluxo identificável e representável com fidelidade, desenhar mesmo sem pedido explícito. Para outros visuais, considerar o pedido e a utilidade. Sinalizar lacunas pertinentes e preservar relações estáticas sem inventar sequência.
2. **Tipo:** fluxo, árvore, sequência ou arquitetura = diagrama; valores e séries numéricas = gráfico quantitativo; exploração com controles solicitada = interativo. Não inventar dados, estados nem conexões.
3. **Capacidades atuais:** conferir somente ferramentas, recursos ou prévias que a própria sessão realmente apresenta. Nome da plataforma, marketing, documentação ou modelo não comprovam disponibilidade nesta conta. Não executar sucessivas pesquisas, instalar extensões, abrir sites ou sondar provedores externos só para escolher um renderer.
4. **Restrições:** verificar se há dados sensíveis, preferência por formato, acessibilidade, necessidade real de SVG/PNG e permissão para arquivos, execução local e rede.
5. **Escolha:** selecionar a solução disponível que cumpra a entrega com menos ferramentas, conversões, chamadas de modelo, tráfego, passos humanos e código desnecessário. Sem medições comparativas, custo/eficiência são critérios heurísticos, não percentuais comprovados.

## Tabela de decisão

| Conteúdo e capacidade efetiva | Primeira opção | Alternativa de menor dependência |
|---|---|---|
| Sem necessidade visual | Texto breve | Nenhuma imagem |
| Relações/fluxo + prévia Mermaid | Mermaid nativo | SVG local verificável |
| Dados numéricos + gráfico integrado | Gráfico nativo / Vega-Lite se suportado | SVG estático ou tabela fiel |
| Diagrama + SVG inline/arquivo suportado | SVG local autossuficiente | HTML/SVG em Canvas/Artifact, se habilitado |
| Exploração interativa realmente pedida | Visual interativo nativo | HTML/Canvas autossuficiente se disponível |
| Nenhuma prévia ou arquivo possível | Código Mermaid ou SVG com limite declarado | Instrução manual curta; saída parcial |

**Ordem de decisão:** cumprir o requisito visual e a fidelidade primeiro; entre alternativas capazes, preferir a de menor custo incremental. Um renderer Mermaid não tem preferência absoluta sobre um gráfico numérico integrado. Não transformar gráfico em imagem generativa se houver renderer semântico adequado.

## Limite de trabalho e entregável

- Padrão: **um único visual principal**, com legenda textual e descrição acessível. Criar múltiplos apenas se representarem relações ou conjuntos de dados distintos e necessários, ou se o usuário pedir explicitamente.
- Realizar **uma tentativa no recurso de maior adequação comprovada**; se indisponível ou falhar, escolher **uma alternativa compatível**. Não repetir tentativas às cegas nem adicionar camadas de complexidade para uma tarefa simples.
- Só criar PNG, SVG, HTML ou `.mmd` adicionais quando pedidos ou indispensáveis para visualização/portabilidade. Se SVG e PNG forem expressamente exigidos, entregar arquivos existentes e verificáveis ou reportar o impedimento.
- Anotar sem ambiguidade `visual exibido`, `código produzido`, `SVG baixável`, `PNG baixável` e `precisa ação do usuário`. Código com syntax highlighting não comprova prévia gráfica.
- SVG reconstruído a partir das relações é **representação visual equivalente**, não renderização nativa Mermaid. Priorizar grafos fiéis, sem estados fabricados e com rótulos acessíveis.
- **Privacidade:** não enviar dados privados a CDN, API de terceiros ou renderizador externo sem autorização. Não instalar plugin/pacote ou usar rede apenas para um desenho se houver saída local.
- Se a sessão não expuser ferramentas nem meio de exibição, não inventar detecção: declarar `capacidade de prévia não verificada` e oferecer a fonte fiel como entrega parcial.

## Encaminhamento específico

- Gemini Web: `references/GEMINI-DIAGRAMAS.md` (primeiro nesta evolução).
- ChatGPT: `references/CHATGPT-DIAGRAMAS.md` (segunda etapa).
- Claude Web, Grok Web, Codex CLI, Claude Code, Antigravity e Grok Build: `references/PLATAFORMAS-VISUAIS.md` (terceira etapa).

**Avaliação:** testes automáticos apenas verificam texto, rotas e pacotes; testes nas interfaces reais devem registrar renderer exibido, formato, número de chamadas, tempo, passos, possibilidade de exportar e fidelidade. Sem essas medições não alegar maior eficiência ou menor custo monetário.
