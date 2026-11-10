# Auditoria adversarial AXI — versão 2.0 → 2.1.0-rc1

**Data:** 4 de novembro de 2026. **Escopo:** inspeção dos 8 ZIPs anteriores, conteúdo do `SKILL.md`, arquivos de referências e configuração pessoal; confronto com literatura e documentação primária; desenvolvimento de verificações estáticas e casos adversariais. **Não** foi feito teste real de comportamento nos oito provedores, *pentest* em produção ou experimento com usuários.

## Convenção

- **Mitigado estaticamente:** texto, estrutura e controles foram alterados; não comprova obediência do LLM.
- **Parcial:** existe mitigação, mas depende da plataforma, de usuário ou ferramenta.
- **Aberto:** requer comprovação externa, decisão humana ou experimento.
- Severidades são juízo técnico do projeto, não pontuação CVSS nem risco medido.

| ID | Severidade | Achado adversarial v2.0 | Mitigação v2.1.0-rc1 | Estado |
|---|---|---|---|---|
| RT-01 | Crítico | Nome/e-mail pessoais embutidos no `assets/CONFIGURACAO-USUARIO.md` de todos os ZIPs. Risco de exposição no GitHub. | Remover a identidade do artefato distribuível, usar `config.example.json` nulo e `.gitignore`. Varredura em testes estáticos. | Mitigado estaticamente; verificar histórico de commits futuro |
| RT-02 | Alto | Apresentar base científica de componentes como prova do protocolo AXI. | Tabela de evidências separa inspiração filosófica, modelo conceitual, evidência empírica indireta e validação AXI ausente. | Mitigado documentalmente; eficácia **aberta** |
| RT-03 | Alto | Modelo de Dilts/PNL interpretado como técnica com eficácia cerebral, pedagógica ou persuasiva demonstrada. | Marcação explícita como heurística opcional, sem promessa de eficácia; revisão Sturt com escopo correto. | Mitigado estaticamente |
| RT-04 | Alto | Metáforas reais/virtuais/metafísicas podem ser forçadas, dando falsa equivalência factual. | Comparar apenas com relevância, mapear relações e explicitar limite. | Mitigado estaticamente; observação real **aberta** |
| RT-05 | Alto | “Integração em movimento” pode produzir causalidade inventada em objetos estáticos. | Exigir apenas relações logicamente aplicáveis, não inventar fluxos, atores ou feedback. | Mitigado estaticamente |
| RT-06 | Alto | Instruções vindas de páginas externas podem tomar o controle (prompt injection). | Fronteira de confiança, isolamento de conteúdo, sem permissão adicional e revisão humana de ações. | **Parcial:** nenhuma defesa textual é invulnerável |
| RT-07 | Alto | Bibliografia ABNT pode conter URLs, datas, títulos ou fontes alucinados. | Fontes somente efetivamente consultadas, metadata confirmada, ausência declarada e referências no corpo. | **Parcial:** depende de checagem na plataforma |
| RT-08 | Alto | Exigir assinatura/rodapé quebra JSON, CSV, código e documentos estritos. | Prioridade para formato solicitado; sem rodapé dentro de artefatos rígidos; validação por parser nos testes. | Mitigado estaticamente |
| RT-09 | Alto | “Todas as fontes” pode revelar títulos de documentos privados e terceiros. | Registrar fontes privadas com descrição genérica e preservar sigilo. | Mitigado estaticamente; revisão de caso **aberta** |
| RT-10 | Médio | Imposição A/X/I prolixa pode prejudicar perguntas simples e acessibilidade. | Ativação por relevância e nível micro/padrão/técnico, com critérios de parada. | Mitigado estaticamente; comparação empírica **aberta** |
| RT-11 | Médio | Oito pacotes validados em ZIP confundidos com compatibilidade operacional; ChatGPT Web pode exigir skill distribuída por plugin, não ZIP avulso. | Estado por ambiente, rotas de instalação, ressalva de disponibilidade e testes reais não executados. | **Parcial:** testes nos serviços abertos |
| RT-12 | Médio | Atribuir perfis a pessoas com base no mapa cultural de Meyer causa estereótipos. | Preferências explícitas e contexto individual, não dedução demográfica. | Mitigado estaticamente |
| RT-13 | Médio | Apoio científico da etapa I não é identificável como hipótese própria. | Declaração de origem autoral e plano comparativo preregistrável. | Mitigado documentalmente; efeito **aberto** |
| RT-14 | Médio | Empacotamento pode transportar arquivos inesperados, caminhos absolutos ou symlinks. | Conjunto permitido, ZIP sem execução, proteção contra traversal e symlinks, hashing e testes de integridade. | Mitigado estaticamente |
| RT-15 | Médio | Reutilização pública sem definição de direitos/licença. | Documento de decisão de licença, sem presumir cessão automática de direitos. | **Aberto:** titular deve escolher a licença |
| RT-16 | Médio | Confundir usuário/nome com autor da skill, vazando e-mail indevido na assinatura. | A identificação é opcional, explicitamente escolhida pelo usuário e não herdada de pacotes públicos. | Mitigado estaticamente |
| RT-17 | Médio | Modelo pode usar “Fontes consultadas” com bibliografia da documentação, mesmo sem pesquisa no atendimento. | Distinguir bibliografia do desenvolvimento e registro efetivo da execução. | Mitigado estaticamente |
| RT-18 | Médio | Publicar um benchmark de teste como prova de conformidade comportamental. | Testes estáticos declarados, cenários adversariais marcados “não executados nos LLMs”, experimento separado. | Mitigado documentalmente |
| RT-19 | Médio | Condições de plataforma mudam; link/ZIP podem deixar de ser aceitos. | README datado e teste de importação obrigatório antes do release final. | **Aberto:** compatibilidade operacional |
| RT-20 | Médio | Métrica subjetiva “parece claro” incentiva respostas convincentes, mas erradas. | Protocolo A/B, precisão independente, tarefas de transferência, controle ativo, avaliadores cegos. | **Aberto:** experimento ainda não executado |
| RT-21 | Médio | Misturar método editorial e autonomia de ferramentas cria falsa garantia de segurança. | Sem scripts nem MCP na skill; documentação de permissões mínimas; revisão humana para ações externas. | Mitigado estruturalmente; segurança residual |
| RT-22 | Baixo | Títulos fixos podem desobedecer tom/formato do pedido. | Títulos e exemplos condicionais, instrução explícita do usuário tem prioridade. | Mitigado estaticamente |

