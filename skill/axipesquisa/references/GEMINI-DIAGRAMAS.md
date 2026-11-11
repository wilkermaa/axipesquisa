# Gemini Web — execução visual obrigatória na microfase I (v2.3.4)

**Escopo:** somente a microfase **Diagramação do Fluxo de Aplicação**, parte da fase **I — Integração**, nível Gestão e Coordenação. Em um fluxo fielmente representável, **tentar entregar gráfico visível mesmo sem pedido explícito**. A regra central também está no `SKILL.md`, independentemente de o modelo consultar este guia.

## Procedimento obrigatório de execução no Gemini

1. **Identifique o fluxo e prepare a estrutura:** nós, rótulos, setas, bifurcações e lacunas confirmados. Não inventar etapas, condições, datas, autoridades nem base jurídica.
2. **Selecione e ACIONE a visualização na sessão corrente:** preferir **SVG efetivamente renderizado na própria tela ou em prévia gráfica** quando o Gemini disponibilizar esse recurso. Se SVG não for renderizável/exibível, usar **PNG ou visualização nativa** realmente acessível. Formatos são meios, não fins; a IA **decide livremente** qual recurso realmente utilizável produz a figura; a escolha tecnológica permanece da IA executora. Não recorrer a Mermaid.js embarcado se a Skill não puder executar JavaScript.
3. **Produza a figura, não somente a fonte:** não finalizar emitindo `graph TD`, `flowchart TD`, XML `<svg>`, código Mermaid, HTML ou um bloco **“Snippet de código”** como se isso fosse desenho. **Gerar um arquivo SVG não equivale a abrir uma prévia**; se for criado, solicitar sua exibição ou conferir que o arquivo gráfico real está acessível.
4. **Verifique antes de responder:** a figura aparece na própria interface? Há prévia visual realmente produzida? Ou há arquivo gráfico existente e acessível? Conferir nós/arestas/rótulos e marcar como concluída apenas uma **entrega visual verificável**. Não alegar que o usuário visualizou algo quando apenas a prévia/arquivo foi criado.
5. **Recupere em caso de somente código:** se a saída for snippet Mermaid/SVG/HTML, tentar **uma alternativa gráfica viável** na mesma sessão. Se falhar, informar **entrega parcial** e o impedimento observado; **Não inventar prévias**, não anunciar sucesso, não gerar link inexistente e não solicitar ferramentas ou serviços externos não autorizados.
6. **Não obrigar PDF nem download:** **PDF não é obrigatório**; gráfico visível no chat ou prévia gráfica já basta. PDF de auditoria, PNG/SVG para download e exportação só se solicitados ou necessários; a existência de um PDF não integra o critério de aceite.
7. **Canvas com verificação real:** se a interface com Skill disponibilizar Canvas utilizável nesta sessão, ele pode exibir HTML/SVG. **Não presumir** interoperabilidade e **não declarar impossível** o uso do Canvas sem observar a sessão; abrir Canvas em **conversa separada** pode ser alternativa manual, **não uma entrega feita pela Skill na conversa original**.
8. **Economia e segurança:** não carregar Mermaid.js, renderizadores externos, CDNs ou HTML/JavaScript extenso por padrão; entre saídas aptas, minimizar tokens, etapas e conversões. Manter privacidade, texto legível e conexões semanticamente fiéis.

## Oráculo de aceitação Gemini

| Saída realmente observada | Classificação |
|---|---|
| SVG desenhado na interface ou prévia visual | **Aceito** para apresentação gráfica |
| PNG/gráfico nativo exibido na tela ou em prévia | **Aceito** para apresentação gráfica |
| Arquivo gráfico existente e acessível, não necessariamente aberto pelo usuário | **Aceito** como arquivo visual disponível, sem alegar que foi visto |
| `flowchart TD` em “Snippet de código”, Mermaid sem preview, XML SVG como texto | **Reprovado**: fonte, não gráfico |
| Não há visual, mas o modelo explica a limitação real | **Parcial**, não homologar diagramação |

**Caso de regressão:** `@axipesquisa procedimento para mudar a lotação do funcionario na prefeitura de matinhos`. Aplicar esta regra somente quando o modelo puder definir fluxo fiel com dados verificados; a geração de fluxograma não valida a exatidão jurídica das etapas. **O autor relatou todos os recursos disponíveis no teste**, mas a captura apresentou código e não o desenho. O diagnóstico editorial deve avaliar o acionamento do mecanismo de prévia, sem presumir ausência de ferramentas. A versão da Skill ativa na captura não foi comprovada.

**Validação:** registrar modelo, data, versão ativa da Skill, prompt, captura da resposta, recurso realmente acionado e presença de figura, sem exigir PDF. Testes estáticos e CI não demonstram renderização real no Gemini.

GOOGLE. *Sobre a transição dos Gems para habilidades*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/18560919?hl=pt-BR. Acesso em: 11 nov. 2026.
