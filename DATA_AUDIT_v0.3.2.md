# Auditoria editorial ToolBoxWeb v0.3.2 — 2026-10-19

## Âmbito e limites
- 109 ferramentas mantidas, sem exclusões.
- 97 ferramentas com correcções explícitas nesta revisão; restantes conservadas da v0.3.1.
- 9 ferramentas com **algum atributo** suportado por fonte oficial consultada nesta revisão.
- **Não foi possível verificar documentalmente os cinco atributos das 109 ferramentas.** Os restantes valores continuam editoriais, identificados campo a campo em `field_evidence`.
- `verification.status=pending` é intencional: nenhuma ferramenta é considerada completamente auditada só por ter um atributo confirmado.
- Não foi feito teste de funcionamento/conta de cada website; preços, quotas e políticas podem mudar.

## Distribuição dos dados

- **pricing:** free=68, freemium=40, paid=1
- **license:** mixed=6, open_source=47, proprietary=53, unknown=3
- **offline:** no=54, partial=24, unknown=9, yes=22
- **self_hosted:** no=61, unknown=19, yes=29
- **account_required:** no=55, optional=30, unknown=6, yes=18

## Fontes oficiais efectivamente consultadas nesta revisão
- Ollama: https://github.com/ollama/ollama/blob/main/LICENSE — license
- Penpot: https://github.com/penpot/penpot — license, self_hosted
- AnythingLLM: https://github.com/Mintplex-Labs/anything-llm/blob/master/TERMS_SELF_HOSTED.md — license, self_hosted, offline
- Nextcloud: https://github.com/nextcloud/server/blob/master/contribute/HowToApplyALicense.md — license, self_hosted
- Karakeep: https://github.com/karakeep-app/karakeep — license, self_hosted
- Stirling PDF: https://github.com/Stirling-Tools/Stirling-PDF/blob/main/LICENSE — license, self_hosted
- Open WebUI: https://docs.openwebui.com/license/ — license
- Hoppscotch: https://github.com/hoppscotch/hoppscotch — license, self_hosted
- Bitwarden: https://github.com/bitwarden/server/blob/master/LICENSE.txt — license

## Casos que exigem cuidado
- **Open WebUI**: a licença actual inclui restrições de marca; não apresentar simplesmente como open-source sem ressalvas.
- **Stirling PDF**: projecto open-core com pastas de licença proprietária; classificado `mixed`.
- **Bitwarden**: coexistem componentes AGPL e módulos sob licença Bitwarden; `mixed`.
- **Grátis vs freemium**: serviços com plano gratuito limitado são `freemium`, não `free`.
- **Offline**: o campo refere-se à utilização principal da ferramenta, não à possibilidade de descarregar conteúdos.
- **Self-hosted**: instalar software localmente não é automaticamente equivalente a alojar um serviço.

## Próximo passo técnico
O motor de filtros actual continua compatível. Para uma versão pública, mostrar opcionalmente o estado da evidência em detalhes; não transformar `editorial` em `official` sem consulta documental. Uma auditoria integral requer consulta individual dos 109 fornecedores.
