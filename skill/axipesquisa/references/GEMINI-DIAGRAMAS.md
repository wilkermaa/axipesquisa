# Gemini Web — microfase I: ação de renderização sem formatos obrigatórios

**Objetivo:** quando houver fluxo fiel, produzir gráfico de fato, **mesmo sem pedido explícito**. Essa exigência é da microfase **Diagramação do Fluxo de Aplicação**, subordinada à fase I, não de toda resposta.

**Procedimento mínimo na própria sessão:**

1. Verificar qual recurso visual está **efetivamente acessível nesta conversa**; não presumir capacidade ou incapacidade por nome do modelo, modo de esforço ou documentação geral.
2. A IA executora decide livremente entre prévia nativa, Mermaid renderizado, SVG exibido, HTML com prévia, imagem ou outra opção. **É preciso efetivamente apresentar o gráfico, não escrever `graph TD` ou código-fonte como resposta final.**
3. Se um mecanismo produzir somente código, tentar **uma alternativa habilitada**; se não houver, marcar entrega parcial e explicar o impedimento observado.
4. **Uma figura já visível na tela ou prévia real satisfaz a entrega. PDF não é obrigatório**, tampouco download SVG/PNG sem pedido do usuário. O PDF usado na auditoria da v2.3.2 foi apenas captura/registro da resposta.
5. Se Canvas estiver acessível nesta sessão, utilizá-lo apenas quando a Skill e a interface realmente permitirem; **não declarar impossível com base apenas em documentação**. Se Canvas só estiver acessível numa conversa separada, tratar como opção manual, não sucesso da Skill. Não inventar prévias.
6. Preservar nós, conexões, condições, rótulos, privacidade e incerteza jurídica. Gerador de imagens só é adequado quando preserva a semântica do fluxo; não sacrificar fidelidade por apresentação.

**Regressão de referência:** `@axipesquisa procedimento para mudar a lotação do funcionario na prefeitura de matinhos`. O PDF histórico continha Mermaid em texto sem gráfico visível no documento. Classificar esse documento como evidência de saída textual; verificar **a conversa original** antes de afirmar que nenhuma prévia externa foi aberta.

**Homologação:** capturar versão ativa da Skill, prompt, resposta, recurso acionado, visual efetivamente observado, fidelidade e custo em chamadas/passos. Não confundir aprovação estrutural com funcionamento em produto.

GOOGLE. *Sobre a transição dos Gems para habilidades*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/18560919?hl=pt-BR. Acesso em: 11 nov. 2026.
