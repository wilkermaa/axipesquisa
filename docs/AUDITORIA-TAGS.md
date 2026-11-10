# Auditoria das tags históricas — AXI Pesquisa
**Data da consulta:** 10/11/2026 · **Fonte de verificação:** referências Git, objetos de tag anotados, árvore de cada commit e catálogo de Releases do repositório `wilkermaa/axipesquisa`.

## Resultado

Foram verificadas **oito tags anotadas** com referências distintas a **oito commits históricos diferentes**. Todos os oito Releases já existem. Em 10/11/2026, o Release `v2.2.2` possuía oito assets ZIP e os outros sete não possuíam assets de instaladores. A árvore de cada commit foi inspecionada. Não foi realizada comparação byte a byte entre todas as pastas do Drive e as tags, e as tags não são cópia do estado contemporâneo de `main`.

| Tag | Commit imutável associado | Entradas da árvore | Observação | Assets em 10/11 |
|---|---|---:|---|---:|
| [v1.0](https://github.com/wilkermaa/axipesquisa/releases/tag/v1.0) | [`854246c3d769`](https://github.com/wilkermaa/axipesquisa/commit/854246c3d769ff96f74fc16995cabb178ccf1d21) | 8 | Registro documental parcial; não há instalador completo no snapshot | 0 |
| [v2.0.0](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.0.0) | [`74367d9e8b09`](https://github.com/wilkermaa/axipesquisa/commit/74367d9e8b09e3d360d7ff1633b75a2befcdfbe5) | 31 | Oito ZIPs históricos em pacotes/; requer auditoria de informações pessoais antes de distribuir | 0 |
| [v2.1.0-rc1](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.1.0-rc1) | [`4e89378bf050`](https://github.com/wilkermaa/axipesquisa/commit/4e89378bf050f69f46d477216e39876dc20adbee) | 15 | Registro documental parcial; não há instalador completo no snapshot | 0 |
| [v2.2.0-rc2](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.0-rc2) | [`db8094f6fee5`](https://github.com/wilkermaa/axipesquisa/commit/db8094f6fee5799af9f25974c7d15b15133a88b5) | 53 | Fonte com builder para oito IA; benchmark C2 permanece congelado | 0 |
| [v2.2.0-rc3](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.0-rc3) | [`aa26d5de121e`](https://github.com/wilkermaa/axipesquisa/commit/aa26d5de121ea9c90dd5dd050f46e2cf39e95760) | 62 | Fonte com builder para oito IA | 0 |
| [v2.2.0-rc4](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.0-rc4) | [`15eb567f7939`](https://github.com/wilkermaa/axipesquisa/commit/15eb567f7939308035f7cea7fe73514aaf78bb08) | 63 | Fonte com builder para oito IA | 0 |
| [v2.2.1](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.1) | [`ce56d499e6f4`](https://github.com/wilkermaa/axipesquisa/commit/ce56d499e6f470e1e4f77f689f70d222dc1cac00) | 64 | Fonte com builder para oito IA | 0 |
| [v2.2.2](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.2) | [`592c400fbd43`](https://github.com/wilkermaa/axipesquisa/commit/592c400fbd438b7841ba976eaeb584e6a7df0993) | 71 | Oito instaladores originais anexados ao GitHub Release | 8 |

### Inconsistências e decisões
- O identificador legado `v1.0` contém duas casas e **não** segue o formato atual `vMAJOR.MINOR.PATCH`. Preservar sem reescrever; caso se crie um alias `v1.0.0`, documentar a equivalência antes de qualquer publicação. Uma tag adicional não torna instalável conteúdo documental incompleto.
- No GitHub, `main` é o trunk corrente, enquanto tags antigas preservam árvores independentes de versões fechadas. Não deslocar refs históricos nem tratar uma pasta no Drive como tag Git publicada.
- As versões `v1.0` e `v2.1.0-rc1` documentam ausência de distribuição instalável completa. Não anexar fontes ou benchmarks fingindo que são instaladores.
- A versão `v2.0.0` possui oito ZIPs de plataforma, mas o changelog antigo alerta sobre possíveis dados pessoais; **não redistribuir como instalador público sem inspeção do conteúdo**.
- `v2.2.0-rc2` permanece condição congelada do experimento científico C2. Recriar instaladores a partir de uma tag não altera o experimento; preservar claramente essa distinção.
- Tags e Releases têm funções distintas: **tag** identifica integralmente o código e documentos versionados; **asset do Release** distribui o pacote utilizável pelo público. A presença de um asset não prova validação funcional nativa da IA.

### Próximas verificações
A automação de instalação histórica, quando executada, deverá validar a versão do builder, testes locais, integridade ZIP, licenciamento e ausência de segredos. Ela deverá **anexar assets novos, jamais sobrescrever os existentes**, preservar os Releases e produzir SHA256 para rastreabilidade. Atualizar este inventário com o resultado real de cada execução.

## Referências (ABNT)
GIT. *git-tag Documentation*. [s. d.]. Disponível em: https://git-scm.com/docs/git-tag.html. Acesso em: 10 nov. 2026.

GITHUB. *About releases*. [s. d.]. Disponível em: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases. Acesso em: 10 nov. 2026.

SEMANTIC VERSIONING. *Semantic Versioning 2.0.0*. [s. d.]. Disponível em: https://semver.org/. Acesso em: 10 nov. 2026.

---
◌ AXI · instrução personalizada - wilkermaa@gmail.com
