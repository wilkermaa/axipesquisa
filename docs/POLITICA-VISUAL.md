# AXI-Pesquisa v2.2.0-rc3 — Política de visualização na Integração

O **Mermaid é preferencial, não obrigatório**. A fase I deve decidir primeiro se o texto é suficiente. Somente quando um diagrama esclarecer relações, use a renderização visual suportada pelo ambiente.

- Aplicações: fluxos, árvores de decisão, arquiteturas, diagramas de sequência e redes de relações.
- Clareza: hierarquia legível, poucas conexões cruzadas, nomes precisos, sem efeitos ou relações inventadas.
- Status: verde = concluído; amarelo = atenção; vermelho = bloqueado, apenas quando suportado e com rótulos textuais.
- Acessibilidade: descrição textual equivalente e estados escritos, não somente cores.
- Exportação: preferir SVG, oferecer PNG quando puder produzir; disponibilizar somente links reais verificados.
- Ambiente sem renderizador: usar bloco de código Mermaid, sem afirmar que gerou o diagrama ou seus arquivos.
- Privacidade: não usar renderizadores externos com dados restritos sem autorização.
- Escopo: esta atualização é editorial/funcional e **não demonstra superioridade científica**, eficácia de aprendizagem ou compatibilidade comprovada com todas as plataformas.

## Teste de aceitação manual sugerido (a executar nas plataformas)

Solicite a descrição de um fluxo com decisão e estados; compare se a skill:
1. propõe diagrama apenas se for útil;
2. gera Mermaid válido ou declara indisponibilidade;
3. mantém rótulos para verde/amarelo/vermelho;
4. entrega SVG/PNG somente se os arquivos forem realmente gerados e acessíveis;
5. evita diagramas quando uma resposta textual curta resolve o pedido.

**Importante:** este teste é de aceitação futura; não é declarado como executado nas IAs Web.
