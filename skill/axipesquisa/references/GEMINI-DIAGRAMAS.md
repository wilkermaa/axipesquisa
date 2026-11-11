# Gemini Web — execução visual obrigatória na microfase I (v2.3.7)

**Capacidade visual:** verificar a capacidade de renderização nesta sessão; o nome do produto não demonstra acesso efetivo a um visualizador.

**Escopo:** somente a microfase **Diagramação do Fluxo de Aplicação**, parte da fase **I — Integração**, nível Gestão e Coordenação. Em um fluxo fielmente representável, **tentar entregar gráfico visível mesmo sem pedido explícito**. A regra central também está no `SKILL.md`, independentemente de o modelo consultar este guia.

## Procedimento obrigatório de execução no Gemini

0. **Priorize a pesquisa aplicável antes do visual:** em procedimentos jurídicos/administrativos municipais, consultar lei local, artigos e modificações relevantes; citar a fonte e preparar referências ABNT. Não afirmar que pesquisou se não houve consulta. Diagrama, pesquisa e ABNT são deveres independentes: **não sacrificar fundamentação legal por apresentação gráfica**.
1. **Identifique o fluxo e prepare a estrutura:** nós, rótulos, setas, bifurcações e lacunas confirmados. Não inventar etapas, condições, datas, autoridades nem base jurídica.
2. **Canvas como ferramenta de saída: CHAME-O para gerar a Prévia SVG.** A Skill executa **A, X e prepara o fluxo no chat**. Na fase I, solicitar/acionar **Canvas para criar um documento HTML com SVG inline e exibir a Prévia**, na conversa atual, quando houver ação compatível. **Não colocar a Skill para funcionar dentro do Canvas. Não é necessária interação após a geração:** o objetivo é entregar uma figura que o usuário consiga visualizar.
   - **Ordem operacional:** `AXI define nós e relações → chama Canvas → Canvas gera HTML/SVG → abre Prévia → AXI verifica o desenho`. Use só o conteúdo necessário do diagrama e **não inclua dados pessoais ou jurídicos não confirmados**.
   - **Ativação não é suposição:** mesmo que o botão Canvas apareça, é preciso **efetivamente solicitar a criação/abertura da Prévia**. Nem botão visível nem snippet HTML equivalem a figura. Não afirme que a chamada foi concluída sem retorno ou evidência da tela.
   - **Limite documentado:** a ajuda oficial Google ainda declara que **Skills não funcionam com Canvas** e inclui Canvas entre as ferramentas não suportadas por Skills. Isso **não prova que o botão Canvas desaparece**, mas também **não comprova que o modelo possa encaminhar automaticamente uma chamada originada na Skill**. A chamada é uma **hipótese operacional a testar no Gemini real**, não uma integração garantida pela Skill. Não se esconder atrás de limitação presumida: tentar acionar a ação habilitada; se houver recusa concreta, registrar.
   - **Recuperação:** se a chamada ao Canvas falhar, tentar SVG ou PNG real em prévia/arquivo acessível, sem depender de Mermaid.js executado pela Skill. Se não houver visual, registrar entrega parcial e a impossibilidade observada, sem exigir conversa separada ou intervenção manual como prova de conclusão.
3. **Produza a figura, não somente a fonte:** não finalizar emitindo `graph TD`, `flowchart TD`, XML `<svg>`, código Mermaid, HTML ou um bloco **“Snippet de código”** como se isso fosse desenho. **Gerar um arquivo SVG não equivale a abrir uma prévia**; se for criado, solicitar sua exibição ou conferir que o arquivo gráfico real está acessível.
4. **Verifique antes de responder:** a figura aparece na própria interface? Há prévia visual realmente produzida? Ou há arquivo gráfico existente e acessível? Conferir nós/arestas/rótulos e marcar como concluída apenas uma **entrega visual verificável**. Não alegar que o usuário visualizou algo quando apenas a prévia/arquivo foi criado.
5. **Recupere em caso de somente código:** se a saída for snippet Mermaid/SVG/HTML, tentar **uma alternativa gráfica viável** na mesma sessão. Se falhar, informar **entrega parcial** e o impedimento observado; **Não inventar prévias**, não anunciar sucesso, não gerar link inexistente e não solicitar ferramentas ou serviços externos não autorizados.
6. **Não obrigar PDF nem download:** **PDF não é obrigatório**; gráfico visível no chat ou prévia gráfica já basta. PDF de auditoria, PNG/SVG para download e exportação só se solicitados ou necessários; a existência de um PDF não integra o critério de aceite.
7. **Separar orquestração e execução:** a Skill continua coordenando a resposta AXI e pede ao Canvas **apenas a geração de HTML/SVG e a abertura da Prévia**, sem precisar estar ativa dentro dele. **Não presumir** interoperabilidade e **não declarar impossível** a tentativa apenas pela documentação; validar a chamada real. Caso o usuário opte por abrir Canvas em **conversa separada**, isso é uma alternativa manual e **não prova execução pela Skill na conversa original**.
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

**Nota de compatibilidade 11/11/2026:** o suporte oficial Google sobre Skills declara que **ainda não funcionam com Canvas**, inclusive em sua lista de ferramentas. **A orquestração Skill → chamada Canvas → Prévia é o fluxo pretendido pelo autor, porém não há confirmação documental de que essa chamada seja permitida na execução de Skills.** Isso exige ensaio funcional, não negativa antecipada nem alegação de sucesso. **A presença do botão Canvas é distinta da possibilidade de chamada automática.**

**Validação:** registrar modelo, data, versão ativa da Skill, prompt, captura da resposta, recurso realmente acionado, **fontes normativas consultadas, dispositivos citados, bibliografia ABNT** e presença de figura, sem exigir PDF. Testes estáticos e CI não demonstram renderização real no Gemini.

GOOGLE. *Sobre a transição dos Gems para habilidades*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/18560919?hl=pt-BR. Acesso em: 11 nov. 2026.
