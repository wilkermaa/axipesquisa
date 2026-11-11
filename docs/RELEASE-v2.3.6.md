# AXI-Pesquisa v2.3.6 — restauração do contrato integral e rotas de diagramação

**PATCH | 11 nov. 2026 | Autorização:** restauração das instruções enfraquecidas v2.0.0; leitura integral, progressiva e obrigatória de arquivos da Skill; padronização específica de visual por IA.

## Mudanças e decisão

- **Leitura integral do pacote**: ler `SKILL.md` completamente e demais arquivos textuais **um a um** durante início/A, meio/X e fim/I. Não trocar por resumos ou só fragmentos; não declarar leitura que a sessão não permitiu. Roteiro: `references/FLUXO-LEITURA-INTEGRAL.md`.
- **Fontes ABNT:** seção `Fontes consultadas (ABNT)` em **toda resposta explicativa ou de pesquisa**; registrar fontes reais ou declarar ausência de consulta, sem inventar URLs. A pesquisa jurídica validada continua obrigatória quando pertinente.
- **Recuperação v2.0:** 12 casos originais T01–T12 preservados byte a byte e agora de leitura obrigatória; oito perguntas editoriais de Meyer preservadas; comparações filosóficas/metafísicas novamente citadas na alternativa compacta; assinatura neutra autorizada, sem expor dados pessoais no ZIP público.
- **Renderização específica por plataforma (fase I):** ChatGPT usa Mermaid com prévia; Claude Web usa visual HTML/SVG inline ou Artifact renderizado; Grok Web usa SVG em cartão com prévia ou HTML Preview em Projects; Gemini Web **busca Canvas com SVG e Prévia** quando efetivamente integrado.
- **Limite do Gemini:** o suporte oficial Google em 11/11/2026 declara que Skills **não funcionam com Canvas**; esta instrução é a rota futura/prioritária, **não prova de integração habilitada**. Se o modelo não puder acionar Canvas junto à Skill, não fingir sucesso; tentar uma visualização SVG real acessível como alternativa e registrar entrega parcial na ausência de figura.
- **Pacotes específicos:** `scripts/build.py` inclui `INSTALADOR-PLATAFORMA.md` próprio em cada ZIP, com referências técnicas e contrato de leitura/ABNT.

## Testes e riscos residuais

CI e testes avaliam texto, preservação de material histórico, versão e oito ZIPs com SHA-256. **Não demonstram que qualquer modelo leu integralmente todos os arquivos, executou Canvas, gerou figura ou seguiu ABNT em um atendimento real.** Homologação nas IAs continua pendente, especialmente Gemini (Issue #4). Espelhamento Drive permanece Issue #6. Preservar tags anteriores e experimento C0/C1/C2 congelado v2.2.0-rc2.

## Fontes técnicas consultadas na elaboração (ABNT; não copiar automaticamente às respostas da Skill)

GOOGLE. *Sobre a transição dos Gems para habilidades*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/18560919?hl=pt-BR. Acesso em: 11 nov. 2026.
ANTHROPIC. *Visuais personalizados no chat e Cowork*. 2026. Disponível em: https://support.claude.com/pt/articles/13979539-visuais-personalizados-no-chat-e-cowork. Acesso em: 11 nov. 2026.
GROK. *Release Notes — Sep 19, 2026*. 2026. Disponível em: https://grok.com/release-notes/sep-19-2026. Acesso em: 11 nov. 2026.
OPENAI. *Como trabalhar com blocos de escrita e blocos de código no ChatGPT*. [s.d.]. Disponível em: https://help.openai.com/pt-br/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt. Acesso em: 11 nov. 2026.

