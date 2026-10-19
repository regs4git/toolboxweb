# ToolBox — Beta v0.2.0 (Fase 2)

Catálogo responsivo de 109 ferramentas e websites, baseado na taxonomia e catálogo da Fase 1 v0.1.1.

## Testar localmente

Na pasta do projecto:

```bash
python3 -m http.server 8000
```

Abrir http://localhost:8000/ . Não abrir `index.html` por `file://`, porque os módulos JS e o carregamento de JSON exigem HTTP(S).

## Publicar no GitHub Pages

Publicar o conteúdo desta pasta na raiz do repositório e activar **Settings > Pages > Deploy from a branch > main / root**. O projecto usa caminhos relativos e funciona também num repositório de projecto (`/nome-repo/`).

## Funcionalidades

- Início com categorias e selecção Top
- Explorar e pesquisar nome, descrição, keywords e funcionalidades
- Filtros por domínio e funcionalidades, exactos ou aproximados
- Vista grelha, lista e compacta; ordenação
- Favoritos persistentes, exportação e importação
- Tema claro/escuro/sistema
- Links externos seguros, abertos em novo separador
- Fallback offline limitado ao catálogo previamente guardado, quando a página já está disponível no browser

## Ainda não incluído (Fase 3)

Manifest de instalação PWA, Service Worker, offline integral da interface, verificação e notificações de novas versões e testes completos multi-browser.

## Manutenção

O catálogo é `data/tools.json`, a classificação em `data/taxonomy.json`. Consulta `CATALOG_GUIDE.md` antes de editar. Não inserir ferramentas directamente no JavaScript.

## Limitações conhecidas

Os atributos comerciais do catálogo permanecem por verificar. O armazenamento local pode ser eliminado pelo browser; exporta os favoritos para cópia de segurança. A pesquisa não usa IA.
