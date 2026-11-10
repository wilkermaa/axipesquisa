# AXI-Pesquisa v2.2.0-rc3 — COMECE AQUI

**Versão atual de instalação: 2.2.0-rc3 (06/11/2026)**  
**Autor original:** Wilker M. de Araujo Alexandre  
**Situação:** versão experimental, ainda sem validação científica independente do método completo.  
**Destino:** `SOPRO_DEV/AXI-Pesquisa/trunk/` no Google Drive.

## Para instalar a Skill na IA

Abra a pasta `01-INSTALADORES` e escolha exatamente um arquivo:

| Plataforma | Arquivo |
| --- | --- |
| ChatGPT Web | `01-CHATGPT-WEB-IMPORTAR-SKILL-v2.2.0-rc3.zip` |
| Gemini Web | `02-GEMINI-WEB-IMPORTAR-SKILL-v2.2.0-rc3.zip` |
| Claude Web | `03-CLAUDE-WEB-IMPORTAR-SKILL-v2.2.0-rc3.zip` |
| Grok Web | `04-GROK-WEB-USAR-COMO-REFERENCIA-v2.2.0-rc3.zip` (importação ZIP ainda não confirmada) |
| Codex | `05-CODEX-EXTRAIR-NO-PROJETO-v2.2.0-rc3.zip` |
| Claude Code | `06-CLAUDE-CODE-EXTRAIR-NO-PROJETO-v2.2.0-rc3.zip` |
| Antigravity | `07-ANTIGRAVITY-EXTRAIR-NO-PROJETO-v2.2.0-rc3.zip` |
| Grok Build | `08-GROK-BUILD-EXTRAIR-NO-PROJETO-v2.2.0-rc3.zip` |

**Alternativa universal:** `09-AXI-v2.2.0-rc3-TEXTO-PARA-OUTRAS-IAS.md`, para copiar quando a IA não suportar Skills nativas.

Nas versões Web, carregue o ZIP na área própria de Skills/Habilidades **quando disponível na conta**. Não confunda com anexar um arquivo em uma conversa. Em CLI/IDE, extraia para a pasta de Skills específica da plataforma (consulte `02-FONTE-GITHUB/docs/PLATAFORMAS.md` ao descompactar o repositório).

**Atenção:** o projeto anterior contém habilidades v2.0.0, v2.2.0-rc2 e pacotes de benchmark. Não instale o ZIP de experimento como Skill. Substitua/desative habilidades antigas quando a plataforma permitir. Verifique se a Skill instalada informa `version: "2.2.0-rc3"` no `SKILL.md`.

## O que mudou na rc3

Na fase **I. Integração**, a IA recebe orientação explícita para:
1. preferir **Mermaid renderizado** quando ajudar a entender fluxos, decisões, arquiteturas, sequências ou relações;
2. preservar hierarquia clara, conexões legíveis, poucos cruzamentos e precisão;
3. empregar **verde = concluído**, **amarelo = atenção**, **vermelho = bloqueado**, quando suportado, sempre com rótulos;
4. fornecer **SVG e PNG reais para download somente se as ferramentas puderem criá-los**, sem afirmar exportação inexistente;
5. **não gerar diagramas quando texto simples bastar**.

Se o ambiente não exportar diagramas, a Skill pede a fonte Mermaid e uma explicação objetiva da limitação.

## Código-fonte, pesquisas e testes

- `02-FONTE-GITHUB` contém o repositório completo para publicação, mais a política visual em leitura rápida.
- `03-TESTES-E-INTEGRIDADE` contém resultados locais e hashes.
- Testes de código não validam efeitos do método sobre leitores ou modelos Web.
- A investigação comparativa previamente desenhada congelou **v2.2.0-rc2**. Não substituir silenciosamente C2 por v2.2.0-rc3 na coleta oficial; tratar rc3 como uma intervenção distinta, caso venha a ser avaliada.

## Licenciamento

MIT para software original e CC BY 4.0 para documentação e skill textual autoral, com atribuição ao autor, observados direitos de terceiros. Ver avisos no repositório.

## Estado da publicação

Esta entrega salva arquivos no Google Drive. **Não cria commit nem publica no GitHub automaticamente.**
