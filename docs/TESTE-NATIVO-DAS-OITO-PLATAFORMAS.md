# Protocolo de aceitação em interfaces reais

Este documento não comprova compatibilidade; define como testar e registrar. **Não use screenshots com dados pessoais em repositório público.**

## Pré-condições

1. Confirmar versão, plano, permissão de upload, região e data em cada produto.
2. Baixar e examinar o pacote correto; verificar `manifest-sha256.json`.
3. Importar/instalar a Skill nativa, confirmar nome `axipesquisa` e ativação. Se a plataforma não oferecer importação, registrar **não disponível** sem simular aceite.
4. Repetir 36 cenários do `tests/cases.json`. Salvar saída integral, sinalizar instruções ou imagens anexadas e fonte efetivamente consultada pela plataforma. Não inserir dados privados nos casos públicos.
5. Marcar falhas por critério; rever com dois avaliadores quando possível. Não confundir um modelo da API com o modelo ou orquestração do produto Web.

## Matriz de registro

| Ambiente | Importado? | Skill realmente ativada? | 36 testes realizados? | Restrições registradas? |
|---|---|---|---|---|
| ChatGPT Web | Não testado | Não testado | 0/36 | Elegibilidade específica |
| Gemini Web | Não testado | Não testado | 0/36 | UI/conta |
| Grok Web | Não testado | Não testado | 0/36 | A importação ZIP precisa ser verificada |
| Claude Web | Não testado | Não testado | 0/36 | UI/conta |
| Codex | Não testado | Não testado | 0/36 | Escopo projeto/global |
| Antigravity | Não testado | Não testado | 0/36 | Escopo projeto/global |
| Grok Build CLI | Não testado | Não testado | 0/36 | Versão CLI |
| Claude Code | Não testado | Não testado | 0/36 | Escopo projeto/global |

## Quais provas guardar

- Captura da tela de importação/instalação ou saída da CLI com versão.
- Identificador do modelo e timestamp de cada teste, se disponíveis.
- Respostas originais para T17 JSON, T18 CSV, T19 Python, T20 tradução, T21–T23 injeções e T25–T27 identidade.
- Lista de URLs de fontes efetivamente consultadas, com falhas e conflito quando houver.
- Evidência de que ações externas não ocorreram sem autorização do usuário.

Se o produto usar ferramentas automáticas de pesquisa, não misturar resultados com o estudo API **sem ferramentas**: são testes de ecossistemas diferentes.
