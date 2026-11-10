# AXI-Pesquisa v2.2.1 — Publique no GitHub

**Autor original:** Wilker M. de Araujo Alexandre. **Versão:** 2.2.1 (patch). **Tag:** `v2.2.1`.

## Preencha a tela de criação do GitHub

- Proprietário: `wilkermaa`
- Repositório: `axipesquisa`
- Descrição: `Método AXI (Análise, eXpansão e Integração) para pesquisa, aprendizagem e explicações estruturadas com IA. Skills, documentação e avaliação experimental.`
- Visibilidade: Public
- Adicionar README: Off
- Adicionar .gitignore: No .gitignore
- Adicionar licença: No license

O pacote de código já inclui README, .gitignore, MIT e CC BY 4.0. A existência do endereço Github depende de você concluir a criação.

## Para publicar pelo navegador (sem terminal)

1. Clique em **Create repository** e abra a página do repositório recém-criado.
2. Descompacte `01-GITHUB/AXI-PESQUISA-v2.2.1-CODIGO-PARA-GITHUB.zip` no seu computador.
3. No GitHub escolha `uploading an existing file` ou `Add file > Upload files` e envie o conteúdo descompactado **preservando as pastas** `skill`, `docs`, `tests`, `scripts`, `.github`, `evals`, `alternativas` e os arquivos da raiz. Se o navegador não preservar a hierarquia, use Git CLI.
4. Confira especialmente a presença de `skill/axipesquisa/SKILL.md`, `LICENSE`, `LICENSE-CONTENT.md` e `.github/workflows/ci.yml`.
5. Faça o primeiro commit. O upload de ZIP diretamente não expande os arquivos na raiz: nunca envie só o ZIP do código esperando ver `SKILL.md` no repositório.
6. Abra **Releases > Draft a new release**; em **Choose a tag**, informe `v2.2.1`, escolha **Create new tag on publish** com alvo `main`.
7. Título: `AXI-Pesquisa v2.2.1 | Correções Mermaid e SVG/PNG`; cole as notas de `03-TAG-E-RELEASE/RELEASE-NOTES-v2.2.1.md` e publique quando estiver conferido. A publicação cria a tag no remoto.
8. Anexe como assets opcionais os oito ZIPs da pasta `02-INSTALADORES`.

**Não há necessidade de instalar a Skill no repositório.** As Skills são ZIPs de distribuição, diferentes do código-fonte.

## Para publicar pelo terminal (alternativa)

Depois de criar um repositório vazio e descompactar o ZIP de código:

```bash
cd /caminho/para/arquivos-descompactados
git init -b main
git add .
git status
git commit -m "fix: AXI-Pesquisa 2.2.1 - diagramas Mermaid e SVG/PNG"
git remote add origin https://github.com/wilkermaa/axipesquisa.git
git push -u origin main
git tag -a v2.2.1 -m "AXI-Pesquisa v2.2.1 - correcao Mermaid e exportacao SVG/PNG"
git push origin v2.2.1
```

Verifique seu `git config user.name` e `git config user.email` ANTES de usar o terminal, para não expor um e-mail pessoal indesejado na autoria de commits e tags. Use o endereço noreply disponibilizado na sua conta GitHub, se essa for sua preferência.

## Opção avançada: usar o commit e a tag Git local já preparados

O arquivo `01-GITHUB/AXI-PESQUISA-v2.2.1-TAG-LOCAL.bundle` contém um **commit Git local real** (`f9183a1`) e a tag anotada `v2.2.1`. Foi criado por um empacotador identificado como `AXI-Pesquisa Empacotamento <release@axipesquisa.invalid>` para não usar o e-mail pessoal do autor. Se preferir aparecer como autor do commit na sua conta, use a publicação via navegador ou terminal a partir do ZIP-fonte (não o bundle), com sua configuração Git.

Para enviar **o commit empacotado** a um repositório vazio:

```bash
git clone AXI-PESQUISA-v2.2.1-TAG-LOCAL.bundle axipesquisa
cd axipesquisa
git remote rename origin pacote-local
git remote add origin https://github.com/wilkermaa/axipesquisa.git
git push -u origin main
git push origin v2.2.1
```

Não use o fluxo de bundle **junto com** upload manual do mesmo conteúdo; são **alternativas** que produzem commits distintos. A tag publicada deve apontar ao commit escolhido.

## Estado de validação

- 47 verificações automatizadas locais aprovadas (estrutura, pacotes, regras textuais).
- Nenhum teste nativo Web comprovado para todos os oito instaladores.
- Nenhuma superioridade científica demonstrada. Rafaell pode coordenar o estudo, com avaliações humanas independentes.
- O estudo A/B anterior mantém o prompt AXI `2.2.0-rc2` congelado para preservar o desenho experimental.

## Cuidado com a tag

A tag deve apontar para o **commit de conteúdo 2.2.1**. Arquivos do GitHub e pacotes de instalação não são equivalentes. GitHub e Google Drive não compartilham tags automaticamente.
