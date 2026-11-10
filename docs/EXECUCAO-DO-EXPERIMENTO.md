# Execução do benchmark AXI com modelos reais

Os testes precisam ocorrer em um computador com conexão, créditos API e credenciais próprias. **Nunca envie uma chave de API por chat nem coloque credenciais no GitHub**. Guarde-as em variáveis de ambiente locais ou gerenciador de segredos.

## 1. Seleção de modelo

Escolha um modelo real e disponível no provedor. Não trate a versão de um modelo na API como idêntica à versão no aplicativo Web; elas podem usar instruções, ferramentas e configurações diferentes.

Os provedores suportados pelo executor são `openai`, `anthropic`, `gemini`, `xai`. Use o mesmo modelo por bloco e mantenha separados testes feitos em datas ou configurações distintas.

## 2. Preparação sem custos

```bash
python scripts/run_eval.py prepare --provider openai --model SEU_MODELO_REAL --repeats 2 --output evals/openai-manifest.jsonl
```

Isso produz **216 tarefas**: 36 casos × 3 condições × 2 repetições. Se executar um modelo em cada um dos quatro provedores, serão 864 requisições. Selecione volume e orçamento antes de rodar. A execução é sequencial e pode gerar cobrança.

## 3. Execução com consentimento explícito

```bash
# Defina OPENAI_API_KEY no seu ambiente local, sem registrá-la em um arquivo versionado
python scripts/run_eval.py run --input evals/openai-manifest.jsonl \
  --output evals/openai-real-responses.jsonl --confirm-billable --max-calls 3
```

Após validar esse teste de pequena escala, repita sem `--max-calls` para todas as tarefas. Resultados completos permanecem em arquivo JSONL e chamadas concluídas com sucesso não serão repetidas ao reiniciar. Caso edite a Skill, gere um novo manifesto; o runner protege contra prompts trocados após preparação.

Os nomes de variáveis são `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, `XAI_API_KEY`. Não use dados reais de pacientes ou outros registros privados como prompts de teste.

## 4. Verificação determinística parcial

```bash
python scripts/check_outputs.py --input evals/openai-real-responses.jsonl \
  --output evals/oracles.jsonl
```

Somente T17, T18, T19, T20, T29 e T34 têm oráculos automáticos; os demais **precisam de revisão humana e verificação factual externa**. Oráculos simples não medem qualidade científica.

## 5. Avaliação humana e cegamento parcial

```bash
python scripts/eval_review.py prepare --input evals/openai-real-responses.jsonl --output evals/review
```

Envie aos avaliadores apenas `blind_responses.csv` e um modelo limpo de `ratings_template.csv`. **Não** entregue `PRIVATE_BLIND_KEY.json`; ele contém o mapeamento das condições. Como o AXI usa títulos distintivos, o cegamento é parcial; isso deve constar no artigo. Recolha avaliações de **dois avaliadores independentes** e identifique o avaliador em cada registro.

Preencha as notas 0 a 4 nos critérios factual, whole_parts, analogy_limits, integration, clarity, format, sources e safety. Use campos vazios quando a dimensão não se aplica; marque falhas críticas comprovadas. Os avaliadores precisam consultar as fontes originais para aferir precisão, não apenas julgar aparência de correção.

```bash
python scripts/eval_review.py aggregate --key evals/review/PRIVATE_BLIND_KEY.json \
  --ratings evals/review/ratings_filled.csv --output evals/aggregate.json --min-reviewers 2
```

A análise usa comparação pareada e reamostragem por caso; diferenças são **exploratórias**. Para uma alegação de eficácia na compreensão, faça estudo adicional com leitores, questões de transferência e plano de poder amostral pré-definido.

## 6. Avaliação nativa de plataforma

API sem ferramentas não equivale a Skill instalada em interfaces Web. Para cada plataforma, registre: data, versão, modelo visível, método de instalação, evidência de ativação, 36 prompts, saída original, falha e tela (sem dados privados). Registre não disponível em vez de inventar suporte.

## 7. Riscos e limites

- Chamadas são cobradas conforme preços e termos do provedor; não estimamos custo sem modelo e tabela vigentes.
- Sem ferramentas/busca, não teste “fontes efetivamente consultadas” como navegação real; teste se o modelo admite a limitação.
- Mudanças no modelo com o mesmo nome podem afetar replicabilidade; salve a data e metadados devolvidos.
- Condições com comprimentos de instrução diferentes podem influenciar custo e qualidade, e devem ser discutidas como variável de confusão.
- Não alegar resultado favorável sem dados reais. Nunca completar a tabela de notas por previsão ou com respostas sintéticas.
