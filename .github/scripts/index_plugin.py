import json
import os

payload = os.getenv('EVENT_PAYLOAD')
plugin = json.loads(payload)
with open('./plugins.json', 'rt') as prf:
        plugins = json.load(prf)
        plugins.extend(plugin)

with open('./plugins.json', 'wt', encoding='utf-8') as pwf:
        json.dump(plugins, pwf, ensure_ascii=False, indent=4)