## Testes adversariais incluídos

A pasta `tests/cases.json` contém cenários (não saídas fingidas) para: JSON puro, código, prompt injection em artigo, referência maliciosa, fontes inexistentes, PNL e afirmações universais, perfil cultural indevido, análise de partes controversas, integração causal, assunto abstrato, divulgação de configuração privada, assinatura sem identidade, citações completas, dados não fornecidos, tarefas triviais e contextos profissionais.

`python scripts/validate.py` e `python -m unittest discover -s tests -v` verificam **invariantes estáticos**. Isso detecta ausência de regras/erros de empacotamento; **não** garante que um modelo obedecerá às regras. Um conjunto de avaliações humanas e integração real continua indispensável.

## Critérios de liberação

1. **Gate de segurança estática:** sem informação privada na distribuição pública, sem executáveis ou symlinks no ZIP, YAML válido, manifestos coerentes, integridade verificada.
2. **Gate de funcionamento:** instalação e execução reproduzíveis em cada plataforma marcada “compatível”. Se falhar, registrar a plataforma como “não validada”, sem propaganda de suporte garantido.
3. **Gate científico:** até resultado empírico, informar “metodologia editorial fundamentada indiretamente; eficácia não demonstrada”.
4. **Gate jurídico/editorial:** decidir licença, autoria pública e regime de contribuições antes de promover repositório como projeto aberto para reutilização.

**Veredito de Red Team:** o projeto pode seguir como **candidato público para avaliação**, mas chamar o método de “blindado”, “validado” ou “superior” seria tecnicamente incorreto.
