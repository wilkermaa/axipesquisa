# Relatório histórico: verificações locais da AXI v2.1.0-rc1

**Atenção: relatório histórico de 2.1.0-rc1. Não representa o status da release 2.2.0-rc2.**

Data: **04/11/2026**. Este arquivo é um registro de validação estrutural realizada localmente, não auditoria independente de eficácia.

- Foram examinados os 8 ZIPs históricos da v2.0 e seus conteúdos fundamentais para localizar dados pessoais, regras frágeis e riscos epistemológicos.
- O Red Team documental catalogou **22 achados** com mitigação e status de risco residual; consulte `RED-TEAM.md`.
- Foram preparados **36 casos adversariais** em `tests/cases.json`. **Nenhum desses casos foi executado nos serviços de LLM**.
- O teste `python -m unittest discover -s tests -v` terminou com **22 testes automatizados aprovados** nesta execução.
- O comando `python scripts/validate.py` aprovou o frontmatter YAML do `SKILL.md`, integridade e paths dos **8 ZIPs**, ausência de e-mails no material público da skill e presença dos módulos principais.
- Todos os ZIPs foram escritos de forma determinística, com entradas limitadas a textos Markdown/JSON nos pacotes de skill, sem executáveis ou symlinks.
- O relatório de hashes SHA-256 é `dist/manifest-sha256.json`, gerado por `python scripts/build.py`.

## O que NÃO foi demonstrado

1. Que oito plataformas aceitam os ZIPs nas respectivas interfaces.
2. Que os modelos obedecem aos 36 cenários adversariais.
3. Que AXI é empiricamente mais eficaz, cientificamente validado ou imune a prompt injection/alucinação.
4. Que havia licença aberta e autorização final de publicação naquela versão histórica. A decisão de MIT + CC BY 4.0 e a identificação pública do autor foram registradas posteriormente, na 2.2.0-rc2.

**Recomendação histórica:** não publicar a 2.1.0-rc1 como produto “blindado” ou “comprovado”. Para o release atual, consultar `STATUS-DAS-PENDENCIAS.md` e `PUBLICACAO.md`.
