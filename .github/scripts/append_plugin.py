import json

with open('./plugin.json') as pf:
    plugin = json.load(pf)
    with open('./plugins.json', 'rt') as prf:
        plugins = json.load(prf)
        plugins.append(plugin)

with open('./plugins.json', 'wt', encoding='utf-8') as pwf:
        json.dump(plugins, pwf, ensure_ascii=False, indent=4)