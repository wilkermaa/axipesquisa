# Diagramação do Fluxo de Aplicação — gestão visual por resultado (v2.3.2)

**Escopo exclusivo:** esta política se aplica à microfase **Diagramação do Fluxo de Aplicação**, sob a **fase I — Integração**, nível de **Gestão e Coordenação**. Não obriga imagens nas fases A e X nem altera pedidos explícitos de outros visuais.

## Contrato funcional

1. **Acionamento:** se houver fluxo identificável e fielmente representável, exigir tentativa de **diagrama real mesmo sem pedido explícito**. Sem fluxo, não desenhar processo fictício.
2. **Gestão e Coordenação:** especificar resultado, relações, decisões, atores, fidelidade, acessibilidade, custo e verificação. **Não prescrever tecnologia específica**.
3. **Execução pela IA:** escolher autonomamente o recurso visual efetivamente disponível na sessão — recurso nativo, Mermaid, SVG, HTML/preview, PNG ou nova tecnologia. **Não obrigar Mermaid, SVG, HTML, Canvas, PNG**, e não impor uma ordem rígida.
4. **Custo:** entre escolhas funcionais, diminuir tokens, código, chamadas, passos, rede e conversões. Uma tentativa principal mais, quando viável, uma alternativa; sem ferramentas pagas de sondagem.
5. **Aceite:** visual exibido na interface, prévia verificável ou arquivo gráfico real acessível. Somente código ou somente texto = **saída parcial**, não visual concluído.
6. **Falha:** registrar recurso efetivamente tentado, impedimento observado e alternativa manual quando cabível. Não inventar ferramentas ou êxito, nem pressupor que o usuário abriu um arquivo.
7. **Confiabilidade:** preservar nós, arestas, decisões, unidades, privacidade, acessibilidade e estado dos dados; nenhuma transmissão externa não autorizada.

## Matriz conceitual, sem amarras de implementação

| Conteúdo | Resultado | Seleção pela IA |
|---|---|---|
| Fluxo fiel | Diagrama de relações/decisões | Qualquer renderizador visual realmente utilizável na sessão |
| Relações estáticas | Estrutura, sem cronologia falsa | Grafo/representação se útil, sem forçar dinâmica |
| Valores quantitativos pertinentes | Gráfico fiel, com escalas e unidades | Meio numérico adequado que a IA consiga exibir |
| Nenhuma ferramenta gráfica | Declaração de limitação + fonte, **saída parcial** | Sem fingir imagem entregue |

**Mensuração:** observar visual exibido, prévia, arquivo acessível, custo incremental e falhas nas interfaces reais; testes estáticos não verificam frontends. C0/C1/C2 v2.2.0-rc2 congelado.

