# Plataformas: instalação e status em 04/11/2026

Esta é a documentação de **caminhos de distribuição**. A leitura de documentação pública não representa teste de importação em conta do usuário. Pacotes em `dist/` são produzidos por `python scripts/build.py`.

| Ambiente | Instalação/extração proposta | Observações e status |
|---|---|---|
| ChatGPT Web | `dist/axipesquisa-2.2.2-chatgpt-web.zip` com pasta `axipesquisa/SKILL.md` | Disponibilidade depende da conta/workspace. A documentação OpenAI confirma carregamento direto do computador para contas elegíveis. **Skill individual é diferente de Plugin de diretório.** Alternativa por instruções personalizadas. **Não testado em conta real.** |
| Gemini Web | `dist/axipesquisa-2.2.2-gemini-web.zip` com `SKILL.md` na raiz do ZIP e recursos ao lado | Google aceita `SKILL.md`, pasta ou ZIP com arquivo na pasta principal. **Não testado no painel.** |
| Grok Web | `dist/axipesquisa-2.2.2-grok-web.zip` com `SKILL.md` na raiz e arquivo individual no repositório | xAI diz que cria Skills por conversa/arquivo; aceitação **específica de ZIP não confirmada**. Alternativa: texto do `SKILL.md`. |
| Claude Web | `dist/axipesquisa-2.2.2-claude-web.zip` com pasta `axipesquisa/` na raiz | Anthropic instrui enviar ZIP da pasta e ativar em Personalizar > Habilidades. **Não testado na conta.** |
| Codex CLI/IDE | Extrair `dist/axipesquisa-2.2.2-codex.zip` para `.agents/skills/axipesquisa/SKILL.md` | Pasta do projeto, não upload direto de ZIP. Consulte a documentação do Codex. |
| Antigravity IDE/CLI | Extrair `dist/axipesquisa-2.2.2-antigravity.zip` para `.agents/skills/axipesquisa/SKILL.md` | Escopo global documentado: `~/.gemini/config/skills/axipesquisa/`. |
| Grok Build CLI | Extrair `dist/axipesquisa-2.2.2-grok-build-cli.zip` para `.grok/skills/axipesquisa/SKILL.md` | Escopo global documentado: `~/.grok/skills/axipesquisa/`. |
| Claude Code | Extrair `dist/axipesquisa-2.2.2-claude-code.zip` para `.claude/skills/axipesquisa/SKILL.md` | Escopo global documentado: `~/.claude/skills/axipesquisa/`. |

## Instalação local (exemplos)

```bash
# Codex
unzip dist/axipesquisa-2.2.2-codex.zip -d /caminho/do/projeto
# Antigravity
unzip dist/axipesquisa-2.2.2-antigravity.zip -d /caminho/do/projeto
# Grok Build
unzip dist/axipesquisa-2.2.2-grok-build-cli.zip -d /caminho/do/projeto
# Claude Code
unzip dist/axipesquisa-2.2.2-claude-code.zip -d /caminho/do/projeto
```

Para plataformas web, consulte a UI em sua conta, não use a presença do ZIP como prova de aceite. Quando uma plataforma disser que não suporta importação, use as instruções personalizadas, se existirem, ou ajuste a variante conforme a documentação.

## Fontes oficiais para rotas de instalação

- Agent Skills: https://agentskills.io/specification
- OpenAI ChatGPT: https://help.openai.com/pt-br/articles/20001066-skills-in-chatgpt
- Gemini Web: https://support.google.com/gemini/answer/17094296?hl=pt-br
- Grok Web: https://x.ai/news/grok-skills
- Claude Web: https://support.claude.com/pt/articles/12512198-como-criar-habilidades-personalizadas
- OpenAI Codex: https://learn.chatgpt.com/docs/build-skills
- Antigravity: https://antigravity.google/docs/skills?app=antigravity-ide
- Grok Build: https://docs.x.ai/build/features/skills-plugins-marketplaces
- Claude Code: https://code.claude.com/docs/en/skills

Estas páginas podem mudar. Antes de proclamar compatibilidade final, executar importação e cenários adversariais em cada produto.

## Correção do ChatGPT Web em 04/11/2026

Consulte `COMPATIBILIDADE-CHATGPT-2026.md`. O ChatGPT permite upload individual de Skill em contas elegíveis, por meio de Plugins > Skills. A distribuição pública via diretório exige pacote de Plugin separado, com `plugin.json`, validação e elegibilidade. O ZIP de Plugin desta versão é **candidato não submetido**.
