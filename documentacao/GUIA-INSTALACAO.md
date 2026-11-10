# Guia de instalação — axipesquisa 2.0.0

**Data de elaboração:** 4 de novembro de 2026. **Estado:** pacotes gerados e validados localmente; ainda não testados nos serviços reais. A disponibilidade de interfaces depende de plano, versão, região e configurações administrativas.

## Pré-requisito comum

`axipesquisa` contém um arquivo principal `SKILL.md` com frontmatter YAML e arquivos auxiliares `references/` e `assets/`. A instalação não cria contas, não habilita uma função bloqueada e não configura automaticamente regras globais. A ativação da skill costuma depender de correspondência com a tarefa, ou de invocação explícita.

## 1. ChatGPT Web

Pacote: `axipesquisa-v2-chatgpt-web.zip` (raiz do ZIP: `axipesquisa/SKILL.md`). Em contas que possuem Skills, abra **Plugins > Habilidades > Criar > Carregar do computador**. A página da OpenAI consultada em 4/11/2026 limita o recurso às contas elegíveis Business, Enterprise, Healthcare e Edu e respectivas políticas de workspace. **Em Free, Go, Plus ou Pro sem Skills:** use a versão resumida de instruções em `alternativas/CHATGPT-INSTRUCOES-PERSONALIZADAS.md` nas configurações de Personalização (pode haver limites de caracteres), ou configure um projeto que permita instruções. A alternativa por texto não garante carregar arquivos auxiliares nem equivalência integral à skill.

Fonte: https://help.openai.com/pt-br/articles/20001066-skills-in-chatgpt; https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions

## 2. Gemini Web

Pacote: `axipesquisa-v2-gemini-web.zip` (`SKILL.md` na raiz do ZIP, com referências ao lado). Acesse `https://gemini.google.com` > **Personalizar > Habilidades > Criar > Fazer upload**. O Google admite um `SKILL.md` individual, uma pasta ou um `.zip` com esse arquivo na pasta principal. O recurso requer conta elegível, idade mínima informada na ajuda e configuração Manter Atividade. Se a interface não exibir Habilidades, a disponibilidade pode variar.

Fonte: https://support.google.com/gemini/answer/17094296?hl=pt-br

## 3. Grok Web

Pacote: `axipesquisa-v2-grok-web.zip` (`SKILL.md` na raiz); arquivo individual alternativo: `alternativas/GROK-WEB-SKILL.md`. Em `https://grok.com`, abra o gerenciamento/criação de Skills e utilize a opção de **carregar arquivo** ou peça ao criador de skills que incorpore o `SKILL.md`. A xAI confirma a existência de Skills no web e criação por conversa, arquivo ou edição manual, mas a publicação consultada **não especifica o formato ZIP exato**. Se a tela recusar o ZIP, importe o `.md` avulso e as referências se a interface permitir. Não afirmar que um ZIP foi importado antes de testar.

Fonte: https://x.ai/news/grok-skills

## 4. Claude Web

Pacote: `axipesquisa-v2-claude-web.zip` (pasta `axipesquisa/SKILL.md` no ZIP). Vá para **Personalizar > Skills > + > Criar skill > Carregar um skill**. Carregue o ZIP e ative. A estrutura com pasta principal é exigência documentada pela Anthropic. A interface pode variar por conta.

Fonte: https://support.claude.com/pt/articles/12512180-usar-skills-no-claude; https://support.claude.com/pt/articles/12512198-como-criar-habilidades-personalizadas

## 5. Codex

Pacote: `axipesquisa-v2-codex.zip`, com diretório `.agents/skills/axipesquisa/SKILL.md` após extrair no repositório. Para uso pessoal, extraia o conteúdo da pasta interna em `~/.agents/skills/axipesquisa/`. Em Codex CLI/IDE, use `/skills` ou mencione `$axipesquisa` quando disponível. O ZIP é meio de transporte, **não upload nativo**.

```bash
unzip axipesquisa-v2-codex.zip -d /caminho/do/projeto
# ou copie .agents/skills/axipesquisa para ~/.agents/skills/axipesquisa
```

Fonte: https://learn.chatgpt.com/docs/build-skills

## 6. Google Antigravity

Pacote: `axipesquisa-v2-antigravity.zip`. Extraia no workspace, preservando `.agents/skills/axipesquisa/SKILL.md`; para instalação global, use `~/.gemini/config/skills/axipesquisa/`. A documentação atual registra `.agents/skills` como caminho preferencial e `.agent/skills` como compatibilidade legada. A skill pode ser ativada automaticamente quando relevante ou por `/axipesquisa` conforme a versão.

Fonte: https://antigravity.google/docs/skills?app=antigravity-ide

## 7. Grok Build CLI

Pacote: `axipesquisa-v2-grok-build-cli.zip`. Extraia em `.grok/skills/axipesquisa/SKILL.md` no projeto; para pessoal, `~/.grok/skills/axipesquisa/SKILL.md`. Confira o que o CLI identificou com `grok inspect` ou use `/skills` no ambiente interativo. Não confundir Grok Build CLI com Grok Web.

Fonte: https://docs.x.ai/build/features/skills-plugins-marketplaces; https://docs.x.ai/build/cli/reference

## 8. Claude Code

Pacote: `axipesquisa-v2-claude-code.zip`. Extraia em `.claude/skills/axipesquisa/SKILL.md` no projeto ou `~/.claude/skills/axipesquisa/SKILL.md` para uso pessoal. Invoque `/axipesquisa` para teste ou permita ativação por tarefa. Skills pessoais locais podem não aparecer em sessões cloud; consultar sincronização de skills do claude.ai quando necessário.

Fonte: https://code.claude.com/docs/en/skills

## Personalizar assinatura

Abra `assets/CONFIGURACAO-USUARIO.md` dentro da skill. Altere nome/e-mail e a preferência de assinatura. A versão entregue está configurada para usar o e-mail anteriormente fornecido nas instruções AXI; se publicar a skill, substitua os dados pessoais. A instrução explícita atual do usuário prevalece.

## Testes após instalar

1. `Explique autenticação em um sistema web pelo AXI, incluindo o todo, suas partes, analogias e fluxo prático.`
2. `Pesquise duas fontes oficiais sobre um tema e liste TODAS as fontes consultadas em ABNT imediatamente antes da assinatura.`
3. `Responda apenas com JSON válido: {"teste": true}` (deve preservar JSON).
4. `Use a assinatura ◌ AXI · Maria nesta resposta` (deve respeitar a identidade configurada na mensagem).

O resultado desses testes **não foi executado nos serviços**. Use `references/EXEMPLOS-E-TESTES.md` para uma bateria completa e `RELATORIO-VALIDACAO.json` para validação estática.
