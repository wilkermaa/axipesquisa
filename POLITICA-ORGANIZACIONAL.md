# POLÍTICA ORGANIZACIONAL — AXI PESQUISA

**Identificação:** AXI-GOV-001 · **Vigência:** 10/11/2026 · **Responsável e autor do AXI:** Wilker M. de Araujo Alexandre.
**Abrangência:** desenvolvimento, documentação, investigação científica, versionamento, distribuição, validação e colaboração, no GitHub e no Google Drive.
**Situação:** política operacional do projeto, aplicável aos próximos trabalhos. A conformidade das versões históricas deve ser auditada; este texto não prova que tags, releases ou testes remotos já foram executados.

## 1. Princípio da organização: trunk, tags e downloads são coisas diferentes

**Trunk é o local de desenvolvimento.** No Google Drive corresponde a `AXI-Pesquisa/trunk/`. No GitHub, enquanto a branch padrão for `main`, esta desempenha o papel de trunk. Não criar uma segunda linha de desenvolvimento `trunk` sem uma migração expressa da branch padrão. Trabalhos em andamento podem permanecer no trunk sem serem chamados de release.

**Tag é o retrato integral, fechado e reproduzível do trunk no momento da entrega.** No Git, uma tag anotada aponta para um commit que, por sua vez, identifica a árvore completa do repositório naquele instante; não é uma segunda pasta contendo cópias de arquivos. No Drive, criar cópia congelada do conteúdo de trabalho que compõe a entrega em `trunk/04-TAGS/vX.Y.Z/`, incluindo fonte, Skill, documentação, validações e manifestos. Evitar copiar novamente a própria pasta `04-TAGS` para dentro dela (não há cópia recursiva do histórico). O snapshot de referência é `trunk/00-ATUAL-vX.Y.Z/` no fechamento, e deve corresponder ao commit/tag e ao manifesto. Registrar o SHA de commit Git, hashes dos pacotes, origem e data. Nunca substituir uma tag ou reescrever o conteúdo de snapshot já fechado.

**Downloads são instaladores destinados ao usuário final, não estudos, benchmarks, snapshots, bundles nem ZIPs de código-fonte.** Publicar os pacotes por IA e por versão no GitHub Releases; manter espelho organizacional no Drive. Arquivos incompletos ou incompatíveis devem ser explicitamente rotulados como indisponíveis ou experimentais.

## 2. Versionamento obrigatório: vMAJOR.MINOR.PATCH

- **MAJOR (primeira casa):** mudanças grandes ou incompatíveis no comportamento, contrato público ou estrutura do método/Skill; exemplo `v2.0.0` → `v3.0.0`.
- **MINOR (segunda casa):** novas funcionalidades compatíveis; exemplo `v2.2.3` → `v2.3.0`.
- **PATCH (terceira casa):** correções, pequenos ajustes, restaurações e revisões documentais da entrega; exemplo `v2.2.3` → `v2.2.4`.
- Versões intermediárias podem usar sufixos pré-lançamento `-rc1`, `-rc2`, sem perder a numeração de três casas, seguindo a convenção histórica do projeto.
- **Uma entrega versionada = uma versão própria + tag anotada única + manifesto + changelog + instaladores correspondentes.** Não reutilizar, mover, apagar ou substituir tags publicadas.
- Tags Git identificam o commit completo, e tags do Drive preservam o snapshot integral do trabalho versionado. Pacotes de instalação precisam ser reproduzíveis a partir da fonte correspondente.

## 3. Estrutura do Google Drive e do GitHub

