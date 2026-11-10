# Política organizacional obrigatória — AXI-Pesquisa

**Vigência:** v2.2.3 em diante. **Responsável pelo projeto:** Wilker M. de Araujo Alexandre.

## Regra fundamental: 1 alteração versionada = 1 versão e 1 tag

1. **Toda modificação versionada no tronco da distribuição**, inclusive correção de erro, documentação, testes, exemplos, referências, licenças ou empacotamento, exige **incrementar a versão SemVer** `MAJOR.MINOR.PATCH` e criar **uma nova tag Git anotada** `vMAJOR.MINOR.PATCH` para o commit exato da entrega.
2. **Não modificar nem substituir tags publicadas.** A tag identifica um commit imutável. Se houver correção após o fechamento, gere outro PATCH e outra tag; não reaproveite a anterior.
3. **PATCH** para correção/restauração/documentação sem alteração intencional do contrato público; **MINOR** para nova função compatível; **MAJOR** para alteração incompatível de contrato. Cada novo release aumenta a versão, mesmo que a mudança seja somente documental.
4. Atualizar em conjunto `VERSION`, `scripts/build.py`, metadados e título de `SKILL.md`, arquivos da versão atual, `CHANGELOG.md` e `docs/RELEASE-vX.Y.Z.md`. Os oito pacotes devem ser reconstruídos a partir da mesma fonte canônica.
5. Antes de criar a tag: executar `python scripts/check_release.py --source`, `python scripts/validate.py`, `python -m unittest discover -s tests -v`, `python scripts/build.py`, revisar direitos/segredos e hashes. **A tag só pode apontar para o commit que passou nas verificações.**
6. `scripts/check_release.py --git-tag` verifica tag anotada `v<versão>` no HEAD; o CI rejeita envio à `main` sem a tag correspondente, desde que o repositório esteja com a política em execução. O CI não garante, sozinho, execução independente em interfaces Web.
7. Em Pull Requests, validar se a nova versão é maior que a versão da base, quando a base Git estiver acessível, e documentar mudanças e impacto de regressão.
8. Quando houver GitHub remoto, publique e verifique a tag na plataforma. **Tag local, bundle Git e pasta no Google Drive não equivalem a tag publicada no GitHub**.
9. No Google Drive: `trunk/00-ATUAL-vX.Y.Z` contém versão corrente, e `trunk/04-TAGS/vX.Y.Z` registra evidências de tag, notas e integridade. Pastas históricas permanecem intactas; um índice na raiz aponta para a atual.
10. Testes científicos comparativos utilizam **versão congelada** (o estudo original permanece na **v2.2.0-rc2**), sem receber modificações retroativas da Skill distribuída; nova hipótese gera novo protocolo/braço experimental.

## Procedimento de release local

```bash
# Edite apenas após definir a próxima versão.
python scripts/check_release.py --source
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/build.py
# Depois, faça commit e crie a tag anotada exata para esse commit.
git add -A
git commit -m "chore: release AXI-Pesquisa vX.Y.Z"
git tag -a vX.Y.Z -m "AXI-Pesquisa vX.Y.Z"
python scripts/check_release.py --git-tag
# Ao publicar, autentique o remoto e envie tag e main.
git push origin refs/tags/vX.Y.Z
git push origin main
```

## Limites da automação

Checks locais verificam consistência e integridade, **não** se a interface Web renderizou diagramas nem se o método é cientificamente superior. Branch protection e CI só valem no GitHub após serem efetivamente instalados/ativados. Nunca alegar tag remota ou release remoto antes de observar confirmação no GitHub.
