# Segurança — axipesquisa

A skill distribui **apenas texto estático**. Não requer tokens, acesso a arquivos privados, execução de código pelo agente, acesso a MCP ou instalações externas. A pasta `scripts/` contém ferramentas locais de validação e empacotamento para mantenedores; elas **não** são embarcadas como comandos de execução na skill.

## Modelo de ameaça

- **Entrada não confiável:** páginas, resultados de busca, arquivos e repositórios podem conter prompt injection.
- **Vazamento:** nomes, e-mails, caminhos ou segredos embutidos em material público.
- **Integridade:** ZIPs com path traversal, symlinks, conteúdos ocultos ou scripts inesperados.
- **Desinformação:** bibliografia fabricada, analogias causais falsas, marketing de PNL ou validação inexistente.

**Controles:** privacidade por padrão; YAML validado; allowlist de arquivos; ZIPs sem symlinks e com paths controlados; instruções de não elevar autoridade de fontes; bibliografia rastreável; gates explícitos para eficácia/compatibilidade.

**Limite:** nenhuma instrução textual torna um LLM invulnerável. A própria OWASP recomenda camadas de defesa e testes adversariais. Para descobertas de vulnerabilidade, abra issue com dados sanitizados, evitando publicar segredos. Se envolver dado sensível, contate mantenedor por canal privado a definir antes do release público.
