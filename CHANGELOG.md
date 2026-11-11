# Changelog

## v2.3.4 — 11 nov. 2026 (PATCH)

- Corrige especificamente a execução da microfase **Diagramação do Fluxo de Aplicação** no Gemini Web: **abrir/renderizar uma prévia visual real antes de finalizar**, com SVG renderizado prioritário quando viável e PNG/visual nativo como alternativas.
- Reprova explicitamente `flowchart TD`, Mermaid ou XML SVG exibidos apenas como texto em **Snippet de código**. Código não substitui gráfico.
- Define verificação de figura/prévia/arquivo real e tentativa de uma alternativa visual funcional; falha deve ser marcada como entrega parcial, não sucesso presumido.
- Preserva a autonomia de escolha de tecnologia em outras plataformas, a economia de tokens, a privacidade, a não obrigatoriedade de PDF e as versões anteriores.
- Reforça teste independente no Gemini com versão ativa identificada. CI estrutural não prova funcionamento da interface e o protocolo C0/C1/C2 v2.2.0-rc2 permanece congelado.

## v2.3.3 — 11 nov. 2026 (PATCH)

- Corrige o acionamento real de renderização na microfase **Diagramação do Fluxo de Aplicação**, fase I — Integração: não basta escrever código; a IA deve tentar uma prévia ou entrega gráfica efetiva.
- **PDF não é obrigatório:** figura realmente apresentada no chat, prévia visual real ou arquivo gráfico válido atendem ao critério. Arquivo ou exportação não são exigidos quando a interface já mostra a figura.
- Incorpora 20 cenários de red team, limita tentativas a um mecanismo principal mais uma alternativa viável e registra falhas e capacidades sem inventá-las.
- Melhora a regra do Gemini: avaliar capacidades da sessão sem presumir Canvas automaticamente disponível ou indisponível, evitar código `graph TD` como saída concluída.
- Homologação em Gemini e nas demais IAs continua pendente; testes automáticos validam política textual, empacotamento e integridade, não a interface. Sem alterar v2.3.2 nem protocolo científico C0/C1/C2 v2.2.0-rc2.

## v2.3.2 — 11 nov. 2026 (PATCH)

- Corrige exclusivamente a microfase **Diagramação do Fluxo de Aplicação**, na fase I — Integração, nível **Gestão e Coordenação**: exigir **entrega visual real** para fluxos fiéis, mesmo sem solicitação explícita.
- A IA executora escolhe **autonomamente** visualização nativa, Mermaid, SVG, HTML/preview, PNG ou tecnologia futura compatível; nenhuma linguagem ou ordem fixa é obrigatória.
- Distingue visual exibido, prévia, arquivo acessível e código/texto como resultado parcial; prioriza fidelidade, privacidade e economia real de tokens/passos.
- Declara **SemVer 2.0.0** como fundamentação técnica normativa de engenharia de software, **não** comprovação acadêmica da eficácia AXI.
- Mantém histórico da v2.3.1 e benchmark C0/C1/C2 v2.2.0-rc2. Testes estruturais não comprovam renderização nas plataformas.

## v2.3.1 — 11 nov. 2026 (PATCH)

- Corrige a omissão de diagramas na Integração com a microfase Diagramação do Fluxo de Aplicação.
- Exige o diagrama quando houver fluxo fielmente representável, mesmo sem pedido explícito. Sinaliza lacunas e preserva relações estáticas.
- Alinha as referências por plataforma e os testes de regressão ao requisito.

## v2.3.0 — 11 nov. 2026 (MINOR; fechamento de distribuição condicionado)

- Nova funcionalidade da fase I: reconhecimento gratuito das capacidades da sessão e seleção adaptativa do renderer com menor custo incremental observável.
- Implementação em ordem Gemini Web, ChatGPT e lote das seis outras plataformas, preservando Mermaid/SVG/Canvas e distinguindo prévia, código e exportação.
- Um visual principal por padrão; gráficos quantitativos usam visualização quantitativa quando disponível; sem rede ou plugins apenas para renderizar.
- Acrescentadas referências específicas e testes estruturais de roteamento; testes reais de interfaces, custos mensurados e validação científica continuam pendentes.
- Experimento C0/C1/C2 v2.2.0-rc2 inalterado.


## v2.2.3 — 10 nov. 2026

- Restaurados os 12 exemplos didáticos da v2.0 e as oito perguntas editoriais de Erin Meyer.
- Guia de instalação dentro dos oito pacotes da Skill.
- Incluídos dez testes locais de regressão e política de atualização de versão e tag.
- Núcleo A–X–I e 36 cenários experimentais preservados; 71 testes locais aprovados na preparação.
- Validação científica independente pendente.


## v2.2.2 — 10 nov. 2026

- Corrige a insuficiência visual no Gemini: fallback SVG autossuficiente e HTML/SVG no Canvas quando não houver prévia Mermaid.
- Recomenda botões reais de exportação SVG e PNG em página Canvas, quando possíveis, sem dependência de CDN nem transmissão de dados privados.
- Distingue código, prévia renderizada e arquivos efetivamente entregues; proíbe declarar sucesso sem evidências.
- Acrescenta guia Gemini e testes de aceitação estáticos. **Não constitui teste real no Gemini Web.**

# Changelog

## v2.3.1 — 11 nov. 2026 (PATCH)

- Corrige a omissão de diagramas na Integração com a microfase Diagramação do Fluxo de Aplicação.
- Exige o diagrama quando houver fluxo fielmente representável, mesmo sem pedido explícito. Sinaliza lacunas e preserva relações estáticas.
- Alinha as referências por plataforma e os testes de regressão ao requisito.

## 2.2.1 — 2026-11-10

- Correção de versão: abandona o sufixo RC nas distribuições atuais e usa o terceiro segmento (patch) para correções futuras.
- Consolida o ajuste de diagramas Mermaid da rc4: pedido explícito exige tentativa de renderização, não apenas código ou wireframes.
- Exportações SVG/PNG somente se os arquivos existirem e forem verificáveis; declarar reconstruções com outros motores e limitações reais.
- Todos os oito instaladores usam o mesmo núcleo SKILL.md e metadado de versão 2.2.1.
- Nenhuma validação científica independente ou sucesso de renderização no Gemini foi demonstrado por testes estruturais.
- O benchmark científico iniciado com **2.2.0-rc2 continua congelado**, evitando contaminação experimental.


## 2.2.0-rc4 — 2026-11-10

- Correção do contrato de diagramas na fase I: pedido explícito exige tentativa efetiva de visualização, não só código Mermaid ou wireframes.
- Ordem de preferência: renderer nativo quando disponível; artefato visual via ferramentas habilitadas; fallback honesto quando impossível.
- SVG/PNG devem ser arquivos reais, verificáveis; conversão com outro motor deve ser identificada como equivalente.
- Status de cores apenas quando sustentados por evidência; casos não verificados ficam neutros e "a validar".
- Documentação baseada na disponibilidade de arquivos SVG/PNG e recursos de Canvas do Gemini, sem alegar que toda sessão tem um parser Mermaid.
- O benchmark da v2.2.0-rc2 continua congelado. Não há comprovação de superioridade científica.

# Changelog

## v2.3.1 — 11 nov. 2026 (PATCH)

- Corrige a omissão de diagramas na Integração com a microfase Diagramação do Fluxo de Aplicação.
- Exige o diagrama quando houver fluxo fielmente representável, mesmo sem pedido explícito. Sinaliza lacunas e preserva relações estáticas.
- Alinha as referências por plataforma e os testes de regressão ao requisito.

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
