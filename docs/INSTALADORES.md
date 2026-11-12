# Instaladores AXI — catálogo público

**Objetivo:** oferecer pacotes destinados à instalação da Skill AXI, e não pacotes de código, fotografias do repositório ou arquivos de benchmark. Autor: Wilker M. de Araujo Alexandre.

## Versão v2.3.9 — REPROVADA; não instalar como versão oficial

**DECISÃO DO AUTOR (12/11/2026): REPROVADA / NÃO HOMOLOGADA.** Não recomendar para instalação ou uso oficial. Os oito ZIPs, o release e a tag são preservados como acervo histórico; a existência dos downloads não significa aprovação. A versão oficial recomendada continua **v2.3.8**. [Registro da decisão — Issue #15](https://github.com/wilkermaa/axipesquisa/issues/15).

### Descrição histórica — Gemini minimalista, caixas apenas com títulos

Preserva a **imagem de fluxograma obrigatória** e estabelece, especificamente no Gemini, **caixas SOMENTE COM TÍTULOS CURTOS, SEM ÍCONES NEM DESCRIÇÕES**, estilo visual simples do Mermaid. Apenas setas, decisões e rótulos breves; detalhes jurídicos e ABNT fora da imagem. [Release v2.3.9](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.9). Homologação no Gemini e espelhamento Drive sujeitos a evidência.

## Versão v2.3.8 — IMAGEM OBRIGATÓRIA na microfase I

A Skill deve mostrar **imagem de fluxograma realmente visível na resposta ou em prévia aberta** quando houver fluxo representável. No Gemini, o instalador prioriza **geração direta de imagem SVG renderizado/PNG**, não aplicativo HTML/Canvas como primeira opção; tabela, ASCII, código ou arquivo sem prévia são falha/entrega parcial. ChatGPT mantém Mermaid com prévia, Claude/Grok seus recursos visuais. Testes de fonte e empacotamento não comprovam suporte do Gemini à chamada de Imagens com Skill ativa. [Release v2.3.8](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.8). Homologação na Issue #4, Drive Issue #6.

## Versão v2.3.7 — Canvas como ferramenta de saída para Prévia SVG

A Skill AXI no Gemini **não precisa funcionar dentro do Canvas**: ela prepara o fluxograma e deve **solicitar/acionar o Canvas para construir SVG inline e abrir a Prévia**. A chamada ainda requer teste funcional, pois a ajuda oficial Google informa que Canvas não funciona com Skills; não declarar sucesso sem retorno observável. Preservados ABNT, leitura integral e roteamento das outras IAs. O ZIP Gemini v2.3.7 inclui guia específico. [Release v2.3.7](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.7). Homologação na interface e espelhamento Drive pendentes.

## Versão v2.3.6 — leitura integral AXI e rotas visuais específicas

Restaura a instrução fundamental de leitura completa **arquivo por arquivo, em A → X → I**, ABNT em todas as explicações/pesquisas e comparações da v2.0.0. Cada um dos **oito ZIPs** contém **`INSTALADOR-PLATAFORMA.md` específico**: Gemini = Canvas com SVG e prévia (bloqueio Skills+Canvas registrado, alternativa SVG real se possível), ChatGPT = Mermaid renderizado, Claude = visual HTML/SVG inline/Artifact, Grok = SVG inline/Projects Preview e orientações próprias para as quatro CLIs. **Sem homologação funcional de interface**. [Release v2.3.6](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.6).

## Versão v2.3.5
 — pesquisa jurídica, citações ABNT e visual preservados

PATCH para restaurar o portão de pesquisa legal e fontes verificáveis em ABNT **sem enfraquecer a renderização**. Exige distinguir regras locais por artigos; casos sem consulta são preliminares e declarados. [Release v2.3.5](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.5). Instalações continuam sujeitas a testes reais nas oito IAs; espelho do Drive pendente de verificação.

## Versão v2.3.4 — SVG em prévia no Gemini, com fallback visual

Correção PATCH específica da microfase I no Gemini: **acionar e verificar a visualização**, priorizando SVG realmente renderizado quando disponível; fallback PNG/visual nativo. Um snippet Mermaid/SVG sem figura é falha. [Release v2.3.4](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.4). Os oito instaladores são gerados e anexados pelo fluxo de publicação após CI aprovado. A homologação real das interfaces permanece pendente.

## Versão v2.3.3 — diagrama visual real; PDF opcional

A correção PATCH documenta a obrigatoriedade de uma **ação concreta de renderização** na microfase I, sem obrigatoriedade de PDF/arquivo quando a imagem já é exibida na tela. [Release v2.3.3](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.3). A homologação real permanece pendente.

## Versão v2.3.2 — Gestão e Coordenação visual da microfase I

Oito instaladores da correção estão previstos na [release v2.3.2](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.2). A IA executora seleciona autonomamente o meio gráfico; ainda não existe homologação completa nas oito IAs.

## Versão v2.3.1 — Diagramação do Fluxo de Aplicação

Consulte os anexos da [release v2.3.1](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.1) após a publicação.

## Versão v2.3.0 — roteamento visual

Oito instaladores estão disponíveis na [release v2.3.0](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.3.0). O teste de aceite nas oito IAs continua pendente.

| Plataforma | Nome esperado do ZIP |
|---|---|
| ChatGPT Web | `01-CHATGPT-WEB-AXI-v2.3.0.zip` |
| Gemini Web | `02-GEMINI-WEB-AXI-v2.3.0.zip` |
| Claude Web | `03-CLAUDE-WEB-AXI-v2.3.0.zip` |
| Grok Web | `04-GROK-WEB-AXI-v2.3.0.zip` |
| Codex | `05-CODEX-AXI-v2.3.0.zip` |
| Claude Code | `06-CLAUDE-CODE-AXI-v2.3.0.zip` |
| Antigravity | `07-ANTIGRAVITY-AXI-v2.3.0.zip` |
| Grok Build | `08-GROK-BUILD-AXI-v2.3.0.zip` |

## Versão v2.2.3 — instaladores históricos

| Plataforma | Instalador |
|---|---|
| ChatGPT Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.3/01-CHATGPT-WEB-AXI-v2.2.3.zip) |
| Gemini Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.3/02-GEMINI-WEB-AXI-v2.2.3.zip) |
| Claude Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.3/03-CLAUDE-WEB-AXI-v2.2.3.zip) |
| Grok Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.3/04-GROK-WEB-AXI-v2.2.3.zip) |
| Codex | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.3/05-CODEX-AXI-v2.2.3.zip) |
| Claude Code | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.3/06-CLAUDE-CODE-AXI-v2.2.3.zip) |
| Antigravity | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.3/07-ANTIGRAVITY-AXI-v2.2.3.zip) |
| Grok Build | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.3/08-GROK-BUILD-AXI-v2.2.3.zip) |

