# AXI Pesquisa v2.4.0 — contrato visual da Análise e Integração

> **Estado:** especificação técnica da issue [#16](https://github.com/wilkermaa/axipesquisa/issues/16); não equivale a uma release nem a prova de execução gráfica.
>
> **Baseline:** tag aprovada [v2.3.8](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.8); manter o protocolo científico C0/C1/C2 congelado na v2.2.0-rc2 e as tags históricas inalteradas.
>
> **Decisão autoral registrada:** Markmap `layout: tree` + `theme: cards` **obrigatório e prioritário na fase A quando o objeto justificar decomposição hierárquica**; manter Mermaid como rota preferencial de diagramas funcionais da fase I.

## A — Análise: regras acionáveis

1. **Identificar o todo:** nomear objeto, contexto, objetivo, limites e desconhecidos, sem inventar divisão.
2. **Identificar as partes:** decompor em componentes relevantes e, quando necessário, subpartes; função e relações não hierárquicas podem ser explicadas fora da árvore.
3. **Gatilho positivo:** havendo hierarquia fiel (todo → partes → subpartes), **renderizar e apresentar visualmente** uma árvore da esquerda para a direita com cartões, preferindo **Markmap** no padrão `tree` + `cards`.
4. **Resultado indispensável:** a árvore **desenhada e visível na resposta ou em prévia realmente aberta**, legível, com os componentes corretos. Código Markdown/YAML, snippet Markmap, descrição ASCII, tabela ou arquivo oculto **não são representação visual entregue**.
5. **Fallback visual:** quando Markmap não estiver de fato disponível, tentar **uma alternativa visual equivalente** acessível (ex.: SVG/PNG desenhado e pré-visualizado), preservando os mesmos nós/arestas e a leitura esquerda→direita. Identificar como **equivalente**, não como renderização nativa do Markmap.
6. **Fallback final textual:** se nem Markmap nem imagem/previsão visual puderem ser exibidos, entregar uma **decomposição textual explícita** com todo e partes, declarando **ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO** e a limitação observada. Não fingir imagem ou execução de ferramenta.
7. **Gatilho negativo:** não produzir árvore por obrigação ritual em pergunta trivial, objeto sem decomposição coerente, gráfico que induza erro ou formato fechado proibitivo. Justificar a exceção quando pertinente.
8. **Cruzamentos e múltiplos pertencimentos:** árvores mostram uma perspectiva classificatória, não todas as interações. Não duplicar componentes como se fossem partes mutuamente exclusivas, nem converter um sistema em árvore se relações transversais forem essenciais.
9. **Segurança:** não enviar dados sigilosos à ferramenta gráfica externa sem base/autorização, privilegiando recursos locais e mínimos. As afirmações dos nós e seus limites precisam ser sustentados pelas fontes quando aplicável.
10. **Acessibilidade:** rótulos legíveis e curtos, ordem esquerda→direita, contraste adequado, alternativa textual útil inclusive para leitor de tela e nomenclatura consistente.

## X — eXpansão

Usar analogias/comparações quando esclarecedoras, com correspondências e limites explícitos. **Sem imposição de segundo gráfico**. A fase X não herda automaticamente as obrigações visuais de A ou I.

## I — Integração: preservar v2.3.8

- Reconstruir relações, dependências, condições, interações e funcionamento a partir dos elementos validados.
- Se existir fluxo real fielmente representável, conservar a **microfase obrigatória de diagramação da I**, preferindo **Mermaid efetivamente renderizado** onde a plataforma o suporte (especialmente ChatGPT), ou visual funcional equivalente.
- **Mermaid na I não substitui Markmap da A**. Não apresentar só `flowchart` ou SVG/HTML em código como se fossem imagens.
- Fluxo inexistente não impõe fluxograma artificial. Saídas com formato estrito prevalecem.
- Requisitos de fontes oficiais, ABNT, segurança, proveniência e fidelidade científica/jurídica da v2.3.8 permanecem inalterados.

## Matriz de cenários de aceite

| ID | Entrada | Fase | Oráculo de resultado |
|---|---|---|---|
| A01 | Escola → Gestão/Ensino/Infraestrutura/Comunidade | A | árvore Tree + Cards Markmap **realmente exibida**; nomes e vínculos corretos |
| A02 | A01 com Markmap inacessível, SVG local disponível | A | SVG/PNG equivalente **visivelmente exibido**, identificado como fallback |
| A03 | A01 sem quaisquer meios visuais funcionais | A | decomposição textual + aviso de **ENTREGA PARCIAL** |
| A04 | A01 entregue só como bloco Markdown/YAML | A | **não conforme**, mesmo se a sintaxe Markmap for válida |
| A05 | Questão direta sem hierarquia útil | A | sem mapa obrigatório; resposta proporcional |
| A06 | Objeto com múltiplos pais/arestas cruzadas essenciais | A | delimitação da perspectiva ou não usar árvore enganosa |
| A07 | Tarefa com informações sigilosas e renderer remoto | A | não transmitir dados sem autorização; usar meio local ou fallback |
| A08 | Diagrama exibido mas partes incorretas/inventadas | A | não conforme: imagem elegante não compensa erro |
| I01 | Processo verdadeiro com decisão e feedback | I | Mermaid/diagrama equivalente com nós e setas **renderizados** |
| I02 | Processo entregue somente em código Mermaid | I | não conforme, reportar falha e tentar alternativa |
| I03 | Objeto estático sem processo válido | I | não inventar fluxo |
| X01 | Analogia com diferenças importantes | X | correspondências, diferenças e limites, sem obrigar imagem |
| F01 | Saída fechada (JSON exigido) | Todas | respeitar formato e não injetar imagem/referências extras indevidas |

## Critérios verificáveis / limite do aceite

- **Correção estrutural:** conferir todos os nós e arestas do mapa contra a análise; não inferir relações sem evidência.
- **Renderização visível:** exigir evidência concreta da imagem/prévia; arquivo gerado não equivale a visualização exibida.
- **Compatibilidade:** instruções podem orientar uso de Markmap, mas **não comprovam** a capacidade de cada IA chamá-lo nativamente.
- **Economia:** uma tentativa principal e uma alternativa viável são suficientes; sem instalações compulsórias ou app interativo não solicitado.
- **Versão:** a v2.4.0 é funcionalidade **MINOR candidata** com a v2.3.8 como baseline; não há tag, homologação, ZIP instalado ou validação científica por este documento.

## Evidências e fontes

- AXI Pesquisa: [SKILL da tag v2.3.8](https://github.com/wilkermaa/axipesquisa/blob/v2.3.8/skill/axipesquisa/SKILL.md), [POLITICA-ORGANIZACIONAL.md](https://github.com/wilkermaa/axipesquisa/blob/v2.3.8/POLITICA-ORGANIZACIONAL.md).
- MARKMAP. *Themes and layouts*. [s.d.]. Disponível em: https://markmap.js.org/docs/guide/themes-and-layouts. Acesso em: 19 nov. 2026.
- MARKMAP. *Options*. [s.d.]. Disponível em: https://markmap.js.org/docs/guide/options. Acesso em: 19 nov. 2026.
- MERMAID. *About Mermaid*. [s.d.]. Disponível em: https://mermaid.js.org/intro/. Acesso em: 19 nov. 2026.
- PEC-001: https://github.com/wilkermaa/politica-de-execucao-continua/blob/main/politica/PEC-001-POLITICA-EXECUCAO-CONTINUA-v1.0.0.md.
- Política de issues: https://github.com/wilkermaa/politica-issues.

**Próxima disciplina:** DESENVOLVIMENTO conforme #17; testes e QA independentes têm issues próprias. Sem evidências reais, não relatar a fase como homologada.

◌ SOPRO GPDO AXI
