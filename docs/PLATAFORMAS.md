# Plataformas: instalação e matriz A/I (v2.4.0) — revisto em 19/11/2026

Esta é a documentação de **caminhos de distribuição e renderização visual (Fase A: Markmap Tree + Cards; Fase I: Mermaid/fluxo)**. A leitura de documentação pública não representa teste de importação em conta do usuário, nem comprova suporte nativo universal de Markmap em todas as interfaces. Pacotes em `dist/` são produzidos por `python scripts/build.py`.

| Ambiente | Instalação/extração proposta | Rota Fase A (Markmap Tree + Cards) e Fase I (Mermaid/Fluxo) + Status |
|---|---|---|
| ChatGPT Web | `dist/axipesquisa-2.4.0-chatgpt-web.zip` com pasta `axipesquisa/SKILL.md` | Disponibilidade depende da conta/workspace. **Skill individual é diferente de Plugin de diretório.** **Fase A:** Markmap `tree`+`cards` em prévia se disponível; fallback visual equivalente (SVG/PNG/Mermaid em prévia). **Fase I:** Mermaid renderizado em prévia. Sem suporte nativo de Markmap comprovado. **Não testado em conta real.** |
| Gemini Web | `dist/axipesquisa-2.4.0-gemini-web.zip` com `SKILL.md` na raiz do ZIP e recursos ao lado | Google aceita `SKILL.md`, pasta ou ZIP na pasta principal. **Fase A:** Markmap se acionável na sessão; fallback prioritário por **geração direta de imagem** estática (SVG renderizado ou PNG) esquerda→direita. **Fase I:** geração direta de imagem SVG/PNG com prévia na conversa. **Não gerar HTML/app interativo, tabela ou ASCII como entrega**; Canvas é incompatível com Skills segundo ajuda do Google e só conta se abrir figura real. **Não testado em conta real.** |
| Grok Web | `dist/axipesquisa-2.4.0-grok-web.zip` com `SKILL.md` na raiz e arquivo individual no repositório | xAI cria Skills por conversa/arquivo; aceitação específica de ZIP não confirmada. Alternativa: texto do `SKILL.md`. **Fase A e I:** Markmap na A quando disponível; rota visual real via **SVG em cartão com prévia inline** ou **Projects HTML Preview** estático. **Não testado no ambiente real.** |
| Claude Web | `dist/axipesquisa-2.4.0-claude-web.zip` com pasta `axipesquisa/` na raiz | Anthropic instrui enviar ZIP da pasta e ativar em Personalizar > Habilidades. **Fase A e I:** Markmap se disponível na A; rota principal via **visual personalizado HTML/SVG inline** ou **Artifact com prévia renderizada**, sem exigir app interativo. **Não testado na conta.** |
| Codex CLI/IDE | Extrair `dist/axipesquisa-2.4.0-codex.zip` para `.agents/skills/axipesquisa/SKILL.md` | Pasta do projeto, não upload direto de ZIP. **Fase A e I:** Markmap/Mermaid/SVG/PNG em visualizador ou prévia local realmente aberta; em terminal puro sem figura visível, registrar **`ENTREGA PARCIAL`**. |
| Antigravity IDE/CLI | Extrair `dist/axipesquisa-2.4.0-antigravity.zip` para `.agents/skills/axipesquisa/SKILL.md` | Escopo global documentado: `~/.gemini/config/skills/axipesquisa/`. **Fase A e I:** Markmap/Mermaid se disponível ou SVG/PNG local exibido/inspecionado inline na IDE (prévia aberta); sem exibição visual, registrar `ENTREGA PARCIAL`. |
| Grok Build CLI | Extrair `dist/axipesquisa-2.4.0-grok-build-cli.zip` para `.grok/skills/axipesquisa/SKILL.md` | Escopo global documentado: `~/.grok/skills/axipesquisa/`. **Fase A e I:** renderer visual local para Markmap/Mermaid ou SVG/PNG em prévia aberta; terminal sem imagem = `ENTREGA PARCIAL`. |
| Claude Code | Extrair `dist/axipesquisa-2.4.0-claude-code.zip` para `.claude/skills/axipesquisa/SKILL.md` | Escopo global documentado: `~/.claude/skills/axipesquisa/`. **Fase A e I:** Markmap/HTML/SVG/PNG local em visualizador da IDE com prévia aberta; arquivo em disco sem visualização não conclui entrega visual. |

**Todos os oito ZIPs v2.4.0 incluem `INSTALADOR-PLATAFORMA.md` específico**, `references/ROTEAMENTO-VISUAL-ANALISE.md` (Fase A) e o fluxo integral `references/FLUXO-LEITURA-INTEGRAL.md`. **Não exigir aplicativo interativo nem instalação de dependências externas por padrão.** **Privacidade:** nunca enviar dados privados ou sigilosos para renderizadores públicos externos sem autorização.

**Aceite para todos os ambientes (A e I):** hierarquia fiel na **fase A** e processo representável na **fase I** exigem **imagem do diagrama visível na tela ou prévia realmente aberta**. Produção de arquivo local sem exibição/prévia, snippet de código Markdown/YAML/Mermaid/SVG, tabela ou ASCII não concluem a entrega visual; registrar **`ENTREGA PARCIAL — MAPA VISUAL NÃO EXIBIDO`** (A) ou **`ENTREGA PARCIAL`** (I) com a limitação observada. PDF e download são opcionais. Não impor diagrama em conteúdo sem hierarquia (A) ou sem fluxo (I).

## Instalação local (exemplos)

```bash
# Codex
unzip dist/axipesquisa-2.4.0-codex.zip -d /caminho/do/projeto
# Antigravity
unzip dist/axipesquisa-2.4.0-antigravity.zip -d /caminho/do/projeto
# Grok Build
unzip dist/axipesquisa-2.4.0-grok-build-cli.zip -d /caminho/do/projeto
# Claude Code
unzip dist/axipesquisa-2.4.0-claude-code.zip -d /caminho/do/projeto
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