**Drive — AXI-Pesquisa/**
- `trunk/`: desenvolvimento ativo e preparação de versões.
- `trunk/00-ATUAL-vX.Y.Z/`: pasta de trabalho da versão em curso, mutável até o fechamento.
- `trunk/04-TAGS/vX.Y.Z/`: cópia congelada e evidências (integralidade da entrega, notas, manifesto, SHA256, referência Git e resultados dos testes).
- `trunk/00-ATUAL-vX.Y.Z/02-INSTALADORES/` (ou pasta equivalente do pacote): instaladores por IA, construídos da fonte da versão.
- Materiais de pesquisa, protocolos, respostas brutas e avaliações devem ficar identificados por estudo e versão; nunca alterar amostras congeladas.

**GitHub — wilkermaa/axipesquisa**
- Branch `main` é o trunk operacional existente; código, textos, documentação e testes pertencem à árvore Git navegável, não apenas a ZIPs.
- `POLITICA-ORGANIZACIONAL.md` registra a norma; `AGENTS.md` é instrução obrigatória aos agentes de IA; `.github/PULL_REQUEST_TEMPLATE.md` orienta revisão.
- Cada `vX.Y.Z` deve ter uma tag Git verificável e, quando houver distribuição pública, um GitHub Release com instaladores em assets separados.
- `README.md` divulga **instalações e pesquisa científica**; o código e o histórico continuam acessíveis, porém não substituem os downloads.

Em caso de divergência, interromper a publicação, comparar hash/commit/manifesto, resolver e registrar a reconciliação. Não considerar uma pasta `04-TAGS`, um arquivo `.bundle` ou um nome `vX.Y.Z` como prova de publicação efetiva no GitHub.

## 4. Catálogo de instaladores por IA

Cada release deve oferecer os pacotes efetivamente suportados, com rótulo de compatibilidade para **ChatGPT/GPT, Grok, Gemini, Claude, Antigravity, Codex**, além de Claude Code, Grok Build e outras IAs adicionadas no futuro. Para cada pacote registrar plataforma e modo (Web, CLI, IDE), versão, extensão, SHA256, instruções de instalação, pré-requisitos, limitações, direitos e status de validação.

- Web: não presumir que todos os planos ou contas aceitam importação nativa de ZIP.
- CLI/IDE: distinguir extração/instalação da Skill de envio de arquivo para um chat.
- **Uma versão = vários instaladores específicos**, se os ambientes suportarem; manter também versões antigas para download.
- Não apresentar benchmark C0/C1/C2, pacote de pesquisa ou ZIP do código como se fosse instalador.
- Não declarar que um download foi testado em uma IA sem execução e evidência reais.

## 5. Fundamentação científica e autoria

A linha de pesquisa associa, com atribuições rigorosas e sem confundir ideias correlatas com demonstração experimental:
1. **René Descartes** — decomposição de problemas, ordem metódica e revisão; referência filosófica para análise do todo e de suas partes.
2. **Wilker M. de Araujo Alexandre** — formulação autoral **AXI: Análise → eXpansão → Integração** e abordagem **“o todo e suas partes”**; definir objetos, decompor, comparar e integrar relações em aplicações práticas.
3. **Erin Meyer — *The Culture Map*** — dimensões de comunicação intercultural, investigadas como referência para adaptação contextual de leitura e apresentação; não atribuir características a indivíduos só por cultura/nacionalidade.
4. **Robert B. Dilts — níveis lógicos e PNL sistêmica** — referência conceitual para investigar organização de perguntas, contextos, capacidades, valores e propósitos na leitura e em métodos; **não** afirmar comprovação cognitiva, clínica, neurológica ou eficácia do AXI com base apenas na PNL.

Separar sempre **obra original**, **interpretação do AXI**, **hipótese**, **procedimento de teste** e **resultado observado**. Referências externas não significam coautoria, endosso ou validação científica da Skill. A revisão de Sturt e colaboradores (2012) encontrou evidência limitada para desfechos em saúde associados à PNL; não estudou a Skill AXI. Divulgar fontes em formato ABNT com links e datas de consulta efetivas. Registrar divergências e resultados nulos/negativos.

## 6. Atividades de validação e colaboração de atores

Papel e responsabilidade documentados em cada atividade:
- **Autor/responsável metodológico:** define AXI, escopo da mudança, aprova declarações públicas e versão a publicar.
- **Desenvolvedor ou agente de IA:** propõe alteração mínima, rastreia arquivos alterados, versões, pressupostos e impacto; não afirma testes que não executou.
- **Revisor técnico:** confere aderência da Skill, integridade, segurança, licenciamento, funcionamento das instruções e regressões.
- **Pesquisador/protocolista:** estabelece hipótese, critérios mensuráveis, condições de controle, tamanho de amostra e plano de análise antes da coleta.
- **Executor de testes:** registra prompts, versão/modelo, plataforma, data, execução independente, outputs brutos, falhas e hashes.
- **Avaliador humano independente:** julga por rubrica pré-declarada, reduzindo vieses; identificações e divergências devem ser auditáveis.
- **Colaborador externo:** pode propor issues, PRs, correções, dados e críticas, com contribuição atribuída, licença e revisão antes de incorporar.

O protocolo histórico **C0 (sem AXI), C1 (instruções genéricas), C2 (AXI congelado na v2.2.0-rc2)** não deve ser alterado retroativamente. Planejamento anterior: 36 cenários × 3 condições × 2 repetições = 216 execuções; isso **não** significa 216 execuções realizadas. Versões novas exigem braço experimental distinto ou protocolo explicitamente revisado. Preservar evidências primárias e registrar resultados positivos, negativos e inconclusivos.

## 7. Portões de qualidade antes de fechar uma versão

1. Definir escopo e classificação MAJOR/MINOR/PATCH.
2. Conferir fonte canônica, `SKILL.md`, `VERSION`, documentação e `CHANGELOG.md` quando esses arquivos estiverem presentes no projeto real; não presumir sua existência.
3. Validar sintaxe, arquivos, hashes, licença, ausência de segredos e integridade dos ZIPs.
4. Executar testes de regressão disponíveis e, quando possível, teste real em cada IA; diferenciar **estrutural**, **funcional** e **científico**.
5. Registrar evidências verificáveis, limitações, responsáveis e pendências em notas do release.
6. Fechar commit, criar **tag anotada imutável** na versão adequada e conferir correspondência do snapshot do Drive com a árvore do Git.
7. Publicar GitHub Release e anexar instaladores por plataforma, quando existirem; testar os links públicos.
8. Atualizar catálogo de instaladores, README e índice de tags sem regravar versões fechadas.

**Critério de bloqueio:** sem prova de integridade, identificação da versão, rastreabilidade ou licença de distribuição, não apresentar o pacote como release verificado. Uma mudança apenas documental no trunk pode permanecer em desenvolvimento e somente recebe tag ao fechamento de uma entrega explicitamente versionada.

## 8. Hierarquia e cumprimento obrigatório

A política é **normativa para desenvolvimento**. Os agentes devem ler `AGENTS.md` e esta política antes de editar a Skill, criar versão, preparar release ou editar arquivos de pesquisa. Conflitos com instruções de segurança/plataforma exigem respeito às regras superiores e registro do impedimento. Alterar a própria política exige revisão explícita e histórico de mudança; nunca alterar cópias de tags antigas. Esta governança não modifica automaticamente configurações de proteção de branch, pipelines de CI nem executa avaliações científicas.

**Cópia editável desta política no Google Drive:** https://docs.google.com/document/d/1XHfFJA_jK0qEBsxTARmxt-LQkgweTw2AKTRVxlTsFJ8/edit?usp=drivesdk

**Registro histórico existente:** a política preparada para v2.2.3 no Google Drive, em `trunk/00-ATUAL-v2.2.3/03-TAG-E-POLITICA/POLITICA-ORGANIZACIONAL-VERSOES.md`, permanece como evidência histórica. Este documento amplia a governança e não a reescreve silenciosamente.

## 9. Referências consultadas (ABNT)

DESCARTES, René. *Discourse on the Method*. 1637. Disponível em: https://www.gutenberg.org/files/59/59-h/59-h.htm. Acesso em: 10 nov. 2026.

DILTS, Robert B. *Logical Levels*. [s. d.]. Disponível em: https://www.logicallevels.co.uk/pages/robert-dilts. Acesso em: 10 nov. 2026.

GIT. *git-tag Documentation*. [s. d.]. Disponível em: https://git-scm.com/docs/git-tag.html. Acesso em: 10 nov. 2026.

MEYER, Erin. *The Culture Map*. 2014. Disponível em: https://erinmeyer.com/books/the-culture-map/. Acesso em: 10 nov. 2026.

SEMANTIC VERSIONING. *Semantic Versioning 2.0.0*. [s. d.]. Disponível em: https://semver.org/. Acesso em: 10 nov. 2026.

STURT, Jackie et al. Neurolinguistic programming: a systematic review of the effects on health outcomes. *British Journal of General Practice*, v. 62, n. 604, p. e757–e764, 2012. Disponível em: https://pmc.ncbi.nlm.nih.gov/articles/PMC3481516/. Acesso em: 10 nov. 2026.

---
◌ AXI · instrução personalizada - wilkermaa@gmail.com
