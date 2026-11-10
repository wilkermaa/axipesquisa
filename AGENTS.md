# AGENTS.md — regras obrigatórias para agentes que desenvolvem AXI Pesquisa

Antes de alterar a Skill, código, documentação, pesquisa, instaladores ou criar versões, **leia integralmente [POLITICA-ORGANIZACIONAL.md](POLITICA-ORGANIZACIONAL.md)**. Esta instrução se aplica a Codex, Antigravity, Claude Code, outros agentes e colaboradores.

## Regras de operação

1. **Trunk:** trabalhar na branch padrão GitHub `main` (trunk operacional) e no `AXI-Pesquisa/trunk/` do Drive. Não confundir snapshots de versões com a área de desenvolvimento.
2. **Tags:** fechar versão com três casas `vMAJOR.MINOR.PATCH`, tag Git anotada no commit integral do release e snapshot congelado correspondente no Drive. MAJOR = mudança grande/incompatível; MINOR = nova funcionalidade compatível; PATCH = correção. Não mover ou sobrescrever tags.
3. **Antes de lançar:** validar fonte, changelog, integridade, licença, hashes e testes que realmente possam ser executados. Não criar tags históricas apontando arbitrariamente para HEAD atual.
4. **Downloads:** disponibilizar instaladores separados por plataforma (GPT/ChatGPT, Grok, Gemini, Claude, Antigravity, Codex, Claude Code, Grok Build e demais compatíveis) e por versão, preferencialmente em GitHub Releases. Não apresentar ZIP de código, benchmark ou estudo como instalador.
5. **Método:** preservar as fases A (analisar o todo e suas partes), X (expandir com comparações delimitadas) e I (integrar relações, movimentos, funcionamento e aplicação).
6. **Fundamentação:** atribuir Descartes, Erin Meyer, Wilker (AXI/o todo e suas partes) e Robert Dilts conforme sua contribuição efetiva. Dilts/PNL é referência conceitual, não validação científica comprovada da Skill.
7. **Pesquisa:** separar hipótese, avaliação, execução efetiva e resultados. Preservar C2 v2.2.0-rc2 congelada no protocolo anterior; não declarar superioridade antecipada.
8. **Colaboração:** registrar ator, papel, proposta, revisão, decisões, evidências, fontes, limitações e, quando aplicável, resultado de avaliações humanas independentes.
9. **Mudanças mínimas:** preservar comportamento existente, examinar impactos, testar o que for possível e distinguir explicitamente executado, não testado e pendente.
10. **Fechamento:** informar versão, arquivos modificados, integridade dos downloads, tags e releases realmente publicados, testes realizados e pendências. **O mero commit de documentação no trunk não equivale a release fechado.**

Se a política conflitar com instruções hierarquicamente superiores ou limitações de ferramentas, respeitar as superiores e registrar o bloqueio. Não afirmar que controles automáticos de CI/branch protection foram instalados sem confirmação.

**Fonte canônica de governança:** [POLITICA-ORGANIZACIONAL.md](POLITICA-ORGANIZACIONAL.md).