Os oito arquivos são publicados como assets do GitHub Release `v2.2.3`; os controles científicos permanecem congelados na v2.2.0-rc2. Testes estruturais não substituem ensaios nas interfaces Web.

## Versão v2.2.2 — downloads diretos

| Plataforma | Instalador v2.2.2 |
|---|---|
| ChatGPT Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.2/01-CHATGPT-WEB-AXI-v2.2.2.zip) |
| Gemini Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.2/02-GEMINI-WEB-AXI-v2.2.2.zip) |
| Claude Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.2/03-CLAUDE-WEB-AXI-v2.2.2.zip) |
| Grok Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.2/04-GROK-WEB-AXI-v2.2.2.zip) |
| Codex | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.2/05-CODEX-AXI-v2.2.2.zip) |
| Claude Code | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.2/06-CLAUDE-CODE-AXI-v2.2.2.zip) |
| Antigravity | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.2/07-ANTIGRAVITY-AXI-v2.2.2.zip) |
| Grok Build | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.2/08-GROK-BUILD-AXI-v2.2.2.zip) |

Estes oito arquivos estão publicados como assets do GitHub Release v2.2.2. A existência de um ZIP não comprova que cada serviço Web tenha um mecanismo de importação de Skills habilitado para todas as contas; consulte os recursos disponíveis em sua plataforma. Para ambientes CLI/IDE, normalmente é necessário extrair o conteúdo no local apropriado. Consulte também [a documentação da v2.2.2](https://github.com/wilkermaa/axipesquisa/blob/v2.2.2/docs/PLATAFORMAS.md).


## Downloads históricos por versão e plataforma

As versões abaixo possuem oito instaladores cada. As versões 2.2.0-rc2, rc3, rc4 e 2.2.1 foram reconstruídas diretamente das fontes das tags. Os ZIPs v2.0.0 foram **sanitizados** e não são idênticos byte a byte aos originais. Os testes realizados são estruturais e não comprovam compatibilidade funcional em cada serviço Web.

### [AXI v2.2.1](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.1)

| IA | Instalador |
|---|---|
| Antigravity | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.1/axipesquisa-2.2.1-antigravity.zip) |
| ChatGPT Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.1/axipesquisa-2.2.1-chatgpt-web.zip) |
| Claude Code | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.1/axipesquisa-2.2.1-claude-code.zip) |
| Claude Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.1/axipesquisa-2.2.1-claude-web.zip) |
| Codex | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.1/axipesquisa-2.2.1-codex.zip) |
| Gemini Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.1/axipesquisa-2.2.1-gemini-web.zip) |
| Grok Build CLI | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.1/axipesquisa-2.2.1-grok-build-cli.zip) |
| Grok Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.1/axipesquisa-2.2.1-grok-web.zip) |

