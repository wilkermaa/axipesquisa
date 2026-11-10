# Publicar AXI no GitHub com cautela

O repositório foi preparado localmente. **Nada foi enviado para o GitHub nesta auditoria.** O objetivo desta pasta é permitir inspeção e publicação voluntária posterior.

## Checklist antes de tornar público

1. Confirmar que conteúdo e fontes podem ser publicados sem expor dados de terceiros.
2. Decidir se a autoria será creditada a pessoa física, organização ou pseudônimo; evitar contato pessoal inadvertido.
3. Escolher licença de código (por exemplo MIT/Apache-2.0) e licença de documentação/skill textual (por exemplo CC BY 4.0 ou outra), **somente com autorização do titular**; incluir arquivo(s) apropriado(s).
4. Rodar `python scripts/validate.py`, `python -m unittest discover -s tests -v` e `python scripts/build.py`.
5. Revisar o resultado dos pacotes e o registro de hashes. Fazer inspeção manual do conteúdo do ZIP.
6. Criar repositório e fazer commit apenas de documentos, skill, testes e ferramentas sem segredos. Não adicionar `.env`, arquivos pessoais ou o histórico antigo que continha e-mail real.
7. Adicionar badge/CI apenas após o workflow executar realmente no GitHub; nunca simular testes de plataforma.
8. Criar uma **pré-versão** `v2.1.0-rc1` com notas de que compatibilidade comportamental e eficácia permanecem não verificadas.
9. Abrir issues separadas para testes reais das oito plataformas, escolha de licença e estudo A/B.

## Exemplo local (não executado)

```bash
git init
git add .
git status
git commit -m "AXI 2.1.0-rc1: hardening e auditoria adversarial"
# Após criar um repositório vazio no GitHub e confirmar sua URL:
git remote add origin <URL_DO_SEU_REPOSITORIO>
git branch -M main
git push -u origin main
```

Não cole tokens de acesso em comandos, arquivos ou conversas. O acesso ao GitHub requer autenticação por meios oficiais; nunca inclua o token na documentação.

## Pendências que impedem alegar “blindagem”

- Sem testes reais nas plataformas; compatibilidade é estrutural, não certificada.
- Sem experimento controlado; melhoria de aprendizado não foi demonstrada.
- Sem licença autorizada; não anunciar distribuição *open source* antes de decidir direitos.
- Prompt injection e alucinação não podem ser completamente eliminados por prompt.
