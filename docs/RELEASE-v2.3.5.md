# AXI-Pesquisa v2.3.5 — regressão jurídica e citações ABNT

**Classificação:** PATCH. **Data:** 11 nov. 2026. **Escopo:** correção de instruções e testes. A alteração não substitui a microfase I nem muda o experimento congelado.

## Problema observado

Resposta do Gemini ao pedido de mudança de lotação de servidor em Matinhos apresentou A–X–I e um fluxo em texto, **sem seção Fontes consultadas (ABNT)**, sem citação de artigos e com afirmações não comprovadas sobre procedimentos como portaria universal, participação da Procuradoria e prazos. Ainda alegou ausência de ferramenta gráfica apesar de o autor relatar recursos disponíveis. Não confundir texto gerado com prova de pesquisa ou renderização.

## Contrato corrigido

- **Direito/administrativo:** consultar legislação vigente e específica, priorizando fonte oficial, quando houver ferramenta acessível; vincular regras a número/ano/artigo/parágrafo e distinguir lei, prática local e hipótese. Se a fonte oficial não foi consultada, informar essa limitação. Não inventar referências ou atos.
- **ABNT:** referenciar toda fonte efetivamente consultada e citada perto dos dispositivos, apresentar lista ABNT ao final das explicações. Se não houver acesso a fontes, declarar falta de verificação, sem inventar URL ou bibliografia.
- **Diagramação I:** se o rito foi verificado e existe fluxo fiel, acionar efetivamente visual no Gemini (SVG renderizado quando possível, alternativa PNG/nativa); não aceitar código ou setas textuais como figura; PDF opcional. **Pesquisa, ABNT e visual são deveres independentes**.
- **Caso de regressão:** a Lei nº 1.165/2008 de Matinhos, art. 57, distingue portaria para remoção entre secretarias e ofício dentro da mesma secretaria; §§ 1º–3º estabelecem qualificações importantes. A confirmação municipal oficial do texto atualizado não foi obtida nesta revisão; a comparação foi feita com compilação externa.

## Testes, limitações e governança

CI verifica contrato textual, regressões e integridade de oito ZIPs. **Não prova que o Gemini navegou em fonte oficial, verificou a legislação ou renderizou o gráfico em sua UI**. Homologação real pendente na Issue #4. As tags/ativos anteriores permanecem íntegros; referência SemVer 2.0.0 técnica; protocolo científico C0/C1/C2 v2.2.0-rc2 inalterado.

## Fonte consultada no desenvolvimento (ABNT; não transferir automaticamente às respostas da Skill)

MATINHOS. *Lei nº 1.165/2008: Estatuto dos Servidores Públicos do Município de Matinhos*. 2008. Versão compilada por terceiro, com alterações declaradas até 13 mar. 2026. Disponível em: https://leggicomunali.it/estatuto-do-servidor-funcionario-publico-matinhos-pr. Acesso em: 11 nov. 2026.

