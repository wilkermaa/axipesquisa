# AXI Pesquisa v2.3.10 — correção urgente Gemini: PNG antes de resposta, sem snippet

**PATCH · 11 nov. 2026.** Corrige regressão funcional observada no Gemini com a v2.3.9, mantendo intactos os fundamentos AXI e a estética aprovada.

## Falha observada

No procedimento de mudança de lotação em Guaratuba, o Gemini publicou **“Registro de Entrega Visual Parcial” seguido de bloco Mermaid `flowchart TD`** e alegou indisponibilidade gráfica. **Nenhum PNG foi entregue na resposta.** O texto não prova que houve tentativa efetiva de acionar ferramenta nem que a ferramenta estivesse indisponível. O cabeçalho SOPRO presente na resposta é outro elemento contextual, mas não prova interferência causal.

## Correção

- **Ação real primeiro:** no Gemini, **ACIONAR a geração de PNG**, produzir/exibir uma imagem visível no chat ou em prévia aberta e confirmar sua existência **ANTES** de terminar a explicação.
- **Estética em segundo lugar:** caixas somente com títulos curtos, sem ícones, subtítulos ou descrições internas, conexões semanticamente fiéis. Mermaid é somente referência visual ou estrutura intermediária interna, jamais snippet de saída no Gemini.
- **Sem código compensatório:** é expressamente proibido devolver `mermaid`, `flowchart TD`, XML SVG/HTML, tabela ou ASCII no lugar de imagem, inclusive após declarar entrega parcial.
- **Tentativa e recuperação:** não alegar ferramenta inexistente/indisponível sem evidência observável. Após tentativa PNG sem êxito, tentar um renderizador gráfico realmente habilitado. Sem figura, relatar objetivamente entrega visual não realizada, sem código e sem alegação falsa.
- **Preservações:** leitura integral A → X → I, pesquisa normativa e fontes reais em ABNT, demais rotas específicas das IAs, PDF opcional, tags anteriores intocadas e C0/C1/C2 v2.2.0-rc2 congelado.

## Limite técnico e aceite

A documentação Google confirma que **Skills não operam com todas as ferramentas**, incluindo Canvas. As fontes consultadas **não estabelecem que o acionamento automático da ferramenta de imagens esteja garantido em todas as sessões com Skill ativa**. Portanto, esta mudança é de contrato e roteamento: **CI de texto **não demonstram renderização real** no Gemini e não constitui prova de execução no Gemini**. Homologação funcional exige prompt idêntico, versão aprovada, modelo, configuração de esforço, tentativa observável e captura do PNG renderizado. Não prometer 100% de sucesso sem evidência.

## Fontes consultadas (ABNT)

GOOGLE. *Criar e gerenciar habilidades para os apps do Gemini*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/17094296?hl=pt-BR. Acesso em: 11 nov. 2026.
GOOGLE. *Sobre a transição dos Gems para habilidades*. 2026. Disponível em: https://support.google.com/gemini/answer/18560919?hl=pt-BR. Acesso em: 11 nov. 2026.
GOOGLE. *Gerar e editar imagens com os apps do Gemini*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/14286560?hl=pt-BR. Acesso em: 11 nov. 2026.
