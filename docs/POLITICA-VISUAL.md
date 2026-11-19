# AXI-Pesquisa v2.3.8 — política de entrega visual na microfase da Integração

**Imagem obrigatória na entrega AXI Pesquisa:** toda microfase I acionada por um fluxo fiel exige **figura estática real do diagrama visível na resposta ou em prévia aberta**; arquivo apenas criado sem exibição NÃO conclui. Não fabricar imagem de fluxo em objetos estáticos ou quando a saída rígida do usuário a impedir.

**Gestão e Coordenação** da microfase **Diagramação do Fluxo de Aplicação**, exclusivamente na **I — Integração**, define o resultado visual; a IA/agente executora seleciona livremente e **aciona concretamente** o mecanismo disponível (prévia, renderer, artefato, SVG, HTML, PNG ou outro). A exigência aplica-se quando existe fluxo fielmente representável **mesmo sem pedido explícito**. Não é regra universal de imagens nas fases A e X.

## Aceite

- **Suficiente:** IMAGEM do fluxograma realmente exibida no chat ou prévia visual efetivamente aberta e visível. **Arquivo gráfico apenas acessível sem preview é entrega parcial.** Arquivo não é exigido se a tela já mostra o gráfico.
- **PDF não obrigatório:** no teste anterior o PDF foi uma **evidência exportada**; sua existência, ausência ou formato não integra o requisito da microfase.
- **Insuficiente:** tabela, lista, ASCII, `graph TD`, código Mermaid/SVG/HTML, frases com setas, aplicativo não solicitado ou arquivo não exibido. Nenhum deles é imagem entregue na tela.
- **Recuperação:** após saída apenas textual, uma alternativa visual habilitada; persistindo falha, relatar **entrega parcial**, não fingir sucesso.
- **Economia:** fidelidade e visual primeiro; entre soluções capazes, menor custo real em tokens, chamadas, conversões e passos. Sem HTML/JS excessivo nem exportações desnecessárias.
- **Confiabilidade:** preservar nós, decisões, lacunas e fontes. Não inventar fatos administrativos; transparência sobre limitações da sessão e consentimento para serviços externos.
- **Exceções:** instruções superiores, formatos rigidamente solicitados e ausência de fluxo representável; não quebrar saídas fechadas.

## Não substituição da pesquisa e das citações jurídicas

A microfase visual **não dispensa consulta à legislação aplicável nem referências ABNT**. Em procedimento local, identificar lei, artigo, alterações e formalidades diferenciadas **antes** de desenhar; não representar atos administrativos hipotéticos como obrigatórios. Verificação final independente: **fonte normativa confirmada, bibliografia ABNT verificável e figura realmente apresentada** (ou saída parcial com limitações reais). O art. 57 da Lei nº 1.165/2008 em Matinhos é caso de regressão: entre secretarias = Portaria; dentro da mesma secretaria = Ofício, conforme fonte compilada consultada; confirmação oficial continua recomendada.

## Rotas específicas sem substituir fidelidade e ABNT

**ChatGPT:** Mermaid efetivamente desenhado em prévia como imagem; **Gemini:** **geração direta de imagem SVG/PNG e exibição na conversa**, sem app/HTML por padrão, com fallback estático somente se renderizar de fato; Canvas continua com restrição de Skills documentada; **Claude:** visual personalizado HTML/SVG renderizado inline ou Artifact; **Grok:** SVG real com prévia inline ou Projects HTML Preview. O instalador de cada plataforma descreve seu caminho. **Leitura integral da Skill em início→meio→fim, um arquivo por vez, é fundamento.** A rota específica não permite fingir ferramenta e não afasta referências ABNT em todas as explicações.

## Gemini Web — execução específica

Na **microfase Diagramação do Fluxo de Aplicação**, o modelo no Gemini deve **solicitar/acionar a criação de uma IMAGEM direta do fluxo e mostrá-la na própria tela**, antes de concluir. Preferir SVG efetivamente renderizado ou PNG/gráfico nativo com prévia; **não solicitar HTML/app interativo por padrão**, nem tratar tabela ou ASCII como figura. Um `flowchart TD` em snippet, texto SVG/HTML ou código Mermaid é falha visual mesmo que esteja sintaticamente correto. **Não exigir PDF nem exportação** se a figura já está na interface. Verificar fidelidade, legibilidade e existência da **imagem exibida ou prévia aberta**, não apenas arquivo gerado; sem sucesso, declarar entrega parcial. Não confundir a presença da opção Canvas no chat com uma chamada efetiva; a Skill **não precisa executar dentro do Canvas**, somente solicitar/acionar a ferramenta de saída e verificar a Prévia. Não presumir que esse acionamento é suportado nem declarar ausência de opção sem testar. Esta prioridade é específica do Gemini: **não prescrever tecnologia às outras IAs**.

## Red team

Revisão dos 20 riscos documentada em `docs/REDTEAM-MICROFASE-v2.3.3.md`. Os principais riscos eram: falta de ação concreta de renderização, código confundido com figura, referência condicional não carregada, suposição de Canvas, criação fictícia de arquivos, custo desnecessário, detalhes jurídicos não validados, formatos estritos, privacidade e confusão entre teste estrutural e homologação. Mitigações são instruções; **interoperabilidade real com a interface permanece pendente de testes em produto**.

**Referências operacionais:** `skill/axipesquisa/references/ROTEAMENTO-VISUAL.md` e `references/GEMINI-DIAGRAMAS.md`. Histórico preservado: v2.3.2 e protocolo científico v2.2.0-rc2.
