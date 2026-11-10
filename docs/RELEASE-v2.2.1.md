# AXI-Pesquisa v2.2.1 | Notas de versão

**Tag Git:** `v2.2.1`  
**Tipo:** correção de defeitos (patch), sem `rc`  
**Autor original:** Wilker M. de Araujo Alexandre  
**Data da preparação:** 10/11/2026

## Corrigido

- Consolidação da regra de visualização da Integração (I): pedido explícito de diagrama deve levar à tentativa real de renderização.
- Quando a interface suporta arquivos, gerar SVG/PNG verificáveis. Caso contrário, fornecer Mermaid válido e explicar a limitação específica.
- Em reconstruções com motor diferente de Mermaid, registrar a equivalência sem afirmar renderização nativa.
- Cores de status acessíveis e somente com estados comprovados, sem inventar estados de projeto.
- Nomenclatura dos instaladores e metadados uniformizada para `2.2.1`, sem RC.

## O que não está comprovado

- Execução da Skill em todas as oito plataformas.
- Renderização e exportação reais no Gemini após a correção.
- Superioridade científica do AXI; o estudo está pendente.

## Instalação

Os instaladores correspondem a `dist/axipesquisa-2.2.1-<plataforma>.zip`. Consulte `docs/PLATAFORMAS.md`. O código-fonte GitHub é outro pacote; não instalar a skill a partir de um ZIP completo do repositório.

## Licenciamento

Código-fonte original: MIT (`LICENSE`). Documentação e textos autorais: CC BY 4.0 (`LICENSE-CONTENT.md`). Material de terceiros retém sua própria titularidade.

## Tag

No GitHub, criar a tag **v2.2.1** sobre o commit contendo o código desta versão. A tag não existe no repositório remoto enquanto não for publicada.
