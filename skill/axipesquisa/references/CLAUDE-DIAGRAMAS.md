# Claude Web — visual próprio na microfase I

**Regra AXI:** ler o pacote inteiro em fases A/X/I conforme `references/FLUXO-LEITURA-INTEGRAL.md` e, ao atingir I — Diagramação do Fluxo de Aplicação, **acionar visual personalizado HTML/SVG diretamente no chat**, usando os recursos que a sessão realmente permite. **Visuais personalizados** da Anthropic produzem fluxo inline; para persistência e edição, usar **Artifact com prévia renderizada**. Preferir visuais nativos, sem construir HTML extenso desnecessário.

1. Preparar nós, decisões, conexões e rótulos somente a partir de informações verificadas.
2. Acionar o visual personalizado no chat; conferir a figura. Se não funcionar e houver suporte, criar Artifact HTML/SVG **com prévia efetivamente renderizada**, não apenas fonte.
3. Verificar se a imagem aparece e se o diagrama preserva nós/arestas. Quando precisar manter o visual, usar opção de salvar como Artifact ou exportação SVG/HTML; **não exigir download** sem solicitação.
4. Se só houver código/texto ou recurso indisponível, registrar **entrega parcial**, não declarar renderização. Instruções de Skill não abrem ferramentas indisponíveis.
5. Preservar ABNT em toda explicação ou pesquisa e a verificação de normas aplicáveis independentemente do gráfico.

**Aceite:** visual personalizado ou Artifact visível. **Não aceito:** bloco de HTML/SVG textual sem prévia.

**Fonte técnica consultada na elaboração, não repetir automaticamente como fonte de respostas:** ANTHROPIC. *Visuais personalizados no chat e Cowork*. 2026. Disponível em: https://support.claude.com/pt/articles/13979539-visuais-personalizados-no-chat-e-cowork. Acesso em: 11 nov. 2026.

