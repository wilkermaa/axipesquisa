# axipesquisa · AXI

**Versão 2.2.0-rc2 · candidata a avaliação pública (não validada cientificamente como método completo)**

Skill de pesquisa e explicação em português que organiza respostas em três operações editoriais:

> **A — Análise:** o que é o todo, quais são as partes, seus limites e suas funções?
>
> **X — eXpansão:** como suas relações se comparam com outras situações, distinguindo analogia e prova?
>
> **I — Integração:** como as partes se articulam, em quais condições, com quais resultados e usos?

## Valor, hipótese e restrições

O AXI pode ser útil para estruturar uma análise, orientar exemplos e tornar relações mais visíveis. **Não há, até esta versão, experimento que demonstre desempenho superior do AXI em relação a explicações convencionais.** A fundamentação disponível diz respeito a **componentes** análogos (decomposição, analogia, carga cognitiva), e não à eficácia do método completo. Veja [evidências e limites](docs/EMBASAMENTO-CIENTIFICO.md).

A skill não é motor de busca, árbitro da verdade, substituto de especialista, sistema antialucinação nem proteção infalível contra prompt injection. Não inclui scripts executados pelo agente ou acesso ampliado a ferramentas.

## Instalação

- A pasta canônica é [`skill/axipesquisa`](skill/axipesquisa), contendo `SKILL.md` e materiais auxiliares.
- Para ChatGPT Web, Gemini Web, Grok Web, Claude Web, Codex, Antigravity, Grok Build e Claude Code, consulte [compatibilidade e instalações](docs/PLATAFORMAS.md).
- O script `python scripts/build.py` produz oito pacotes de distribuição em `dist/`; ZIPs são apenas um meio de transporte quando a plataforma exige pasta local.
- **ChatGPT Web:** contas qualificadas Business/Enterprise/Healthcare/Edu podem carregar Skill do computador em Plugins > Skills; isso é **diferente** de publicar Plugin para o Diretório. O pacote `dist/AXI-ChatGPT-Plugin-v2.2.0-rc2.zip` é apenas um candidato para submissão. Para contas sem acesso, há [`alternativas/CHATGPT-INSTRUCOES.md`](alternativas/CHATGPT-INSTRUCOES.md) (dependência da interface).

## Como responder

Nas explicações, iniciar por `Orientação AXI aplicada` e interpretar o pedido; quando apropriado, usar A/X/I, um exemplo útil, seção **Fontes consultadas (ABNT)** e assinatura **◌ AXI · nome ou e-mail escolhido pelo usuário**. Uma saída estritamente em JSON, CSV, código, SQL ou outro artefato de formato fechado **não** deve ganhar rodapé que a invalide.

Bibliografia = fontes **efetivamente consultadas naquela resposta**, não referências incluídas automaticamente neste projeto. Não inventar acesso, títulos, datas, URLs, provas ou dados pessoais. A versão pública contém somente `config.example.json` com campos neutros.

## Auditoria e testes

- [RED TEAM: riscos, evidências e mitigação](docs/RED-TEAM.md)
- [Protocolo de experimento A/B](docs/PROTOCOLO-EMPIRICO.md)
- [Rastreabilidade e fontes](docs/FONTES-CONSULTADAS-ABNT.md)
- [Guia de publicação no GitHub](docs/PUBLICACAO.md)
- [Segurança](SECURITY.md)

### Reproduzir verificações locais

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/build.py
```

Esses testes validam **estrutura e regras textuais**, não o comportamento de um modelo. Os 36 cenários têm um executor API em `scripts/run_eval.py` com três condições, avaliações humanas em `scripts/eval_review.py` e verificação parcial em `scripts/check_outputs.py`. **Zero execuções em modelos reais foram realizadas neste ambiente**. Consulte [status](docs/STATUS-DAS-PENDENCIAS.md) e [como executar](docs/EXECUCAO-DO-EXPERIMENTO.md). Testes nativos em plataformas Web e estudo de compreensão com leitores também permanecem necessários.

## Colaboração e autoria

O AXI é uma composição editorial original proposta por seu criador. Citações de Descartes, Gentner, Sweller, Mayer, Meyer e Dilts são **atribuições de influências distintas**, não endosso, parceria ou reivindicação de propriedade sobre suas teorias. Não há licença de redistribuição escolhida nesta versão (veja [opções para decisão](docs/LICENCA-PARA-DECISAO.md)): antes de publicar para reutilização por terceiros, decidir a licença e registrar seu titular em `LICENSE` (veja [licenciamento](docs/LICENCIAMENTO.md)).

**Estado do release:** candidato auditado estruturalmente; sujeito a verificação empírica, compatibilidade e escolha de licença.

## Verificação científica e distribuições (04/11/2026)

- [Status das quatro pendências](docs/STATUS-DAS-PENDENCIAS.md)
- [Procedimento de avaliação em modelos reais](docs/EXECUCAO-DO-EXPERIMENTO.md)
- [Compatibilidade ChatGPT Skill vs Plugin](docs/COMPATIBILIDADE-CHATGPT-2026.md)
- [Licença: decisão expressa](docs/LICENCA-PARA-DECISAO.md)
- [Instrumentos de avaliação](evals/README.md)

Não há alegação de desempenho, superioridade ou segurança absoluta. O executor é um ensaio **prompt-equivalente sem ferramentas**, diferente da integração nativa da Skill.
