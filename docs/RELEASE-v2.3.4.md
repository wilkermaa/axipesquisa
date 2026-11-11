# AXI-Pesquisa v2.3.4 — Gemini Web: renderização SVG/prévia executada

**Classificação:** PATCH. **Data:** 11 nov. 2026. **Escopo:** correção editorial da microfase **Diagramação do Fluxo de Aplicação**, exclusiva da fase **I — Integração**.

## O que muda

- Na Skill principal, regra explícita para o **Gemini Web**: quando houver fluxo fiel, **acionar visualização e abrir prévia diretamente na sessão** antes de finalizar.
- **SVG realmente renderizado** é o caminho prioritário se a interface permitir sua exibição; se não permitir, usar **PNG ou gráfico nativo** efetivamente disponível. Nenhuma tecnologia é obrigatória para todas as plataformas.
- `flowchart TD`, `graph TD`, XML `<svg>` e HTML em snippet, sem desenho na tela nem arquivo gráfico real, são **falha do critério visual**, não êxito.
- Conferir que o visual existe e está legível; quando uma tentativa só produzir código, tentar outra opção funcional. Se nenhuma saída real for produzida, informar **entrega parcial**.
- **PDF não é obrigatório**; imagem exibida ou prévia real já satisfaz a exigência de visualização. Não presumir que Canvas funcione dentro da conversa da Skill sem comprovação.

## Validação

O CI executa testes de fonte, regressão e empacotamento de oito instaladores. Os testes não executam a interface Gemini. **Homologação funcional no Gemini permanece pendente**, incluindo versão da Skill realmente ativa, prompt, captura de tela, mecanismo acionado e figura exibida. A falha de snippet registrada na Issue #4 motivou a mudança.

## Governança

Preservar tags e assets das versões anteriores, SemVer 2.0.0 como referência técnica e o experimento científico C0/C1/C2 congelado em v2.2.0-rc2. Ver `docs/POLITICA-VISUAL.md` e `docs/INSTALADORES.md`.
