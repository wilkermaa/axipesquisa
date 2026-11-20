# Proposta de TCC / Pesquisa Empírica: Avaliação de Usabilidade e Compreensão com Leitores Humanos (AXI Pesquisa v2.3.8 vs v2.4.0)

**Título Sugerido:**  
*Impacto da Decomposição Visual em Árvore Hierárquica (Tree + Cards) na Compreensão, Tempo de Resposta e Sobrecarga Cognitiva Humana: Um Estudo Comparativo entre as Versões v2.3.8 e v2.4.0 da Skill AXI Pesquisa.*

**Área de Concentração:**  
Interação Humano-Computador (IHC), Engenharia de Software, Ciência da Computação, Sistemas de Informação ou Design de Informação.

**Repositório Base:** https://github.com/wilkermaa/axipesquisa  
**Orientação / Contexto:** AXI Pesquisa, Governança SOPRO GPDO e PEC-001.

---

## 1. Contexto e Motivação Científica

A versão **v2.4.0** da Skill *AXI Pesquisa* introduziu a **Microfase A — Visualização do Todo e das Partes**, priorizando diagramação hierárquica no padrão **Markmap (Tree + Cards, leitura da esquerda para a direita)** quando houver decomposição estrutural fiel, preservando a **Fase I (Mermaid / fluxogramas de processo)**.

Nos ensaios automatizados de laboratório com modelos de linguagem (IA como leitora), observou-se:
1. **Efeito Teto em tarefas simples/médias:** LLMs processam texto linear e imagens estruturadas sem fadiga visual ou limite de memória de trabalho de curto prazo, obtendo pontuação máxima (100%) tanto com texto puro (estilo v2.3.8) quanto com mapa hierárquico (estilo v2.4.0).
2. **Armadilha da Árvore Enganosa em domínios não-hierárquicos:** Quando um sistema possui **múltiplos pais ou arestas cruzadas** (ex.: órgãos com atuação transversal), a imposição de uma árvore estrita oculta relações e induz a IA leitora a erros categóricos (conforme salvaguarda `A06` da política de requisitos da v2.4.0).

Entretanto, **seres humanos possuem limitações biológicas de memória operacional (Miller, 1956; Sweller, 1988) e processam canais visuais e verbais em subsistemas separados (Teoria da Dupla Codificação de Paivio, 1986; Teoria Cognitiva da Aprendizagem Multimídia de Mayer, 2001)**. Estudos clássicos (Larkin & Simon, 1987) apontam que diagramas espaciais indexam informação contígua, reduzindo o tempo de busca visual e acelerando inferências humanas.

**A lacuna empírica que este TCC preenche:**  
A superioridade da v2.4.0 sobre a v2.3.8 para usuários humanos ainda é uma **hipótese teórica e arquitetural**, não um fato empiricamente medido. Este trabalho realizará o primeiro ensaio clínico/experimental controlado com participantes humanos.

---

## 2. Questões de Pesquisa (QPs) e Hipóteses

- **QP1 (Tempo de Recuperação):** Leitores humanos localizam componentes e respondem a perguntas estruturais mais rapidamente com o mapa visual Tree + Cards (v2.4.0) do que com texto puro (v2.3.8)?
  - *H1:* O tempo médio de resposta no Grupo v2.4.0 é significativamente menor que no Grupo v2.3.8 ($p < 0,05$).
- **QP2 (Acurácia e Retenção):** A visualização em Tree + Cards melhora a precisão na lembrança das partes e subpartes após intervalo de distração?
  - *H2:* A taxa de acertos no recall de componentes é maior na v2.4.0.
- **QP3 (Carga Cognitiva e Facilidade Percebida):** Qual versão gera menor esforço mental percebido pelos participantes?
  - *H3:* A pontuação na escala NASA-TLX (ou SMEQ) é estatisticamente menor na v2.4.0.
- **QP4 (Ponto de Ruptura / Limite da Árvore):** Em domínios complexos com componentes transversais (múltiplos pais), a árvore Tree + Cards induz o leitor humano ao erro de silo/exclusividade em taxa maior do que o texto explicativo (validando a salvaguarda `A06`)?
  - *H4:* A árvore estrita reduz o acerto humano em perguntas sobre dependências transversais.

---

## 3. Desenho Metodológico do Experimento

