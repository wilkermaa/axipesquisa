# AXI v1.0 — Guia de instalação e uso

## Conteúdo
- `AXI-Gemini.skill`: ZIP especializado para Gemini CLI (extensão `.skill`).
- `AXI-ChatGPT.zip`: pasta `axi/` dentro do ZIP para Skills, nos ambientes ChatGPT elegíveis.
- `AXI-Claude.zip`: pasta `axi/` dentro do ZIP para Skills do Claude.
- `FONTES-ABNT.md`: documentação oficial consultada.
- `VALIDACAO.json`: validação estrutural e hashes dos três pacotes.

## Gemini CLI
1. Instale/atualize o Gemini CLI se necessário e abra o terminal.
2. Execute `gemini skills install /caminho/AXI-Gemini.skill`.
3. No Gemini CLI, use `/skills list` e, se necessário, `/skills reload`.
4. Faça uma pergunta que corresponda à descrição da skill e autorize a ativação quando solicitado.
5. Alternativa manual: extraia a pasta `axi/` em `~/.gemini/skills/axi/` ou `.gemini/skills/axi/` no projeto.
Observação: Este pacote destina-se ao Gemini CLI. O Gemini Web/Google AI Studio não tem aqui compatibilidade garantida com esse arquivo.

## ChatGPT
1. Caso sua conta e seu workspace tenham Skills habilitadas, abra Plugins > Skills.
2. Selecione Criar > Upload do computador e escolha `AXI-ChatGPT.zip`.
3. Aguarde o processamento/checagem e execute o teste de explicação.
4. Se o menu não existir, a função pode não estar disponível no plano ou no workspace. A documentação consultada lista Business, Enterprise, Healthcare e Edu elegíveis. O ZIP pode também ser aproveitado como referência de implementação em produtos OpenAI compatíveis, mas a importação não foi verificada remotamente.

## Claude
1. Abra Personalizar > Skills (Habilidades).
2. Clique em Adicionar (+), depois Criar skill > Carregar uma skill.
3. Escolha `AXI-Claude.zip` e habilite a skill.
4. Faça os testes indicados em `references/exemplos.md`.
Observação: A função requer a capacidade de execução de código habilitada, conforme documentação da Anthropic consultada.

## Testes recomendados
1. “Explique algoritmo com uma lista de compras.” Deve começar com `Orientação AXI aplicada`, ser simples e terminar com a assinatura.
2. “Compare duas técnicas em tabela.” Deve trazer tabela quando útil.
3. “Responda apenas este JSON: {"ok":true}”. Deve retornar somente JSON, sem assinatura.
4. “Pesquise uma fonte e cite em ABNT.” Deve citar apenas fontes realmente consultadas, com data correta.
5. “Escreva somente uma mensagem pronta para copiar.” Não deve incluir a assinatura AXI no texto que será enviado.

## Limitações
- Skills são recursos sob demanda; não equivalem, por si sós, a instruções globais.
- Validação local é estrutural. Não houve upload autenticado nem execução funcional nos serviços Gemini, ChatGPT ou Claude.
- Instruções de sistema, políticas, segurança e formatos estritos têm precedência.
- Nenhum ZIP contém chaves de API, executáveis ou dependências externas.

## Assinatura configurada
`◌ AXI · instrução personalizada - wilkermaa@gmail.com`
