# Plano preregistrável para testar o AXI

**Objetivo:** verificar se o AXI melhora qualidade das explicações, sem aumentar injustificadamente tempo, verbosidade, falsa confiança, erros ou referências inventadas. Este é um **plano**, não um experimento realizado.

## Hipóteses a pré-registrar

- H1: em tarefas complexas de explicação, AXI melhora a compreensão demonstrada pelo leitor em comparação a um baseline sem skill.
- H2: AXI melhora percepção de clareza e estrutura em comparação a baseline sem skill **e** a instruções genéricas de estruturação (controle ativo).
- H3: AXI não aumenta a taxa de erros factuais, analogias enganosas ou violações de formato além de limites previamente definidos.
- Hipótese nula: não há diferença além da variabilidade de tarefa, modelo e leitor.

## Desenho proposto

1. **Conjunto de tarefas** diversificado: conceitos cotidianos, engenharia de software, sistemas, filosofia, direito/saúde com cautela, perguntas triviais e solicitações com saída estrita. Fixar tarefas e critérios **antes** de testar.
2. **Três condições:** (C0) modelo sem skill; (C1) instrução neutra “explique de modo estruturado, com exemplos e fontes”; (C2) skill AXI. Manter modelo, temperatura/parâmetros quando acessíveis, ferramentas, prompt e contexto equivalentes.
3. **Aleatorização/contrabalanceamento:** ordem randomizada de casos e condições, múltiplas gerações por tarefa; avaliadores cegos para a condição. Registrar modelos, versão, data, provedor, disponibilidade de busca e tokens aproximados.
4. **Avaliação:** (a) precisão factual com revisão independente; (b) mapa correto de partes e relações; (c) utilidade/limite de analogias; (d) capacidade de aplicar conceitos em problema novo; (e) fontes inventadas ou inadequadas; (f) aderência a formatos como JSON; (g) extensão e tempo/custo; (h) confiança autorrelatada e diferença frente à precisão.
5. **Leitores reais:** para compreensão, aplicar problemas de transferência equivalentes sem expor condição. Revisão por pelo menos dois avaliadores independentes e registro de divergências; dimensionamento amostral definido por análise de poder antes do estudo.
6. **Análise:** declarar desfecho primário e limites de segurança antes da coleta; comparar condições com intervalo de confiança, efeitos e distribuição por tipo de tarefa; documentar exclusões e falhas, sem trocar endpoint após ver resultados.
7. **Reprodutibilidade:** disponibilizar prompts, versões, instruções, rubrica, dados anonimizados e scripts de análise se compatível com privacidade e termos das plataformas.

## Métricas operacionalizadas sugeridas

| Métrica | Como aferir | Falha crítica |
|---|---|---|
| Factualidade | Cada alegação verificável confrontada com referência primária | Citação inventada em decisão de alta consequência |
| Cobertura | Checklist do todo e partes baseado em gabarito humano | Componente indispensável omitido |
| Analogias | Correspondência relacional e limites explicitados | Comparação tratada como prova |
| Aplicação | Resolver tarefa de transferência com resposta verificável | Passos inexequíveis e não sinalizados |
| Formato | Parser real para JSON/CSV/código quando solicitado | Saída inválida por assinatura/rodapé |
| Privacidade | Auditoria de nomes, tokens, arquivos e destinos | Exposição não autorizada |
| Eficiência | Tokens, latência e esforço do leitor, quando medidos | Prolixidade sem benefício demonstrado |

**Critério de publicação como método eficaz:** resultados consistentes com ganhos mensuráveis, margem aceitável nos riscos e replicação independente. Não declarar esse critério satisfeito nesta versão.

## Segurança e ética

Não usar dados privados como material de benchmark público. Para casos sensíveis, usar cenários sintéticos e revisão profissional; não instruir participantes a depender da IA para decisões clínicas, jurídicas ou de segurança física.

## Complemento obrigatório antes de coletas (v2.2)

**Desfecho primário no benchmark adversarial:** frequência de **falhas críticas verificadas por avaliadores independentes** por condição, estratificada por categoria. A simples omissão de etiqueta AXI não é falha crítica, e falta de ferramenta deve ser classificada como limitação, não alucinação se honestamente reconhecida.

**Desfechos secundários:** nota média de factualidade, adequação de formato, utilidade da analogia, clareza, capacidade de orientar aplicação, extensão e latência. A principal comparação substantiva será AXI vs controle **genérico**, pois o baseline sem orientação é menos exigente; AXI vs ausência de skill é secundária.

**Não equivalência entre teste API e teste Web:** chamadas API com prompt equivalente podem testar o efeito da instrução em condições controladas, mas não a instalação, ativação ou funcionamento da Skill nos apps. Relatar os dois resultados em tabelas separadas.

**Registro de dados:** só publicar resultados após examinar termos dos provedores, limpar dados privados e preservar a chave de cegamento separada das respostas entregues aos avaliadores.

**Condições de estudo de leitores:** definir população, tarefa de transferência, pré-teste, escore primário, cálculo de amostra, exclusões e logística antes da coleta. Resultados apenas de avaliações por modelos de IA não demonstram melhoria real de aprendizagem.
