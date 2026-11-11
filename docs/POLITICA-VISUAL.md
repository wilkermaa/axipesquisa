# AXI-Pesquisa v2.3.2 — política de visualização da microfase da Integração

**Hierarquia de competência:** Gestão e Coordenação define **o que deve ser entregue**, exclusivamente na microfase **Diagramação do Fluxo de Aplicação**, fase **I — Integração**. A IA/agente executora decide **como gerar e exibir** o visual com capacidades efetivamente disponíveis.

1. Se o fluxo de funcionamento/aplicação for representável fielmente, entregar um diagrama visual **mesmo sem pedido explícito**. Não forçar diagrama em conteúdos sem fluxo nem acrescentar etapas inventadas.
2. Não impor Mermaid, SVG, HTML, Canvas, PNG ou uma linguagem fechada. São exemplos; o agente pode escolher um mecanismo futuro. O requisito é **gráfico visível e fiel**.
3. Entre alternativas realmente capazes, minimizar tokens, passos, chamadas, dependências e conversões. Uma tentativa principal e uma alternativa útil, sem sondagens pagas cegas.
4. **Aceite:** visual exibido, prévia verificável ou arquivo gráfico real acessível. Código fonte, wireframe e texto puro isolados são **entrega parcial**. Não presumir que o usuário viu uma janela nem criar links fictícios.
5. Relatar limitações reais. SVG/PNG para download somente quando pedidos e efetivamente criados; manter unidades, nós, conexões, privacidade e acessibilidade.
6. **Gemini:** não prometer abertura automática do Canvas em uma Skill. Uma conversa Canvas separada, se necessária, depende de ação manual e não comprova entrega pela Skill.

Referências: `skill/axipesquisa/references/ROTEAMENTO-VISUAL.md` e guias por plataforma. Documento histórico: `docs/DECISAO-RENDERIZACAO-v2.3.0.md`.

**Status de validação:** regras editoriais e testes de fonte, sem homologação real garantida nas IAs nem redução de custos demonstrada. Preserva C0/C1/C2 v2.2.0-rc2.

