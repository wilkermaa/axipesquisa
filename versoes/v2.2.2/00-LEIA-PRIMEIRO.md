# AXI-Pesquisa v2.2.2 — Comece aqui

**Autor:** Wilker M. de Araujo Alexandre.
**Estado:** experimental, eficácia científica ainda não demonstrada.
**Licenças:** MIT (código) e CC BY 4.0 (textos originais); consultar o ZIP do repositório.

## Instalação (sem misturar com ZIPs de experimento)

- Gemini Web: `01-INSTALADORES/02-GEMINI-WEB-AXI-v2.2.2.zip`.
- ChatGPT Web: `01-INSTALADORES/01-CHATGPT-WEB-AXI-v2.2.2.zip`.
- Claude Web: `01-INSTALADORES/03-CLAUDE-WEB-AXI-v2.2.2.zip`.
- Outros ambientes: o ZIP correspondente na pasta `01-INSTALADORES` (CLI normalmente exige extração, não upload).
- GitHub: `02-FONTE-GITHUB/AXI-PESQUISA-v2.2.2-CODIGO-PARA-GITHUB.zip` contém os arquivos na raiz. Suba os arquivos extraídos, não o ZIP como arquivo único.

## Correção v2.2.2: Gemini priorizado

Se a interface não renderizar Mermaid, tentar:
1. Produzir SVG vetorial autossuficiente por meio de arquivos do Gemini.
2. Utilizar Gemini Canvas com página HTML e `<svg>` incorporado, usando a prévia visual.
3. Fornecer botões de salvar SVG e PNG quando executáveis no navegador.
4. Se não houver acesso ao Canvas, instruir o usuário: Gemini Web → Adicionar arquivos (+) → Canvas.
5. Se nenhum recurso for possível, fornecer Mermaid e SVG como código, discriminando o que não foi gerado.

A amostra `04-EXEMPLO-GEMINI/ABRIR-NO-NAVEGADOR-COM-BOTOES-SVG-PNG.html` é HTML autocontido, criado como **exemplo**, não demonstra execução do Gemini. O SVG foi validado como XML e rasterizado para PNG por CairoSVG local. A tentativa de capturar prévia com Chromium nesta sessão não foi concluída; os botões de download não foram testados em um navegador interativo nesta etapa.

## Auditoria

- 61/61 testes locais estruturais aprovados; todos os oito instaladores contêm `SKILL.md` idêntico.
- 0 execuções reais do Gemini com a nova skill realizadas por este pacote.
- Os 36 cenários do benchmark v2.2.0-rc2 continuam congelados e não devem ser substituídos silenciosamente.
