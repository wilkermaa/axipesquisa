# AXI: procedimento operacional

**Definição operacional:** AXI é um roteiro editorial para explorar um objeto em três operações complementares: decompor a pergunta e definir a estrutura (A), estabelecer pontes úteis com outros domínios sem confundir analogia e prova (X) e reconstruir relações e possíveis usos (I). O método organiza o que deve ser explicado, não como o modelo produz seu raciocínio interno.

## Entrada, objetivo e nível de detalhe

Interpretar: para quê, o que entregar, situação/contexto e formato de saída. Não pedir esses campos de forma burocrática. Escolher nível de detalhe: micro (1 parágrafo), padrão (3 blocos curtos), técnico (partes, ligações, riscos, fontes). Se faltar apenas um dado essencial, perguntar uma vez; se puder avançar com hipótese declarada e reversível, avançar.

### A — Análise

**Perguntas de referência:**

- O que é o objeto ou fenômeno? O que são seus principais conceitos?
- O que constitui o **todo** neste recorte, e o que fica fora?
- Quais são as **partes** necessárias para explicá-lo? O que é cada uma, sua função e suas dependências?
- Há propriedades do conjunto que não podem ser explicadas pela mera lista de componentes?
- Quais dados são observados, quais são suposições e quais são lacunas?

**Critério de parada:** pare quando uma divisão adicional não ajudar a resolver o pedido. Uma decomposição é um **modelo útil**, não a única ontologia possível. Em termos disputados, apresentar definições alternativas e a escolhida.

### X — eXpansão

Comparar aspectos da análise com um sistema de outra área **porque compartilham uma relação relevante**, não apenas uma aparência. Dar para cada comparação: (1) domínio de origem e alvo, (2) mapeamento, (3) onde falha, (4) insight resultante. Essa cautela é coerente com a teoria de mapeamento de estrutura de Gentner (1983), sem declarar que AXI é extensão validada dela.

**Exemplos:** conceito de autenticação versus porteiro (real); fila versus buffer de mensagens (virtual); controle de versão versus histórico de alterações (conceitual); identidade computacional versus identidade pessoal (filosófico, sem equivalência ontológica). Se o pedido não envolve metafísica, não a acrescente artificialmente.

### I — Integração

A partir dos componentes, explicar **relações observáveis e condições**: quem usa o quê, por quais regras, onde entram dados, onde saem resultados, quais mudanças propagam efeitos e como reconhecer erro. Se o assunto for um teorema, um conceito ou uma taxonomia estática, mostrar dependências lógicas em vez de simular um processo temporal. Se o efeito for causal, exigir base apropriada.

**Aplicação:** cenário, pré-condições, ações, resultado esperado, falhas possíveis, como conferir o resultado. Para tarefas abstratas, aplicação pode ser um exercício verificável, e não execução física.

## Exemplo conciso: autenticação web

- **A:** autenticação verifica a identidade apresentada. Partes relevantes: cliente, credenciais, servidor, verificação, token/sessão. Autorização é decisão distinta.
- **X:** comparar com um controle de acesso: identidade se verifica antes de conceder entrada. **Limite:** tokens, riscos criptográficos e revogação não se confundem com um crachá físico.
- **I:** cliente apresenta credenciais → servidor verifica → autentica ou rejeita → emite sessão/token quando cabível → requisições posteriores são verificadas. Requer criptografia, proteção de segredos, expiração e regras de autorização.

## Critérios de qualidade

1. A definição responde à pergunta, não apenas recita palavras.
2. Partes são relevantes e têm papel explicado.
3. Comparação preserva relações e apresenta limite.
4. Integração é compatível com evidência e uso prático.
5. Ausências, incertezas e riscos não ficam escondidos.
6. A extensão é proporcional; o usuário não paga com volume por fazer pergunta simples.
7. Há rastreabilidade quando afirmações dependem de fontes externas.
