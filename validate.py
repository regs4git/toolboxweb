import json, pathlib, collections, urllib.parse
p=pathlib.Path(__file__).parent/'data'
t=json.loads((p/'taxonomy.json').read_text()); c=json.loads((p/'tools.json').read_text()); v=json.loads((p/'version.json').read_text())
items=c['tools']; ids=[x['id'] for x in items]; urls=[x['url'].rstrip('/').lower() for x in items]
domains={x['id'] for x in t['domains']}; features={x['id'] for x in t['features']}
assert len(ids)==len(set(ids)), 'IDs duplicados'
assert len(urls)==len(set(urls)), 'URLs duplicados'
assert len(features)==len(t['features']) and len(domains)==len(t['domains']), 'IDs da taxonomia duplicados'
assert len(items)==v['tools_count'], 'Contagem incorrecta'
assert c['catalog_version']==v['catalog_version'], 'Versões incompatíveis'
for d in t['domains']:
 assert set(d['feature_ids'])<=features, d['id']
 assert len({g['id'] for g in d['groups']})==len(d['groups']), d['id']
 for g in d['groups']: assert set(g['feature_ids'])<=features, g['id']
for x in items:
 assert urllib.parse.urlparse(x['url']).scheme=='https' and urllib.parse.urlparse(x['url']).netloc, x['id']
 assert x['primary_domain'] in domains and x['primary_domain'] in x['domains'] and set(x['domains'])<=domains, x['id']
 assert set(x['features'])<=features and len(x['features'])==len(set(x['features'])), x['id']
 assert x['verification']['status'] in ('pending','verified','stale'), x['id']
 for f in ('pricing','license','offline','self_hosted','account_required'):
  assert x[f] in t['global_filters'][f], (x['id'],f)
print(f"OK: {len(ids)} ferramentas; {len(domains)} domínios; {len(features)} funcionalidades")