[Verificar SHA256](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.1/SHA256SUMS-v2.2.1.txt)

### [AXI v2.2.0-rc4](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.0-rc4)

| IA | Instalador |
|---|---|
| Antigravity | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc4/axipesquisa-2.2.0-rc4-antigravity.zip) |
| ChatGPT Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc4/axipesquisa-2.2.0-rc4-chatgpt-web.zip) |
| Claude Code | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc4/axipesquisa-2.2.0-rc4-claude-code.zip) |
| Claude Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc4/axipesquisa-2.2.0-rc4-claude-web.zip) |
| Codex | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc4/axipesquisa-2.2.0-rc4-codex.zip) |
| Gemini Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc4/axipesquisa-2.2.0-rc4-gemini-web.zip) |
| Grok Build CLI | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc4/axipesquisa-2.2.0-rc4-grok-build-cli.zip) |
| Grok Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc4/axipesquisa-2.2.0-rc4-grok-web.zip) |

[Verificar SHA256](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc4/SHA256SUMS-v2.2.0-rc4.txt)

### [AXI v2.2.0-rc3](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.0-rc3)

| IA | Instalador |
|---|---|
| Antigravity | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc3/axipesquisa-2.2.0-rc3-antigravity.zip) |
| ChatGPT Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc3/axipesquisa-2.2.0-rc3-chatgpt-web.zip) |
| Claude Code | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc3/axipesquisa-2.2.0-rc3-claude-code.zip) |
| Claude Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc3/axipesquisa-2.2.0-rc3-claude-web.zip) |
| Codex | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc3/axipesquisa-2.2.0-rc3-codex.zip) |
| Gemini Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc3/axipesquisa-2.2.0-rc3-gemini-web.zip) |
| Grok Build CLI | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc3/axipesquisa-2.2.0-rc3-grok-build-cli.zip) |
| Grok Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc3/axipesquisa-2.2.0-rc3-grok-web.zip) |

[Verificar SHA256](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc3/SHA256SUMS-v2.2.0-rc3.txt)

### [AXI v2.2.0-rc2](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.0-rc2)

| IA | Instalador |
|---|---|
| Antigravity | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc2/axipesquisa-2.2.0-rc2-antigravity.zip) |
| ChatGPT Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc2/axipesquisa-2.2.0-rc2-chatgpt-web.zip) |
| Claude Code | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc2/axipesquisa-2.2.0-rc2-claude-code.zip) |
| Claude Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc2/axipesquisa-2.2.0-rc2-claude-web.zip) |
| Codex | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc2/axipesquisa-2.2.0-rc2-codex.zip) |
| Gemini Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc2/axipesquisa-2.2.0-rc2-gemini-web.zip) |
| Grok Build CLI | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc2/axipesquisa-2.2.0-rc2-grok-build-cli.zip) |
| Grok Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc2/axipesquisa-2.2.0-rc2-grok-web.zip) |

