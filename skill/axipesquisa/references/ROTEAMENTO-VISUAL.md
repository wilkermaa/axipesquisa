# Microfase Diagramação do Fluxo de Aplicação — contrato de execução e aceite (v2.3.8)

**Exclusividade:** fase I — Integração, nível Gestão e Coordenação. **Quando houver fluxo fiel, IMAGEM VISÍVEL É OBRIGATÓRIA NA ENTREGA AXI**; produzir arquivo sem exibição, tabela, ASCII ou somente código não conclui. Exigir diagrama **mesmo sem pedido explícito** quando existir fluxo fielmente representável. Não impor nas fases A e X nem fabricar movimento em relações estáticas. Instruções de formato fechado prevalecem.

## Portas de execução

0. **Em tema legal:** conferir fontes normativas e artigos antes de diagramar. Exigir citações e ABNT além do visual, sem inventar rito administrativo.
1. **Detectar:** existe fluxo, decisão, sequência ou dependência funcional representável com elementos confirmados? Se não, encerrar microfase sem diagrama obrigatório.
2. **Escolher:** a IA/agente usa autonomamente a superfície visual efetivamente acessível nesta sessão (qualquer renderer nativo, Mermaid, SVG, HTML/Preview, imagem, tecnologia futura). São exemplos, não sequência obrigatória. Não inferir capacidade apenas pelo modelo.
3. **Executar:** realmente invocar a opção de renderização/prévia ou produzir imagem/arquivo, se o recurso permitir; não apenas apresentar `graph TD` como texto.
4. **Inspecionar:** considerar sucesso **IMAGEM do diagrama exibida inline ou prévia gráfica aberta e visível**, com nós, setas e rótulos corretos. **Arquivo gráfico apenas criado, sem prévia/exibição é entrega parcial**, não aprovação. Uma prévia já basta: **não exigir PDF, PNG, SVG nem download adicional**. PDF de auditoria é evidência opcional, não saída obrigatória.
**Plataformas:** ChatGPT usa Mermaid **desenhado em prévia**; Gemini deve **pedir imagem direta (SVG renderizado ou PNG)** com exibição na conversa; Claude usa visual HTML/SVG inline ou Artifact em prévia; Grok usa SVG com preview inline ou Projects Preview. Código isolado não basta, e **HTML/app interativo não é padrão**.
**Gemini Web (aplicação específica):** **pedir imagem já desenhada e mostrar o SVG/PNG na tela**, antes de tentar Canvas; Canvas/HTML são fallback restrito a uma prévia gráfica estática quando realmente acionável, **não** gerar app interativo por padrão. Se imagem direta falhar, tentar fallback real e registrar bloqueio observado. A IA deve verificar a prévia, nunca chamar `flowchart TD` em snippet de gráfico entregue. PDF não é obrigatório. O guia `references/GEMINI-DIAGRAMAS.md` detalha a execução e as limitações.
5. **Recuperar:** se a primeira tentativa só produzir texto/código, usar **uma alternativa viável** já habilitada. Sem alternativa, descrever a falha como **entrega parcial**; não simular imagem.
6. **Fidelidade:** checar nós/arestas/condições, legibilidade e incerteza do conteúdo; fontes jurídicas e administrativas não viram fatos por terem sido diagramadas.
7. **Economia e segurança:** entre opções que entregam visual correto, minimizar tokens, passos, chamadas, dependências e risco. Não enviar dados privados a renderizadores externos sem autorização.

## Oráculo de homologação

| Saída observável | Estado da microfase |
|---|---|
| Diagrama realmente visível no chat ou prévia | Aprovado para entrega visual (ainda requer fidelidade) |
| Arquivo gráfico real e acessível, mas não mostrado em prévia | **Parcial: não comprova entrega da imagem na tela** |
| Tabela, ASCII, lista, texto `graph TD` ou código Mermaid/SVG/HTML sem visual | Reprovado: apenas fonte; **não é imagem do fluxograma** |
| PDF que reproduz código sem figura | Evidência de código exportado, não requisito de PDF |
| Falha de recurso e explicação honesta | Parcial, não aprovado visualmente |

**Nota:** a Skill, por si, não abre ferramentas não disponibilizadas e não pode forçar renderer do frontend. Testes do repositório são estruturais; aceitação real requer teste na plataforma e evidência visual. Preservar a amostra científica C0/C1/C2 v2.2.0-rc2.
