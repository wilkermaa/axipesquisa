# Gemini Web — execução visual obrigatória na microfase I (v2.3.6)

**Capacidade visual:** verificar a capacidade de renderização nesta sessão; o nome do produto não demonstra acesso efetivo a um visualizador.

**Escopo:** somente a microfase **Diagramação do Fluxo de Aplicação**, parte da fase **I — Integração**, nível Gestão e Coordenação. Em um fluxo fielmente representável, **tentar entregar gráfico visível mesmo sem pedido explícito**. A regra central também está no `SKILL.md`, independentemente de o modelo consultar este guia.

## Procedimento obrigatório de execução no Gemini

0. **Priorize a pesquisa aplicável antes do visual:** em procedimentos jurídicos/administrativos municipais, consultar lei local, artigos e modificações relevantes; citar a fonte e preparar referências ABNT. Não afirmar que pesquisou se não houve consulta. Diagrama, pesquisa e ABNT são deveres independentes: **não sacrificar fundamentação legal por apresentação gráfica**.
1. **Identifique o fluxo e prepare a estrutura:** nós, rótulos, setas, bifurcações e lacunas confirmados. Não inventar etapas, condições, datas, autoridades nem base jurídica.
2. **Caminho obrigatório pretendido no Gemini: Canvas + SVG:** criar a composição em **Canvas do Gemini** usando **HTML com SVG inline**, abrir **Prévia** do Canvas e conferir que o fluxograma aparece realmente desenhado na tela. É a rota preferencial específica do pacote Gemini. **Verificar primeiro se a Skill e o Canvas funcionam conjuntamente nesta sessão**; o Google informa atualmente que a integração Skills+Canvas não é suportada, portanto **não afirmar que abriu Canvas sem realmente acioná-lo**. Caso Canvas não seja acionável a partir da Skill, registrar essa limitação concreta e continuar com saída SVG real em arquivo/prévia verificável, sem fingir sucesso no Canvas. Se SVG em arquivo ou prévia não puder ser exibido, usar **PNG ou visualização nativa** realmente acessível. Formatos são meios, não fins; a IA **decide livremente** qual recurso realmente utilizável produz a figura; a escolha tecnológica permanece da IA executora. Não recorrer a Mermaid.js embarcado se a Skill não puder executar JavaScript.
3. **Produza a figura, não somente a fonte:** não finalizar emitindo `graph TD`, `flowchart TD`, XML `<svg>`, código Mermaid, HTML ou um bloco **“Snippet de código”** como se isso fosse desenho. **Gerar um arquivo SVG não equivale a abrir uma prévia**; se for criado, solicitar sua exibição ou conferir que o arquivo gráfico real está acessível.
4. **Verifique antes de responder:** a figura aparece na própria interface? Há prévia visual realmente produzida? Ou há arquivo gráfico existente e acessível? Conferir nós/arestas/rótulos e marcar como concluída apenas uma **entrega visual verificável**. Não alegar que o usuário visualizou algo quando apenas a prévia/arquivo foi criado.
5. **Recupere em caso de somente código:** se a saída for snippet Mermaid/SVG/HTML, tentar **uma alternativa gráfica viável** na mesma sessão. Se falhar, informar **entrega parcial** e o impedimento observado; **Não inventar prévias**, não anunciar sucesso, não gerar link inexistente e não solicitar ferramentas ou serviços externos não autorizados.
6. **Não obrigar PDF nem download:** **PDF não é obrigatório**; gráfico visível no chat ou prévia gráfica já basta. PDF de auditoria, PNG/SVG para download e exportação só se solicitados ou necessários; a existência de um PDF não integra o critério de aceite.
7. **Canvas com verificação real:** Canvas com SVG é o **padrão solicitado para Gemini**, sujeito ao acesso efetivo na conversa. Se a interface com Skill disponibilizar Canvas utilizável nesta sessão, ele deve exibir HTML/SVG. **Não presumir** interoperabilidade e **não declarar impossível** o uso do Canvas sem observar a sessão; abrir Canvas em **conversa separada** pode ser alternativa manual, **não uma entrega feita pela Skill na conversa original**.
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

**Nota de compatibilidade 11/11/2026:** o suporte oficial Google sobre Skills declara que **ainda não funcionam com Canvas**. A instrução Canvas+SVG é uma preferência de execução e **não remove essa limitação da plataforma**; se necessário, oferecer orientação para o usuário abrir a visualização em conversa Canvas separada, como ação manual **não homologada como execução da Skill**.

**Validação:** registrar modelo, data, versão ativa da Skill, prompt, captura da resposta, recurso realmente acionado, **fontes normativas consultadas, dispositivos citados, bibliografia ABNT** e presença de figura, sem exigir PDF. Testes estáticos e CI não demonstram renderização real no Gemini.

GOOGLE. *Sobre a transição dos Gems para habilidades*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/18560919?hl=pt-BR. Acesso em: 11 nov. 2026.
