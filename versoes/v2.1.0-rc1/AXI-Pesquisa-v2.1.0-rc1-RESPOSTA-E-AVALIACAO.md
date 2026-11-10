# AXI-Pesquisa — Resposta consolidada, opinião técnica e Red Team

**Registro da conversa:** 4 de novembro de 2026.  
**Versão examinada:** 2.0, com correções propostas na `2.1.0-rc1`.  
**Objetivo declarado pelo autor:** disponibilizar a skill AXI no GitHub com embasamento científico pertinente e passar por avaliação adversarial antes da publicação.

## 1. Entendimento do pedido e parecer

O AXI visa organizar explicações e pesquisas por meio de três operações complementares:

1. **A — Análise:** identificar o todo, suas partes e a definição de cada parte.
2. **X — eXpansão:** comparar os elementos analisados com contextos reais, virtuais, conceituais ou metafísicos, sem forçar analogias ou confundir metáforas com fatos.
3. **I — Integração:** explicar articulações e relações aplicáveis entre as partes e a utilização prática, sem inventar causalidade ou movimento.

**Parecer:** O AXI tem utilidade plausível como método de organização editorial, explicação e pesquisa. Não considero a proposta absurda ou desconectada da realidade. Sua contribuição mais relevante é integrar operações conhecidas em um procedimento explícito e verificável. Isso não equivale a uma teoria científica inédita ou a um método com eficácia já demonstrada. O método pode e deve ser submetido a comparação empírica.

O melhor posicionamento público é: **"protocolo autoral, experimental e multiplataforma para estruturar explicações, pesquisas e aplicações práticas"**. Não é defensável chamá-lo de "blindado", "cientificamente validado", "universalmente superior" ou "imune a alucinações".

## 2. Principais riscos apontados

A inspeção da v2.0 encontrou nome e e-mail pessoais embutidos na configuração distribuível, o que cria risco de exposição em um repositório público. A v2.1.0-rc1 desloca a identidade para configuração local, opcional, fora da distribuição pública.

Também foi identificado risco de confundir fontes científicas relativas a componentes do AXI com prova da eficácia do protocolo inteiro. René Descartes, Dedre Gentner, John Sweller e Richard Mayer oferecem fundamentos e inspiração pertinentes, mas nenhum deles demonstra por si só que o AXI melhora a aprendizagem ou a qualidade da resposta. O modelo de Robert Dilts/PNL foi reclassificado como heurística editorial opcional, sem promessa de eficácia científica; a revisão de Sturt et al. aborda intervenções de PNL em saúde, não teste direto do AXI. A abordagem de Erin Meyer exige respeito a preferências e contextos individuais, sem perfis culturais atribuídos automaticamente.

Outros riscos: comparações incorretas, causalidade fabricada na fase I, referências ABNT fictícias, vazamento de referências privadas, prompt injection em fontes externas, rodapés que invalidam JSON e código, excesso de prolixidade, pacote ZIP estruturalmente válido confundido com compatibilidade real, e ausência de decisão sobre licença aberta.

## 3. Auditoria realizada e limites

O relatório detalhado `AXI-Pesquisa-v2.1.0-rc1-REDTEAM.md` apresenta **22 achados** com mitigação e risco residual. Foram preparados **36 cenários adversariais** em `tests/cases.json`. A suíte automatizada local terminou com **22 testes estáticos aprovados**, e os oito ZIPs tiveram integridade/estrutura checadas. Isso não é o mesmo que executar os 36 casos em modelos reais.

**Não foram demonstrados:** compatibilidade operacional em todos os oito serviços, resistência robusta a prompt injection, redução mensurável de erros ou melhora em aprendizagem/compreensão, nem autorização definitiva de licença aberta. Segurança textual é mitigação parcial, não blindagem.

## 4. Avaliação crítica do valor do AXI

Eu manteria o método e continuaria seu desenvolvimento. Seu diferencial defendível está na articulação entre decomposição, comparação e aplicação prática, na transparência das fontes e na possibilidade de aplicar os mesmos critérios em diferentes provedores de IA. As operações isoladas são conhecidas, e isso deve ser reconhecido explicitamente.

Para determinar utilidade, é necessário um protocolo comparativo com respostas sem AXI e com instruções genéricas; avaliadores independentes, de preferência cegos à condição experimental; métricas de correção factual, compreensão, transferência para tarefas práticas, tempo e esforço; e análise de erros, alucinações e desempenho por domínio. Resultados favoráveis sustentariam afirmações limitadas ao contexto medido; resultados desfavoráveis devem levar a refino ou restrição de escopo.

## 5. Critérios de liberação

- **Segurança estática:** não publicar configuração pessoal, executáveis indevidos ou symlinks; validar caminhos, YAML e hashes.
- **Operação:** testar instalação e uso real em cada plataforma antes de declarar compatibilidade.
- **Ciência:** manter a descrição "fundamentação indireta; eficácia específica ainda não demonstrada" até haver experimento adequado.
- **Direitos:** o autor deve decidir licença, autoria pública, diretrizes de contribuição e política de manutenção.
- **Comunicação:** diferenciar referências efetivamente consultadas de bibliografia geral do projeto; não inventar fontes, datas nem resultados.

## 6. Entregáveis associados

