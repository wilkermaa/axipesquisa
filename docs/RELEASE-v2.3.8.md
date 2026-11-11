# AXI Pesquisa v2.3.8 — imagem obrigatória na entrega visual

**PATCH · 11 nov. 2026.** Escopo: microfase **Diagramação do Fluxo de Aplicação** da fase I — Integração, no nível Gestão e Coordenação. O requisito de imagem foi explicitamente aprovado pelo autor após testes que produziram tabela, ASCII e aplicativo HTML desnecessário.

## Contrato obrigatório

- Quando houver fluxo representável e fielmente verificado, **a AXI Pesquisa deve ENTREGAR UMA IMAGEM DE FLUXOGRAMA EXIBIDA NA TELA ou em PRÉVIA GRÁFICA ABERTA** antes da conclusão. Vale nas oito IAs, mesmo sem pedido explícito de diagrama.
- **Não equivalem a imagem entregue:** tabela, lista, ASCII, código Mermaid/SVG/HTML, bloco Snippet de código, texto anunciando app ou arquivo SVG/PNG gerado mas não exibido. Cada um implica **entrega parcial** quando não houver prévia.
- **Gemini: imagem primeiro.** Solicitar/acionar a ferramenta de criação de imagem na sessão para **desenhar fluxograma estático SVG renderizado ou PNG com blocos e setas**, sem app HTML/Canvas por padrão. Se a primeira falhar, tentar fallback gráfico viável. **Interatividade apenas a pedido explícito.**
- **Outras plataformas:** ChatGPT continua Mermaid quando realmente desenhado em prévia, Claude usa imagem inline/Artifact, Grok SVG/PNG com visualização real. CLI/IDE deve abrir prévia quando habilitada, não declarar sucesso por mero arquivo.
- **Validade semântica:** desenho precisa refletir nós e conexões normativamente verificadas; imagem inventando lei, autoridade, rito ou prazo reprova. Leitura integral da Skill, pesquisa jurídica e ABNT permanecem deveres independentes.
- **Exceções:** não inventar processo para temas sem fluxo, respeitar pedido de formato fechado e instruções superiores. PDF e download não são obrigatórios quando a imagem está na tela.

## Compatibilidade externa

A ajuda Google documenta criação de imagens nos apps Gemini, mas **não garante invocação automática de Imagens por uma Skill ativa**. Também registra que **Canvas ainda não funciona com Skills**. O sucesso dessa rota deve ser verificado em teste real no Gemini, não presumido em razão da nova redação.

## Testes e governança

Testes estruturais e CI verificam contrato textual, 8 ZIPs, manifestos e preservação de conteúdo; **não demonstram renderização real no Gemini**. Homologação funcional e homologação real da imagem na UI permanecem na Issue #4; espelhamento Drive permanece na Issue #6. Tags e assets anteriores preservados, experimento científico C0/C1/C2 da v2.2.0-rc2 intacto.

## Fontes consultadas (ABNT)

GOOGLE. *Gerar e editar imagens com os apps do Gemini*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/14286560?hl=pt-BR. Acesso em: 11 nov. 2026.

GOOGLE. *Sobre a transição dos Gems para habilidades*. 2026. Disponível em: https://support.google.com/gemini/answer/18560919?hl=pt-BR. Acesso em: 11 nov. 2026.
