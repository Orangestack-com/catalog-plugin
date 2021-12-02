import json
import os

plugins_file = "./docs/plugins.json"
payload = json.loads(os.getenv('EVENT_PAYLOAD'))
tag = payload["tag"]
plugin = payload["plugin"]
plugin["tags"] = [ tag ]

with open(plugins_file, 'rt') as prf:
        plugins = json.load(prf)
        if not plugins:
                plugins.append(plugin)
        else:
                for p in plugins:
                        if p["name"] == plugin["name"]:
                                if tag not in p["tags"]:
                                        p["tags"].append(tag)
                                else: raise Exception(f'plugin with tag {tag} already indexed')
                        else: plugins.append(plugin)

with open(plugins_file, 'wt', encoding='utf-8') as pwf:
        json.dump(plugins, pwf, ensure_ascii=False, indent=4)