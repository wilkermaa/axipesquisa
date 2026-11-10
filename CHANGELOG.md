# Changelog

## 2.2.0-rc3 — 2026-11-06

- Nova política condicional de diagrama Mermaid na etapa I (Integração): fluxos, decisões, arquiteturas, sequências e relações.
- Legibilidade, hierarquia e rótulos acessíveis para estados; cores semânticas discretas (verde, amarelo, vermelho) quando suportadas.
- Orientação para exportação de SVG e PNG reais e verificáveis; fallback textual em Mermaid quando exportação não for possível.
- Nenhum diagrama obrigatório: texto suficiente mantém resposta simples.
- Alinhamento dos oito pacotes distribuídos e da alternativa textual.
- Atualização apenas editorial: não constitui validação empírica nem teste nativo em provedor.
- Protocolo experimental anterior `2.2.0-rc2` preservado como versão congelada: não modificar silenciosamente seus controles.


## 2.2.0-rc2 — 2026-11-04

- Red Team documentado com riscos classificados e pendências abertas.
- Núcleo AXI mais preciso: todo/partes, analogias relacionais com limites e integração sem causalidade inventada.
- PNL/Dilts reclassificada como heurística não validada; livro de Meyer usado apenas como orientação de contexto e preferências explícitas.
- Bibliografia de desenvolvimento separada de fontes efetivamente consultadas em cada atendimento.
- Removida configuração pessoal de pacotes públicos, substituída por exemplo neutro.
- Regras claras contra prompt injection, vazamento e quebra de saídas estruturadas.
- Plano de experimento A/B para estudar efeitos reais; sem alegação de superioridade.
- Scripts de validação, empacotamento determinístico, testes adversariais e CI propostos.

## 2.0.0 — 2026-11-04 (histórico auditado)

- Oito variantes por plataforma, fundamentação e protocolos AXI A/X/I. Não redistribuir publicamente os pacotes anteriores sem revisar dados pessoais embutidos.

## v2.2.0-rc2 (2026-11-04)
- Executor API reproduzível de benchmark nos provedores OpenAI, Anthropic, Gemini e xAI (requer chaves e autorização de cobrança).
- Comparação pareada AXI × genérico × baseline, oráculos determinísticos, rubrica e kit de revisão humana.
- Pacote separado candidato a ChatGPT Plugin, distinto da Skill local; correção da documentação de compatibilidade.
- Matriz de licenciamento; arquivo LICENSE não concedido sem escolha do titular.
- Status explícito de **zero execuções reais nesta entrega**.

## Proposta de licenciamento aberto (04/11/2026)

- Incluídos MIT para software e CC BY 4.0 para documentação/skill textual, com aviso de atribuição e escopo.
- Identidade pública confirmada como `Wilker M. de Araujo Alexandre` em 04/11/2026.
- Não altera a avaliação científica do AXI nem substitui testes em provedores reais.

## Decisão de autoria pública (04/11/2026)

- Crédito original confirmado: **Wilker M. de Araujo Alexandre**.
- Avisos de licença, atribuição, README, SKILL.md e pacotes de distribuição atualizados.
- Correção do status anterior de autoria provisória. Não há validação empírica de modelo nesta alteração.

## Revisão de pré-publicação (05/11/2026)

- Corrigido guia de release que ainda indicava `v2.1.0-rc1` como versão de publicação.
- Relatórios 2.1.0-rc1 identificados explicitamente como históricos.
- Incluído encaminhamento de validação para Rafaell, sem declarar independência automática nem eficácia.
