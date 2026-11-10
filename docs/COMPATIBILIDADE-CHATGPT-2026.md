# ChatGPT Web: Skills individuais não são Plugins públicos

**Confirmado na documentação em 04/11/2026.**

1. **Skill individual no ChatGPT Web**: em contas elegíveis Business, Enterprise, Healthcare ou Edu, a área `Plugins > Skills` permite criar/carregar Skill do computador. Disponibilidade pode ser determinada por administrações de workspace e lançamento do recurso. Não prometer para Free, Go, Plus ou Pro.
2. **Plugin distribuível no diretório**: exige `plugin.json` em raiz e `skills/axipesquisa/SKILL.md`, além de metadados, validações, identidade de desenvolvedor elegível e revisão conforme exigências. O pacote `dist/AXI-ChatGPT-Plugin-v2.2.2.zip` é um **candidato de empacotamento**, não um plugin aprovado.
3. **Alternativa geral**: fornecer instruções textuais adaptadas sem afirmar que a execução será igual à skill nativa. Plugin e Skill não necessitam de servidor MCP quando o fluxo usa apenas instruções e recursos; publicação no diretório pode ter critérios adicionais.
4. **Teste funcional não substituível por ZIP**: importar, executar prompts e verificar o comportamento na conta real.

Fontes oficiais: 
- OPENAI. *Skills no ChatGPT*. 2026. Disponível em: https://help.openai.com/pt-br/articles/20001066-skills-in-chatgpt. Acesso em: 4 nov. 2026.
- OPENAI. *Package your plugin*. [s.d.]. Disponível em: https://developers.openai.com/plugins/build/plugins. Acesso em: 4 nov. 2026.
- OPENAI. *Upload and submit your plugin*. [s.d.]. Disponível em: https://developers.openai.com/plugins/deploy/submission. Acesso em: 4 nov. 2026.
- OPENAI. *Plugin submission errors*. [s.d.]. Disponível em: https://developers.openai.com/plugins/deploy/submission-errors. Acesso em: 4 nov. 2026.