[Verificar SHA256](https://github.com/wilkermaa/axipesquisa/releases/download/v2.2.0-rc2/SHA256SUMS-v2.2.0-rc2.txt)

### [AXI v2.0.0](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.0.0)

| IA | Instalador |
|---|---|
| Antigravity | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/axipesquisa-v2-antigravity-sanitizado.zip) |
| ChatGPT Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/axipesquisa-v2-chatgpt-web-sanitizado.zip) |
| Claude Code | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/axipesquisa-v2-claude-code-sanitizado.zip) |
| Claude Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/axipesquisa-v2-claude-web-sanitizado.zip) |
| Codex | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/axipesquisa-v2-codex-sanitizado.zip) |
| Gemini Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/axipesquisa-v2-gemini-web-sanitizado.zip) |
| Grok Build CLI | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/axipesquisa-v2-grok-build-cli-sanitizado.zip) |
| Grok Web | [Baixar ZIP](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/axipesquisa-v2-grok-web-sanitizado.zip) |

[Verificar SHA256](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/SHA256SUMS-v2.0.0.txt) · [Nota de sanitização](https://github.com/wilkermaa/axipesquisa/releases/download/v2.0.0/LEIA-SANITIZACAO-v2.0.0.txt)

## Histórico completo de versões identificadas

| Versão | Material localizado | Estado dos downloads públicos de instaladores |
|---|---|---|
| v1.0 | Documentação parcial | Sem instalador completo identificado; [registro](https://github.com/wilkermaa/axipesquisa/releases/tag/v1.0) |
| v2.0.0 | Oito pacotes de distribuição sanitizados | [Baixar instaladores sanitizados](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.0.0) |
| v2.1.0-rc1 | Documentação e protocolo | Sem instalador completo identificado; [registro](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.1.0-rc1) |
| v2.2.0-rc2 | Oito instaladores reconstruídos da tag e benchmark separado | [8 ZIPs](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.0-rc2) |
| v2.2.0-rc3 | Oito instaladores reconstruídos da tag | [8 ZIPs](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.0-rc3) |
| v2.2.0-rc4 | Oito instaladores reconstruídos da tag | [8 ZIPs](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.0-rc4) |
| v2.2.1 | Oito instaladores reconstruídos da tag | [8 ZIPs](https://github.com/wilkermaa/axipesquisa/releases/tag/v2.2.1) |
| **v2.2.2** | **Oito ZIPs de instalação presentes no GitHub** | **Links públicos disponíveis acima** |

Os snapshots completos estão preservados em [tags anotadas](https://github.com/wilkermaa/axipesquisa/tags) e os arquivos para usuários em [Releases](https://github.com/wilkermaa/axipesquisa/releases), com rastreabilidade no [índice de origem](../INDICE-ORIGEM.md). Este catálogo não presume que arquivos presentes em áreas privadas do Drive sejam acessíveis ao público.

## Política de publicação de versões

1. Para cada versão, conferir o conteúdo, a licença, o identificador de versão e a compatibilidade de cada pacote.
2. Criar a **tag Git correspondente ao commit da versão**, sem apontar todas as tags históricas para a mesma versão atual por conveniência.
3. Publicar um **GitHub Release por tag**, anexando os ZIPs de instalação como assets separados por plataforma, com instruções, alterações e limitações verificadas.
4. Preservar versões antigas: novos lançamentos não substituem nem renomeiam os ZIPs anteriores.
5. O README deve priorizar o último lançamento disponível; este catálogo deve permitir escolher as versões anteriores.

Página destinada a receber os pacotes: [GitHub Releases](https://github.com/wilkermaa/axipesquisa/releases). **As oito tags históricas e respectivos Releases já existem.** As distribuições instaláveis estão disponíveis para v2.0.0 e v2.2.0-rc2 até v2.2.2. As versões v1.0 e v2.1.0-rc1 são registros documentais parciais.

## Atenção sobre experimentos

Versões de instalação e versões do estudo são distintas: o experimento C0/C1/C2 preserva a condição AXI v2.2.0-rc2 congelada. Não substituir silenciosamente o pacote experimental por um instalador mais novo. Consulte [Pesquisa científica](PESQUISA-CIENTIFICA.md).
