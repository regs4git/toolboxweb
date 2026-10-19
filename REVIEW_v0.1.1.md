# ToolBox — Revisão editorial da Fase 1 (v0.1.1)

## Âmbito
Revisão estrutural e editorial do catálogo existente, sem auditoria online exaustiva. Não foram adicionados nem eliminados sites.

## Distribuição por domínio principal
| Domínio | Ferramentas |
|---|---:|
| Pesquisa e conhecimento | 11 |
| IA e assistentes | 10 |
| Programação e desenvolvimento | 15 |
| Imagem e design | 13 |
| Vídeo e animação | 2 |
| Segurança e privacidade | 12 |
| Documentos e PDFs | 7 |
| Partilha e armazenamento | 6 |
| Áudio e música | 10 |
| Línguas e comunicação | 4 |
| Organização e produtividade | 5 |
| Internet e utilitários | 9 |
| Cinema e entretenimento | 2 |
| Redes e servidores | 2 |
| Educação e aprendizagem | 1 |
| Negócios e marketing | 0 |

## Melhorias efectuadas
- Grupos de checkboxes definidos para todos os 16 domínios, incluindo o domínio Negócios (actualmente vazio).
- Domínios secundários acrescentados a ferramentas com utilizações transversais.
- Termos de pesquisa derivados de nome e funcionalidades; podem ser refinados na Fase 2.
- Validador reforçado para grupos, valores dos filtros e consistência do domínio principal.
- Mantidos os 20 Top editoriais provisórios, sem confundir com favoritos pessoais.

## Questões identificadas para decisão
- O catálogo contém ferramentas instaláveis e self-hosted (ex.: GIMP, KeePassXC, Ollama), apesar de o âmbito declarado ser «websites». Sugestão: manter links para os websites oficiais e adicionar futuramente um atributo `delivery` (web/app/serviço), sem excluir já as ferramentas.
- Alguns domínios estão pouco representados (Educação, Entretenimento, Infraestrutura) e Negócios está vazio. A UI deve ocultar domínios vazios por defeito.
- Faltam verificações externas de preços, licenças, plataformas, idiomas, contas e capacidades actuais. Todos os atributos incertos continuam `unknown`.
- A árvore de filtros já existe, mas a lógica de AND/OR e correspondências parciais será implementada na Fase 2.
- A lista anterior é a fonte desta revisão; confirmar a correspondência com a lista original de URLs caso se pretenda auditoria de proveniência rigorosa.

## Critério de aceitação
Executar `python3 validate.py` no directório do catálogo.
