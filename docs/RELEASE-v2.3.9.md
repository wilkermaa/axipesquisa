# AXI Pesquisa v2.3.9 — Gemini, títulos curtos em caixas sem ícones

**PATCH · 11 nov. 2026.** Correção estética pontual na microfase **Diagramação do Fluxo de Aplicação**, fase I — Integração.

## Requisito aprovado

- A **imagem do fluxograma permanece obrigatória**, exibida na conversa ou em prévia visual aberta quando houver fluxo fiel e verificável.
- **Gemini:** visual equivalente ao Mermaid minimalista, com **somente título curto em cada caixa**, preferencialmente uma linha, no máximo duas linhas curtas.
- **Sem ícones, subtítulos, descrições internas, parágrafos ou microtextos** nas caixas; apenas setas, ramificações e rótulos breves de decisões.
- Explicações, dispositivos normativos, citações e **Fontes consultadas (ABNT)** devem permanecer fora da imagem.
- Se o gráfico sair excessivamente carregado, **tentar uma única simplificação**, sem inventar etapas jurídicas ou perder conexões essenciais.
- **Não** impor Mermaid.js no Gemini, criar app HTML/interativo sem pedido, converter a imagem em tabela/ASCII ou aceitar arquivo não exibido.
- **Demais IAs:** ChatGPT mantém Mermaid com prévia, Claude/Grok suas próprias prévias; a exigência de imagem visível e as regras de verificação permanecem.

## Validação e integridade

Testes de regressão, build dos oito instaladores, hashes SHA-256 e tag anotada são verificados no GitHub Actions antes da publicação. **não demonstram renderização real** no Gemini. A **homologação real** e funcional da imagem ainda precisa comprovar que o modelo desenhou corretamente; homologação funcional com imagem e auditoria jurídica continuam na Issue #4.

O experimento C0/C1/C2 da v2.2.0-rc2 e os arquivos históricos protegidos por hashes não foram alterados. Espelho GitHub/Drive corresponde ao commit/versionamento quando verificado em ambas as plataformas.

## Fontes consultadas (ABNT)

GOOGLE. *Gerar e editar imagens com os apps do Gemini*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/14286560?hl=pt-BR. Acesso em: 11 nov. 2026.

OPENAI. *Como trabalhar com blocos de escrita e blocos de código no ChatGPT*. [s.d.]. Disponível em: https://help.openai.com/pt-br/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt. Acesso em: 11 nov. 2026.
