# AXI-Pesquisa v2.3.5 — política de entrega visual na microfase da Integração

**Gestão e Coordenação** da microfase **Diagramação do Fluxo de Aplicação**, exclusivamente na **I — Integração**, define o resultado visual; a IA/agente executora seleciona livremente e **aciona concretamente** o mecanismo disponível (prévia, renderer, artefato, SVG, HTML, PNG ou outro). A exigência aplica-se quando existe fluxo fielmente representável **mesmo sem pedido explícito**. Não é regra universal de imagens nas fases A e X.

## Aceite

- **Suficiente:** gráfico realmente exibido no chat, prévia visual gerada ou arquivo gráfico real acessível. Arquivo não é exigido se a tela já mostra o gráfico.
- **PDF não obrigatório:** no teste anterior o PDF foi uma **evidência exportada**; sua existência, ausência ou formato não integra o requisito da microfase.
- **Insuficiente:** `graph TD`, código Mermaid/SVG/HTML, frases com setas ou wireframe textual sem figura renderizada.
- **Recuperação:** após saída apenas textual, uma alternativa visual habilitada; persistindo falha, relatar **entrega parcial**, não fingir sucesso.
- **Economia:** fidelidade e visual primeiro; entre soluções capazes, menor custo real em tokens, chamadas, conversões e passos. Sem HTML/JS excessivo nem exportações desnecessárias.
- **Confiabilidade:** preservar nós, decisões, lacunas e fontes. Não inventar fatos administrativos; transparência sobre limitações da sessão e consentimento para serviços externos.
- **Exceções:** instruções superiores, formatos rigidamente solicitados e ausência de fluxo representável; não quebrar saídas fechadas.

## Não substituição da pesquisa e das citações jurídicas

A microfase visual **não dispensa consulta à legislação aplicável nem referências ABNT**. Em procedimento local, identificar lei, artigo, alterações e formalidades diferenciadas **antes** de desenhar; não representar atos administrativos hipotéticos como obrigatórios. Verificação final independente: **fonte normativa confirmada, bibliografia ABNT verificável e figura realmente apresentada** (ou saída parcial com limitações reais). O art. 57 da Lei nº 1.165/2008 em Matinhos é caso de regressão: entre secretarias = Portaria; dentro da mesma secretaria = Ofício, conforme fonte compilada consultada; confirmação oficial continua recomendada.

## Gemini Web — execução específica

Na **microfase Diagramação do Fluxo de Aplicação**, o modelo no Gemini deve **acionar a geração ou abertura da prévia visual na própria sessão** antes de concluir. **Priorizar SVG efetivamente renderizado**, quando viável; caso contrário, **PNG ou gráfico nativo**. Um `flowchart TD` em snippet, texto SVG/HTML ou código Mermaid é falha visual mesmo que esteja sintaticamente correto. **Não exigir PDF nem exportação** se a figura já está na interface. Verificar fidelidade, legibilidade e existência da prévia ou arquivo real; sem sucesso, declarar entrega parcial. Não supor que Canvas da conta esteja disponível dentro da mesma sessão com Skill. Esta prioridade é específica do Gemini: **não prescrever tecnologia às outras IAs**.

## Red team

Revisão dos 20 riscos documentada em `docs/REDTEAM-MICROFASE-v2.3.3.md`. Os principais riscos eram: falta de ação concreta de renderização, código confundido com figura, referência condicional não carregada, suposição de Canvas, criação fictícia de arquivos, custo desnecessário, detalhes jurídicos não validados, formatos estritos, privacidade e confusão entre teste estrutural e homologação. Mitigações são instruções; **interoperabilidade real com a interface permanece pendente de testes em produto**.

**Referências operacionais:** `skill/axipesquisa/references/ROTEAMENTO-VISUAL.md` e `references/GEMINI-DIAGRAMAS.md`. Histórico preservado: v2.3.2 e protocolo científico v2.2.0-rc2.
