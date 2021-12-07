import json
import os

plugins_file = "./docs/plugins.json"

payload = json.loads(os.getenv('EVENT_PAYLOAD'))
repo = payload["repo"]
release = payload["release"]
url = f"https://github.com/{repo}-{release}"

plugin = payload["plugin"]
plugin["releases"] = [ release ]
plugin["url"] = url

with open(plugins_file, 'rt') as prf:
        plugins = json.load(prf)
        if not plugins:
                plugins.append(plugin)
        else:
                for p in plugins:
                        if p["name"] == plugin["name"]:
                                if release not in p["releases"]:
                                        p["releases"].append(release)
                                else: raise Exception(f'plugin with release {release} already indexed')
                        else: plugins.append(plugin)

with open(plugins_file, 'wt', encoding='utf-8') as pwf:
        json.dump(plugins, pwf, ensure_ascii=False, indent=4)