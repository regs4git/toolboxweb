# ToolBox — Guia de manutenção do catálogo (Fase 1)

## Objectivo
A PWA lê `data/tools.json`, `data/taxonomy.json` e `data/version.json`; adicionar ferramentas não deve exigir alterações ao HTML/CSS/JS. O catálogo é público e de leitura na aplicação. Favoritos e preferências pertencem ao utilizador e ficam separados.

## Instruções para uma IA actualizar o catálogo
1. Ler os três JSON actuais antes de editar. Nunca substituir o catálogo apenas pela nova lista.
2. Para cada URL, confirmar identidade e URL canónico, evitar duplicados por ID, domínio e redireccionamentos.
3. Produzir uma descrição curta, factual e neutra em português europeu.
4. Atribuir `primary_domain`, `domains` e `features` apenas com IDs definidos na taxonomia. Uma ferramenta pode ter várias funções.
5. Para funcionalidades ainda inexistentes, propor extensão da taxonomia e só depois utilizar os novos IDs. Não inventar etiquetas incompatíveis.
6. Não inferir preços, licenças, suporte offline, alojamento próprio nem necessidade de conta: manter `unknown` até verificação em fonte oficial.
7. Usar `verification.status=pending` enquanto não houver verificação; quando confirmada, registar `checked_at` e, numa futura revisão do esquema, referências às fontes.
8. `top` é editorial, nunca favorito pessoal. Não alterar valores Top sem decisão editorial.
9. Preservar IDs estáveis; se um site mudar de domínio, actualizar o URL e manter o ID.
10. Actualizar `catalog_version`, contagens e resumo em `version.json` em conjunto com `tools.json`. Validar os ficheiros antes de publicar.

## Semântica dos filtros
- As funcionalidades são identificadores estáveis; os rótulos podem ser alterados sem modificar os registos.
- Dentro do mesmo grupo, pode existir seleção múltipla; a UI deverá permitir lógica `todas`/`qualquer` conforme modo.
- `unknown` significa por verificar, não significa `no`.
- Ocultar por defeito categorias vazias, mantendo-as no esquema para crescimento futuro.
- A pesquisa por tarefas em linguagem natural fica fora da v1.0.

## Âmbito e qualidade
- `source_group=original`: URL da lista inicial. `source_group=curated`: alternativa adicionada na curadoria.
- Os links representam websites ou páginas oficiais de projectos; não significa que todos sejam serviços exclusivamente web.
- A presença no catálogo não equivale a recomendação ou validação comercial.
- Não recolher nem armazenar dados pessoais de utilizadores no catálogo público.

## Publicação futura
Na integração PWA, usar os três JSON como um conjunto consistente: descarregar, validar e activar em conjunto; conservar a última versão válida offline. Não eliminar favoritos em actualizações.

## Grupos de filtros (v0.1.1)
Cada domínio define `groups` com `feature_ids`. O motor de filtros deve gerar a interface a partir destes dados, sem grupos codificados em JavaScript. Categorias vazias ficam ocultas por defeito. A IA deve preservar IDs de grupos e funcionalidades e executar `python3 validate.py` após cada alteração.
