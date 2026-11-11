# AXI-Pesquisa v2.3.0 — Política de visualização na Integração

**Novo contrato funcional:** verifique sem custo externo a capacidade real do ambiente e o tipo de informação antes de gerar o visual. Fluxos com renderer Mermaid disponível preferem Mermaid; números com gráfico nativo preferem esse gráfico; se a prévia não estiver habilitada, considerar SVG local ou Canvas. Entre meios equivalentes, minimizar passos, conversões, chamadas e dependências. Não prometer valores de economia ainda não medidos. Consulte `docs/DECISAO-RENDERIZACAO-v2.3.0.md` e `skill/axipesquisa/references/ROTEAMENTO-VISUAL.md`.

O **Mermaid é preferencial para fluxos com prévia comprovada, não obrigatório** quando o usuário não pede um diagrama. Em pedidos explícitos, produzir o artefato visual sempre que as ferramentas efetivamente disponíveis permitirem. A fase I deve decidir primeiro se o texto é suficiente. Somente quando um diagrama esclarecer relações, use a renderização visual suportada pelo ambiente.

- Aplicações: fluxos, árvores de decisão, arquiteturas, diagramas de sequência e redes de relações.
- Clareza: hierarquia legível, poucas conexões cruzadas, nomes precisos, sem efeitos ou relações inventadas.
- Status: verde = concluído; amarelo = atenção; vermelho = bloqueado, apenas quando suportado e com rótulos textuais.
- Acessibilidade: descrição textual equivalente e estados escritos, não somente cores.
- Exportação: preferir SVG, oferecer PNG quando puder produzir; disponibilizar somente links reais verificados.
- Ambiente sem renderizador Mermaid: primeiro verificar outras ferramentas disponíveis de criação visual; só então apresentar código Mermaid e explicar eventuais limitações específicas.
- Privacidade: não usar renderizadores externos com dados restritos sem autorização.
- Escopo: esta atualização é editorial/funcional e **não demonstra superioridade científica**, eficácia de aprendizagem ou compatibilidade comprovada com todas as plataformas.

## Contrato de diagrama solicitado explicitamente (corrigido na v2.2.2)

Quando o pedido tiver termos como "desenhe o Mermaid", "quero o gráfico renderizado", "entregue SVG e PNG" ou equivalente, o requisito muda de **preferência** para **entregável solicitado**.

Procedimento:

1. Usar apenas capacidades habilitadas na sessão. Tentar Mermaid nativo, se existir; caso contrário, tentar criação visual por recursos suportados (por exemplo, Canvas para HTML/SVG ou execução local permitida).
2. Priorizar semântica correta: mesmos nós, conexões, condições e decisões, sem estados fictícios.
3. Gerar **arquivos verificáveis**, não só código. Se SVG e PNG forem criados, fornecer acesso para baixar ambos.
4. Quando outro motor criar o SVG/PNG a partir da semântica do Mermaid, identificar como *reconstrução equivalente*, não como compilação Mermaid.
5. Na impossibilidade real, documentar a tentativa, seu limite e fornecer o código `.mmd`. Não afirmar sem checagem que nenhum arquivo gráfico pode ser produzido.

### Exemplo de aplicação no Gemini Web

A documentação oficial do Google (consulta em 10/11/2026) descreve fluxos em que o Gemini cria arquivos `.svg` e `.png` e o Canvas permite criar código/aplicativos. Isso não comprova que toda conversa possua um renderizador Mermaid. Se houver Canvas, uma solução é produzir um SVG autocontido com os mesmos nós e conexões e disponibilizá-lo para download; PNG pode ser gerado pelos recursos habilitados. Não exigir rede externa nem afirmar que qualquer ferramenta específica existe sem verificar.

Referências:
- GOOGLE. *Gerenciar tarefas e fluxos de trabalho nos apps do Gemini*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/17094507?hl=pt-BR. Acesso em: 10 nov. 2026.
- GOOGLE. *Criar documentos, apps e muito mais com o Canvas*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/16047321?hl=pt-BR. Acesso em: 10 nov. 2026.

## Teste de aceitação manual sugerido (a executar nas plataformas)

Solicite a descrição de um fluxo com decisão e estados; compare se a skill:
1. propõe diagrama apenas se for útil;
2. gera Mermaid válido ou declara indisponibilidade;
3. mantém rótulos para verde/amarelo/vermelho;
4. entrega SVG/PNG somente se os arquivos forem realmente gerados e acessíveis;
5. evita diagramas quando uma resposta textual curta resolve o pedido.

**Importante:** este teste é de aceitação futura; não é declarado como executado nas IAs Web.
