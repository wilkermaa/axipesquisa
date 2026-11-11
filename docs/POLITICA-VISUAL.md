# AXI-Pesquisa v2.3.3 — política de entrega visual na microfase da Integração

**Gestão e Coordenação** da microfase **Diagramação do Fluxo de Aplicação**, exclusivamente na **I — Integração**, define o resultado visual; a IA/agente executora seleciona livremente e **aciona concretamente** o mecanismo disponível (prévia, renderer, artefato, SVG, HTML, PNG ou outro). A exigência aplica-se quando existe fluxo fielmente representável **mesmo sem pedido explícito**. Não é regra universal de imagens nas fases A e X.

## Aceite

- **Suficiente:** gráfico realmente exibido no chat, prévia visual gerada ou arquivo gráfico real acessível. Arquivo não é exigido se a tela já mostra o gráfico.
- **PDF não obrigatório:** no teste anterior o PDF foi uma **evidência exportada**; sua existência, ausência ou formato não integra o requisito da microfase.
- **Insuficiente:** `graph TD`, código Mermaid/SVG/HTML, frases com setas ou wireframe textual sem figura renderizada.
- **Recuperação:** após saída apenas textual, uma alternativa visual habilitada; persistindo falha, relatar **entrega parcial**, não fingir sucesso.
- **Economia:** fidelidade e visual primeiro; entre soluções capazes, menor custo real em tokens, chamadas, conversões e passos. Sem HTML/JS excessivo nem exportações desnecessárias.
- **Confiabilidade:** preservar nós, decisões, lacunas e fontes. Não inventar fatos administrativos; transparência sobre limitações da sessão e consentimento para serviços externos.
- **Exceções:** instruções superiores, formatos rigidamente solicitados e ausência de fluxo representável; não quebrar saídas fechadas.

## Red team

Revisão dos 20 riscos documentada em `docs/REDTEAM-MICROFASE-v2.3.3.md`. Os principais riscos eram: falta de ação concreta de renderização, código confundido com figura, referência condicional não carregada, suposição de Canvas, criação fictícia de arquivos, custo desnecessário, detalhes jurídicos não validados, formatos estritos, privacidade e confusão entre teste estrutural e homologação. Mitigações são instruções; **interoperabilidade real com a interface permanece pendente de testes em produto**.

**Referências operacionais:** `skill/axipesquisa/references/ROTEAMENTO-VISUAL.md` e `references/GEMINI-DIAGRAMAS.md`. Histórico preservado: v2.3.2 e protocolo científico v2.2.0-rc2.
