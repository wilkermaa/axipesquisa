# AXI-Pesquisa v2.2.0-rc4 | Correção do Mermaid visual

Autor: Wilker M. de Araujo Alexandre
Data: 10/11/2026

## Qual instalador usar?
- `01-INSTALADORES/01-CHATGPT-WEB-AXI-v2.2.0-rc4.zip` -> ChatGPT Web.
- `01-INSTALADORES/02-GEMINI-WEB-AXI-v2.2.0-rc4.zip` -> Gemini Web.
- `01-INSTALADORES/03-CLAUDE-WEB-AXI-v2.2.0-rc4.zip` -> Claude Web.
- Os demais instaladores trazem nomes explícitos para cada plataforma.

**Não confunda** pacotes de Skill com pacotes de execução dos testes C0/C1/C2. Estes ZIPs são para instalação da Skill, não para o benchmark congelado na rc2.

## Correção de comportamento na fase I (Integração)

- Diagrama opcional em respostas comuns.
- Quando um diagrama Mermaid renderizado é expressamente solicitado, não basta entregar um bloco de código ou wireframe.
- A Skill deverá tentar recursos de renderização realmente habilitados; se não houver motor Mermaid, poderá criar representação visual equivalente com recurso de arquivos/Canvas, informando a diferença.
- Quando solicitados e possíveis, fornecer SVG e PNG reais para download; se não forem possíveis, relatar tentativas e limitação específica, sem inventar arquivos.
- Não representar estados concluído/atenção/bloqueado como fatos sem evidência. Manter status "a validar" nos casos hipotéticos.

## Arquivos ilustrativos

`04-DIAGRAMA-DEMONSTRATIVO` inclui **fonte Mermaid original** enviada pelo usuário e **visualização equivalente gerada com Graphviz** em SVG e PNG. NÃO é compilação nativa Mermaid; os estados coloridos desse exemplo são ilustrativos e não foram auditados.

## Verificações concluídas

- 47/47 testes locais automatizados passaram (estrutura e políticas).
- Validador estático confirmou oito pacotes e um candidato de plugin.
- Integridade dos ZIPs conferida.
- Não houve execução da Skill no Gemini Web a partir desta sessão; portanto, **o comportamento no Gemini continua pendente de teste real**.
- A RC3 anterior, já identificada, deve ser preservada. A rc4 é uma correção nova, não altera o experimento empírico congelado na rc2.

## Limitações e fontes

- GOOGLE. Gerenciar tarefas e fluxos de trabalho nos apps do Gemini. [s.d.]. https://support.google.com/gemini/answer/17094507?hl=pt-BR. Acesso em: 10 nov. 2026.
- GOOGLE. Criar documentos, apps e muito mais com o Canvas. [s.d.]. https://support.google.com/gemini/answer/16047321?hl=pt-BR. Acesso em: 10 nov. 2026.

A existência de capacidade de arquivos SVG/PNG no Gemini não implica existência de motor Mermaid em toda sessão. A Skill é instrução, não instala um renderizador por si só.
