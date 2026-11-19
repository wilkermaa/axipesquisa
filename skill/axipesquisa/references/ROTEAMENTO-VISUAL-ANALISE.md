# Roteamento visual da Análise — AXI Pesquisa v2.4.0 (candidata)

**Microfase da A, independente da Diagramação do Fluxo de Aplicação da I.** Quando a análise identificar uma decomposição hierárquica fiel e relevante, entregar mapa visual do todo às partes.

## Execução e aceite
1. Delimitar o todo, contexto, fronteiras, componentes e subpartes; diferenciar fatos, hipóteses e relações transversais.
2. Priorizar **Markmap** com `layout: tree` e `theme: cards`: raiz à esquerda, crescimento à direita, cartões arredondados. São opções oficialmente documentadas, não comprovação de que toda plataforma suporte Markmap nativo.
3. **Acionar concretamente a renderização e apresentar a figura no chat ou em prévia realmente aberta**. Markdown/YAML/SVG/HTML somente como código, tabela e arquivo gráfico não visualizado não atendem à entrega.
4. Se Markmap estiver indisponível, **produzir e exibir** SVG/PNG ou árvore equivalente em recurso acessível, preservando nós, ordem e ligações. Identificar corretamente o desenho como equivalente.
5. Se não houver qualquer imagem/prévia viável após tentativa principal e uma alternativa real, **apresentar texto estruturado**, com aviso **ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO**, explicando a limitação observada.
6. Não inventar divisões para assuntos triviais, árvore enganosa, relações de múltiplo pertencimento ou saída estritamente fechada; preservar fidelidade jurídica, científica e de fontes.
7. Não transferir dados privados para renderizadores externos sem autorização. Preferir legibilidade, acessibilidade e simplicidade; texto complementar é válido, mas não substitui a imagem quando obrigatória.

## Oráculo
| Saída | Estado |
|---|---|
| Markmap Tree + Cards efetivamente visível e fiel | CONFORME |
| Imagem equivalente exibida, Markmap inacessível | CONFORME COM FALLBACK |
| Somente código/tabela/ASCII/arquivo sem prévia | NÃO CONFORME |
| Texto após ausência real de meios visuais, com aviso | ENTREGA PARCIAL |
| Árvore com partes/filiações inventadas | NÃO CONFORME |

**Fase X:** analogias úteis com limites, sem imagens compulsórias.

**Fase I:** preservar `references/ROTEAMENTO-VISUAL.md` e Mermaid para fluxos funcionais reais. O mapa da A **não substitui** a I.

## Fontes
MARKMAP. *Themes and layouts*. [s.d.]. Disponível em: https://markmap.js.org/docs/guide/themes-and-layouts. Acesso em: 19 nov. 2026.

MARKMAP. *Options*. [s.d.]. Disponível em: https://markmap.js.org/docs/guide/options. Acesso em: 19 nov. 2026.

MERMAID. *About Mermaid*. [s.d.]. Disponível em: https://mermaid.js.org/intro/. Acesso em: 19 nov. 2026.
