# Publicar AXI no GitHub com cautela

O repositório foi preparado localmente. **Nada foi enviado para o GitHub nesta auditoria.** O objetivo desta pasta é permitir inspeção e publicação voluntária posterior.

## Checklist antes de tornar público

1. Confirmar que conteúdo e fontes podem ser publicados sem expor dados de terceiros.
2. Decidir se a autoria será creditada a pessoa física, organização ou pseudônimo; evitar contato pessoal inadvertido.
3. Conferir `LICENSE` (MIT), `LICENSE-CONTENT.md` (CC BY 4.0) e `ATTRIBUTION.md`. Crédito público confirmado como `Wilker M. de Araujo Alexandre` em 04/11/2026. Verificar direitos de terceiros antes de tornar público.
4. Rodar `python scripts/validate.py`, `python -m unittest discover -s tests -v` e `python scripts/build.py`.
5. Revisar o resultado dos pacotes e o registro de hashes. Fazer inspeção manual do conteúdo do ZIP.
6. Criar repositório e fazer commit apenas de documentos, skill, testes e ferramentas sem segredos. Não adicionar `.env`, arquivos pessoais ou o histórico antigo que continha e-mail real.
7. Adicionar badge/CI apenas após o workflow executar realmente no GitHub; nunca simular testes de plataforma.
8. Criar uma **pré-versão** `v2.2.0-rc4` com notas de que compatibilidade comportamental e eficácia permanecem não verificadas.
9. Abrir issues separadas para testes reais das oito plataformas, revisão de direitos de terceiros e estudo A/B. O licenciamento MIT + CC BY 4.0 e a autoria pública já foram escolhidos.

## Exemplo local (não executado)

```bash
git init
git add .
git status
git commit -m "AXI 2.2.0-rc4: versão experimental e protocolos para validação independente"
# Após criar um repositório vazio no GitHub e confirmar sua URL:
git remote add origin <URL_DO_SEU_REPOSITORIO>
git branch -M main
git push -u origin main
```

Não cole tokens de acesso em comandos, arquivos ou conversas. O acesso ao GitHub requer autenticação por meios oficiais; nunca inclua o token na documentação.

## Pendências que impedem alegar “blindagem”

- Sem testes reais nas plataformas; compatibilidade é estrutural, não certificada.
- Sem experimento controlado; melhoria de aprendizado não foi demonstrada.
- Autoria pública confirmada em 04/11/2026. Antes de publicar, verificar licenças e direitos de terceiros.
- Prompt injection e alucinação não podem ser completamente eliminados por prompt.
