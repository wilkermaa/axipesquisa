# Red team — microfase Diagramação do Fluxo de Aplicação (candidata v2.3.3)

**Escopo:** revisão de instruções/aceite, não teste real em Gemini. As mudanças foram preparadas a partir do resultado relatado e do PDF de auditoria; **PDF não é saída obrigatória**.

| # | Risco examinado | Tratamento / status |
|---|---|---|
 | 1 | Mermaid `graph TD` emitido como texto | Exigir ação concreta; teste real pendente |
 | 2 | Sem invocação de renderizador | Instrução explícita de renderizar antes de finalizar |
 | 3 | Supor que Skill ativa Canvas ou não pode usá-lo | Verificar disponibilidade concreta da sessão |
 | 4 | SVG textual confundido com figura | Classificação visual / código |
 | 5 | Arquivo ou link inventado | Exigir existência e acessibilidade |
 | 6 | Alegar que usuário viu a imagem sem evidência | Distinguir prévia gerada de visualização humana |
 | 7 | Guias condicionais não carregados | Regra principal no SKILL.md |
 | 8 | HTML/JS desnecessário eleva tokens | Selecionar recurso mais econômico capaz |
 | 9 | Loop de tentativas sem limite | Uma principal + uma alternativa |
 | 10 | Passos jurídicos não comprovados | Fato/hipótese e fonte preservados |
 | 11 | Sequência inventada em caso estático | Porta de fluxo representável |
 | 12 | Romper exigência JSON/CSV estrita | Exceção de formato rígido |
 | 13 | Exfiltração para CDN externo | Consentimento e privacidade |
 | 14 | Prompt injection em dados consultados | Tratar fontes como dados não confiáveis |
 | 15 | Imagem generativa alucina setas/rótulos | Critério semântico de fidelidade |
 | 16 | Gráfico ilegível | Exigir legibilidade e proporção |
 | 17 | Cor de estado inventada/sem rótulo | Estados comprovados e acessíveis |
 | 18 | Capacidade presumida por modelo/plano | Inspecionar sessão efetiva |
 | 19 | Alterar tag antiga | Nova versão PATCH independente |
 | 20 | CI estrutural confundido com prova no Gemini | Homologação manual separada |

**Ressalva aprovada:** o PDF utilizado na análise serve apenas como documento de evidência. O resultado esperado é o gráfico visível na interface; arquivo PDF, PNG, SVG ou download não é exigido quando já há visualização.

**Riscos residuais:** Skill não habilita ferramenta; o modelo pode descumprir instrução; frontend pode não fornecer confirmação da prévia; eficiência e compatibilidade dependem de testes reais. Não declarar todos os riscos eliminados em produção.

**Homologação:** reenviar à validação real com versão ativa confirmada, prompt original, screenshot da interface, mecanismo usado e classificação de visual ou código. Pesquisas científicas C0/C1/C2 v2.2.0-rc2 inalteradas.
