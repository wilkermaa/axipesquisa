# Relatório histórico de validação (v2.2.0-rc2)

Este documento descreve a versão anterior. Para as versões posteriores, incluindo 2.2.1, consulte o relatório de testes da distribuição trunk.


Data: 04/11/2026. Status: **aprovado estruturalmente, comportamento empírico NÃO verificado**.

## O que foi executado

- `python -m unittest discover -s tests -v`: **31 testes locais aprovados**, após implementação da nova infraestrutura.
- `python scripts/build.py`: oito pacotes de skill individual e um candidato de plugin ChatGPT criados.
- `python scripts/validate.py`: frontmatter e metadados, fontes, regras, ZIPs, integridade, ausência de contatos pessoais na skill pública e pacote de Plugin aprovados.
- Exercícios com fixture de respostas determinísticas para T17, T18, T19, T20, T29 e T34. Isso testa os parsers, **não o comportamento de IA real**.
- Auditoria dos 36 prompts: todos possuem identificador único, expectativa e status `not-run-on-llm`.

## O que não foi executado

- Nenhuma inferência por OpenAI, Anthropic, Gemini ou xAI neste ambiente.
- Nenhuma importação nativa nas interfaces ChatGPT/Gemini/Grok/Claude/Codex/Antigravity/Grok Build/Claude Code.
- Nenhum painel de avaliação com leitores externos, avaliadores cegos ou medidas de compreensão.
- Nenhuma licença foi concedida ou publicação GitHub feita.

## Critérios de liberação propostos

| Gate | Critério | Situação |
|---|---|---|
| Estático | 0 falhas de integridade e ausência de segredos | Aprovado localmente |
| Segurança empírica | Sem divulgação de dados ou comandos perigosos nas execuções adversariais; auditoria humana | Não aferido |
| Formato | T17-T20/T29/T34 aprovados nos modelos reais | Não aferido |
| Factualidade | Revisão humana de afirmações e ABNT contra fonte | Não aferido |
| Comparação | Dados emparelhados AXI vs genérica e sem AXI, com IC | Não aferido |
| Compatibilidade | Importação e uso real por superfície | Não aferido |
| Licenciamento | Titular escolhe e aprova a licença | Pendente |

## Nota sobre representatividade

As 36 tarefas são principalmente **cenários adversariais**. Mesmo que AXI tenha resultados favoráveis nelas, isso não implica aumento de aprendizagem ou compreensão em todos os públicos. Para tal alegação é necessário estudo com leitores e objetivos de aprendizagem independentes.
