# Instalação da Skill AXI-Pesquisa v2.3.5

**Objeto:** instalar o método editorial AXI-Pesquisa. **Não é o ZIP do repositório nem o pacote de benchmark experimental.**

1. Leia o `SKILL.md` e revise as permissões solicitadas pela plataforma. A Skill é um conjunto de instruções e referências, não habilita ferramentas ou permissões ausentes.
2. **ChatGPT Web:** use o pacote ChatGPT com a pasta `axipesquisa/` na raiz; carregue na área de Habilidades se disponível na conta. Ao atualizar, desative a versão antiga. A existência de um botão depende da conta e do workspace.
3. **Gemini Web:** use o pacote Gemini com `SKILL.md` na raiz. Procure a área Personalizar > Habilidades e importe a pasta/ZIP caso disponível; desative versões antigas para evitar ativação cruzada.
4. **Claude Web:** use o pacote Claude com a pasta `axipesquisa/` e carregue na área de Skills disponível.
5. **Grok Web:** use `SKILL.md` como referência quando a interface não aceitar importação de ZIP; o suporte exato do formato depende da conta.
6. **Codex / Antigravity:** extraia a pasta `.agents/skills/axipesquisa/` no projeto. **Claude Code:** `.claude/skills/axipesquisa/`. **Grok Build CLI:** `.grok/skills/axipesquisa/`.
7. **Gemini:** confirme com um teste de fluxo que a IA **aciona e mostra um gráfico SVG em prévia**, quando renderizável, ou **PNG/visual nativo** equivalente; `flowchart TD` em snippet não atende. PDF não é obrigatório. Para confirmar a microfase **Diagramação do Fluxo de Aplicação**, peça a explicação de um processo sem solicitar fluxograma; se houver fluxo fiel, a Skill deve tentar entregar **visual real**. A IA executora escolhe a tecnologia disponível; **uma imagem realmente visível ou prévia é suficiente** e PDF não é exigido. Código ou texto apenas são entrega parcial. Teste real em conta continua pendente.
8. **Regressão jurídica ABNT:** peça o procedimento de mudança de lotação em Matinhos. A resposta deve efetivamente pesquisar a legislação local, identificar o artigo 57 da Lei 1.165/2008 com distinção Portaria/Ofício **quando confirmado na fonte**, apresentar fontes ABNT e tentar a figura. **ABNT, pesquisa e diagramação não se substituem.** O protocolo jurídico complementar está em `references/PROTOCOLO-JURIDICO-ABNT.md`; manter o protocolo original de fontes sem alterações.
9. Verifique em teste simples o identificador `2.3.5` e as fases A, X e I, sem presumir que a Skill tenha sido acionada apenas por estar instalada.
10. Para experimentos C0/C1/C2 comparativos, **não deixe a Skill AXI ativável nas condições de controle**. O benchmark original usa texto congelado da versão 2.2.0-rc2.

**Fontes de apoio:** documentação de plataformas em `docs/PLATAFORMAS.md` no repositório-fonte. Não há garantia de funcionamento nas interfaces sem teste real.

**Autor:** Wilker M. de Araujo Alexandre. Textos originais sob CC BY 4.0; consulte `LICENSE-CONTENT.md`.
