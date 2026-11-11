# AXI-Pesquisa v2.3.3 — execução gráfica concreta na microfase I

**PATCH | Data:** 11 nov. 2026. **Origem:** correção aprovada com a ressalva de que **PDF não é obrigatório**.

## Escopo

A microfase **Diagramação do Fluxo de Aplicação**, nível Gestão e Coordenação da **fase I — Integração**, exige **tentativa concreta de produzir visual** quando houver fluxo representável fielmente, inclusive sem solicitação explícita. A IA executora escolhe o mecanismo viável (nativo, Mermaid, SVG, HTML/preview, PNG ou outro), sem ordem fixa. Não inventar processos para objetos estáticos nem modificar obrigação das fases A ou X.

## Critério de aceite

**Gráfico exibido na própria conversa, prévia visual verificável ou arquivo gráfico realmente acessível**. Se o gráfico já aparecer na interface, **não exigir PDF, PNG, SVG ou download**. O PDF do teste em Gemini foi somente uma evidência documental que continha `graph TD` como texto; não constitui formato de entrega obrigatório. Texto/código apenas são falha visual ou entrega parcial. Quando houver recurso, realizar ação efetiva; se necessário, uma alternativa acessível; se não houver, registrar impedimento real sem simular sucesso.

## Red team e testes

Registrados 20 cenários em `docs/REDTEAM-MICROFASE-v2.3.3.md`, inclusive custo, privacidade, fidelidade, linguagem, Canvas e risco de confundir teste estático com prova real. Testes locais/CI verificam contrato e pacotes, **não a renderização em Gemini**. A Issue #4 preserva o teste manual relatado; Rafaell poderá homologar a v2.3.3 em sessão real.

**Homologação funcional:** pendente no Gemini e nas outras plataformas; os testes automatizados não demonstram que a interface exibirá o gráfico.

## Governança

Não mover/regravar a tag histórica v2.3.2. O protocolo científico C0/C1/C2 permanece congelado na v2.2.0-rc2. SemVer 2.0.0 segue como referência técnica de engenharia, não prova de eficácia didática/cognitiva.

