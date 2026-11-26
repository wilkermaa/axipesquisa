# AGENTS.md — regras obrigatórias para agentes que desenvolvem AXI Pesquisa

<!-- DEC-OPI-006:BEGIN -->
## Normas vigentes — DEC-OPI-006 (26/11/2026)

Por decisão expressa do proponente, este repositório adota documentalmente [OPI 0.4.0](https://github.com/wilkermaa/principio-da-obrigatoriedade-proporcional-e-Intencional-OPI/blob/c654f2706ded68e502cc58886400e96f5433babb/OPI-001-v0.4.0.md) · [PDI 0.4.0](https://github.com/wilkermaa/politica-de-criacao-de-issues/blob/269074a95d7d5cca3da94f677078d96e023d64c5/politica/POLITICA-ISSUES-v0.4.0.md) · [PEAP 0.3.0](https://github.com/wilkermaa/politica-de-criacao-de-eap/blob/487b4596a7842cfcaea06e1dec2c6f93d91553b3/PEAP-001-v0.3.0.md) · [PECDI 1.3.0](https://github.com/wilkermaa/politica-de-execucao-continua-de-issues/blob/f3e8874dea6f8aac1177a40bbd9862cb15436f12/politica/PECDI-001-POLITICA-EXECUCAO-CONTINUA-DE-ISSUES-v1.3.0.md) · [PPSI 0.4.0](https://github.com/wilkermaa/politica-de-prototipacao/blob/20d1faba5f24f859834f44d431be34ff940ccaf8/PPSI-001-v0.4.0.md) nas competências pertinentes. Aplicar [AGENTS-BASE](https://github.com/wilkermaa/principio-da-obrigatoriedade-proporcional-e-Intencional-OPI/blob/c654f2706ded68e502cc58886400e96f5433babb/AGENTS-BASE.md) subordinado às normas e instruções locais. OPI-CICLO-01: para obra/parte verificável fundamentada em AXI, AXI → GDARC completo → REDTEAM → GDARC completo; corrigir localmente, verificar regressões e encerrar por suficiência. PDI: seis ciclos nas partes 1–6, conectados pelo ECC, mantendo 0/7 e DoR/RoR/DoD. Consultas sem obra não exigem o ciclo. Preservar WIP=1, G0–G7, fila, autoridades, segurança, escopo e instruções locais aplicáveis; esta decisão prevalece apenas quanto à atualização normativa aprovada. Não alterar baselines de entregas aceitas nem reabrir trabalho; reconciliar rodadas/perfis no próximo G0/ponto seguro, sem despacho automático. Não duplicar evidências, gates, relatórios ou aprovações humanas. Registrar resultado e evidência proporcional; autorrevisão não substitui revisão independente. Adoção documental não prova aplicação, instalação de agentes nem ganho humano.
<!-- DEC-OPI-006:END -->


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