### 3.1. Delineamento
- **Design Experimental:** *Between-subjects* (entre sujeitos) ou *Within-subjects* contrabalanceado (Latin Square para mitigar efeito de aprendizagem).
- **Amostra Mínima:** $N = 30$ participantes (15 no Grupo Controle v2.3.8 e 15 no Grupo Experimental v2.4.0) para poder estatístico básico ($1 - \beta \ge 0,80$ com tamanho de efeito médio $d \ge 0,5$).

### 3.2. Materiais e Condições
1. **Três Cenários de Teste Padronizados:**
   - **Cenário 1 (Simples):** Cafeteria (4 áreas, 8 subpartes, fluxo linear).
   - **Cenário 2 (Médio):** Aeroporto comercial (5 áreas, 25 subpartes, operações coordenadas).
   - **Cenário 3 (Adversarial / Não-árvore):** Sistema Integrado de Defesa/Segurança com atuação transversal e múltiplos pais (para testar `A06`).
2. **Duas Variantes de Entrega:**
   - **Condição A (v2.3.8):** Fase A em texto estruturado + Fase I em fluxograma.
   - **Condição B (v2.4.0):** Fase A em Markmap Tree + Cards (ESQ → DIR) + Fase I em fluxograma.

### 3.3. Procedimento de Aplicação
1. **Consentimento (TCLE):** Adesão voluntária e termo de sigilo conforme LGPD.
2. **Fase de Exposição:** Apresentação do material na tela por tempo controlado (ex.: 90 a 120 segundos) ou com cronometragem livre de leitura.
3. **Fase de Teste (Bloqueio do Material):**
   - Questionário objetivo de 5 a 6 questões por cenário.
   - Cronômetro automático por pergunta (tempo de latência e tempo total).
4. **Avaliação Subjetiva pós-tarefa:**
   - Escala NASA-TLX (Esforço mental, frustração, desempenho).
   - Escala de Facilidade Percebida (Likert 1 a 5).
   - Pergunta aberta de percepção qualitativa.

---

## 4. Cronograma de Execução do TCC (1 ou 2 Semestres)

| Etapa | Atividade | Duração |
|---|---|---|
| **Etapa 1** | Revisão bibliográfica (Carga Cognitiva, IHC, AXI e Visualização de Dados) | 4 semanas |
| **Etapa 2** | Calibração dos cenários e pré-teste piloto ($N = 4$) | 3 semanas |
| **Etapa 3** | Submissão ao Comitê de Ética em Pesquisa (CEP) / TCLE | 4 semanas |
| **Etapa 4** | Aplicação do experimento com a amostra real ($N \ge 30$) | 5 semanas |
| **Etapa 5** | Tabulação, análise estatística (Shapiro-Wilk, Teste t / Mann-Whitney, ANOVA) | 3 semanas |
| **Etapa 6** | Redação final da monografia / artigo científico e defesa | 4 semanas |

---

## 5. Entregáveis Esperados do Estudante

1. **Monografia de TCC ou Artigo Científico:** Em formato ABNT (ou template SBC / IEEE).
2. **Dataset Aberto e Anonimizado:** Planilha CSV contendo tempos brutos, acertos por questão e scores psicométricos.
3. **Scripts de Análise R / Python:** Código reproduzível em Jupyter Notebook com gráficos de dispersão, boxplots e testes de significância.
4. **Relatório de Recomendações de Engenharia:** Contribuição direta ao repositório `wilkermaa/axipesquisa`, recomendando limiares ótimos para a Microfase A (ex.: quantidade de nós a partir da qual a árvore se torna cognitiva mente vantajosa ou desvantajosa).

---

## 6. Fontes e Referências Teóricas Recomendadas

- LARKIN, Jill H.; SIMON, Herbert A. Why a diagram is (sometimes) worth ten thousand words. **Cognitive Science**, v. 11, n. 1, p. 65-100, 1987.
- MAYER, Richard E. **Multimedia learning**. 3. ed. Cambridge: Cambridge University Press, 2021.
- SWELLER, John. Cognitive load during problem solving: Effects on learning. **Cognitive Science**, v. 12, n. 2, p. 257-285, 1988.
- HART, Sandra G.; STAVELAND, Lowell E. Development of NASA-TLX (Task Load Index): Results of empirical and theoretical research. **Advances in Psychology**, v. 52, p. 139-183, 1988.
- ALEXANDRE, Wilker M. de A. **AXI Pesquisa: Método de Análise, eXpansão e Integração para Agentes e Comunicação**. Versão 2.4.0. Repositório GitHub: wilkermaa/axipesquisa, 2026.
