# AXI-Pesquisa v2.3.7 — Canvas como ferramenta de saída (Gemini)

**Classificação:** PATCH. **Data:** 11 nov. 2026. **Escopo:** ajuste cirúrgico na microfase Diagramação do Fluxo de Aplicação, fase I — Integração, sem modificar método A/X/I, normas jurídicas ou bibliografia ABNT.

## Requisito esclarecido pelo autor

A Skill **não precisa executar dentro do Canvas**. Ela deve coordenar a demanda, preparar nós/conexões com fontes verificadas e **solicitar/acionar Canvas** como ferramenta de saída, para **criar HTML com SVG inline e abrir a Prévia visual**. A prévia é o objetivo; não é necessário exportar PDF, baixar PNG/SVG ou realizar interação posterior do usuário para ter um resultado visual.

## Sequência operacional

1. Ler e aplicar a Skill integralmente, conforme A → X → I; pesquisar as normas aplicáveis antes de fazer fluxograma jurídico e documentar fontes ABNT.
2. No Gemini, transmitir ao Canvas somente a descrição verificada do fluxo e solicitar **SVG renderizado em Prévia**. **Acionar de fato o recurso, quando estiver habilitado**, não apenas escrever `flowchart TD`.
3. Verificar **figura real na tela** e fidelidade das relações. A existência de botão Canvas **não comprova que foi acionado**.
4. Se a chamada à ferramenta Canvas for recusada ou não abrir Prévia, registrar o problema real e tentar visual SVG/PNG acessível; nenhuma imagem = entrega parcial.

## Limitação externa e honestidade técnica

A ajuda oficial do Google informa que Skills **ainda não funcionam com Canvas**, incluindo Canvas na lista de ferramentas indisponíveis para Skills. Isso é evidência de restrição de compatibilidade, **não** de que o controle Canvas esteja ausente da conversa. A orientação para tentar chamar Canvas é o **comportamento requisitado**, **não uma comprovação de interoperabilidade**. O teste da sessão real com Skill ativa e captura de tela é necessário; não anunciar capacidade nem êxito não observado.

## Verificação e governança

CI e testes verificam contrato textual, empacotamento de oito instaladores e hashes. **Não executam o Gemini real** nem provam a chamada Canvas. A homologação funcional continua na Issue #4; o espelhamento Drive, na Issue #6. Tags anteriores e protocolo C0/C1/C2 v2.2.0-rc2 intactos.

## Fontes técnicas consultadas (ABNT)

GOOGLE. *Sobre a transição dos Gems para habilidades*. 2026. Disponível em: https://support.google.com/gemini/answer/18560919?hl=pt-BR. Acesso em: 11 nov. 2026.

GOOGLE. *Crie documentos, apps e muito mais com o Canvas*. [s.d.]. Disponível em: https://support.google.com/gemini/answer/16047321?co=GENIE.Platform%3DDesktop&hl=pt. Acesso em: 11 nov. 2026.