- `AXI-Pesquisa-v2.1.0-rc1-GitHub.zip`: repositório publicável, skills multiplataforma, scripts, testes, documentação e CI.
- `AXI-Pesquisa-v2.1.0-rc1-REDTEAM.md`: 22 achados e mitigação.
- `AXI-Pesquisa-v2.1.0-rc1-FUNDAMENTACAO.md`: fundamentos e limites científicos.
- `AXI-Pesquisa-v2.1.0-rc1-RELATORIO.md`: validação estrutural e limitações.
- `AXI-Pesquisa-v2.1.0-rc1-ABNT.md`: bibliografia.
- `tests/cases.json`: 36 casos de avaliação adversarial ainda não executados nos modelos reais.
- `docs/PROTOCOLO-EMPIRICO.md`: plano de estudo comparativo.
- `dist/manifest-sha256.json`: hashes de pacotes da distribuição.

## 7. Fontes bibliográficas indicadas na resposta original (ABNT)

1. STANFORD ENCYCLOPEDIA OF PHILOSOPHY. *Descartes’ Method*. [s.d.]. Disponível em: https://plato.stanford.edu/entries/descartes-method/. Acesso em: 4 nov. 2026.
2. GENTNER, Dedre. Structure-mapping: a theoretical framework for analogy. *Cognitive Science*, v. 7, n. 2, p. 155-170, 1983. DOI: 10.1016/S0364-0213(83)80009-3. Disponível em: https://www.sciencedirect.com/science/article/pii/S0364021383800093. Acesso em: 4 nov. 2026.
3. SWELLER, John. Cognitive load during problem solving: effects on learning. *Cognitive Science*, v. 12, n. 2, p. 257-285, 1988. DOI: 10.1207/s15516709cog1202_4. Disponível em: https://doi.org/10.1207/s15516709cog1202_4. Acesso em: 4 nov. 2026.
4. MAYER, Richard E. The multimedia principle. In: MAYER, Richard E.; FIORELLA, Logan (org.). *The Cambridge Handbook of Multimedia Learning*. Cambridge: Cambridge University Press, 2021. Disponível em: https://www.cambridge.org/core/books/abs/cambridge-handbook-of-multimedia-learning/multimedia-principle/D09A773C7C5C214FA19D4C9841FBC83B. Acesso em: 4 nov. 2026.
5. MAYER, Richard E.; MORENO, Roxana. Nine ways to reduce cognitive load in multimedia learning. *Educational Psychologist*, v. 38, n. 1, p. 43-52, 2003. DOI: 10.1207/S15326985EP3801_6. Disponível em: https://www.tandfonline.com/doi/abs/10.1207/S15326985EP3801_6. Acesso em: 4 nov. 2026.
6. MEYER, Erin. *The Culture Map: Breaking Through the Invisible Boundaries of Global Business*. New York: PublicAffairs, 2014. Apresentação oficial disponível em: https://erinmeyer.com/books/the-culture-map/. Acesso em: 4 nov. 2026.
7. DILTS, Robert B. *Levels of Learning and Change*. In: *NLPU 100: NLP Practitioner Certification Course Booklet*, p. 13-15. [s.d.]. Disponível em: https://www.nlpu.com/FoundationSample/NLPU100Doc/NLPU%20100%20Levels%20of%20Learning-s.pdf. Acesso em: 4 nov. 2026.
8. STURT, Jackie et al. Neurolinguistic programming: a systematic review of the effects on health outcomes. *British Journal of General Practice*, v. 62, n. 604, p. e757-e764, 2012. DOI: 10.3399/bjgp12X658287. Disponível em: https://pubmed.ncbi.nlm.nih.gov/23211179/. Acesso em: 4 nov. 2026.
9. AGENT SKILLS. *Specification*. [s.d.]. Disponível em: https://agentskills.io/specification. Acesso em: 4 nov. 2026.
10. OWASP. *LLM01:2025 Prompt Injection*. 2025. Disponível em: https://genai.owasp.org/llmrisk/llm01-prompt-injection/. Acesso em: 4 nov. 2026.
11. OPENAI. *Skills no ChatGPT*. 2026. Disponível em: https://help.openai.com/pt-br/articles/20001066-skills-in-chatgpt. Acesso em: 4 nov. 2026.
12. OPENAI. *Build skills: Give ChatGPT and Codex new capabilities and expertise*. [s.d.]. Disponível em: https://learn.chatgpt.com/docs/build-skills. Acesso em: 4 nov. 2026.
13. GOOGLE. *Criar e gerenciar habilidades para os apps do Gemini*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/17094296?hl=pt-br. Acesso em: 4 nov. 2026.
14. GOOGLE. *Agent skills: Google Antigravity Docs*. [s.d.]. Disponível em: https://antigravity.google/docs/skills?app=antigravity-ide. Acesso em: 4 nov. 2026.
15. ANTHROPIC. *Como criar habilidades personalizadas*. [s.d.]. Disponível em: https://support.claude.com/pt/articles/12512198-como-criar-habilidades-personalizadas. Acesso em: 4 nov. 2026.
16. ANTHROPIC. *Extend Claude with skills*. [s.d.]. Disponível em: https://code.claude.com/docs/en/skills. Acesso em: 4 nov. 2026.
17. XAI. *Skills in web, iOS, and Android*. 18 maio 2026. Disponível em: https://x.ai/news/grok-skills. Acesso em: 4 nov. 2026.
18. XAI. *Skills, Plugins & Marketplaces*. [s.d.]. Disponível em: https://docs.x.ai/build/features/skills-plugins-marketplaces. Acesso em: 4 nov. 2026.

**Limite do registro:** estas referências reproduzem o conjunto bibliográfico apresentado na resposta de 04/11/2026. O arquivo não é prova de que cópias integrais das páginas ou artigos foram arquivadas ou de que resultados empíricos do AXI foram obtidos.

◌ AXI · wilkermaa@gmail.com
