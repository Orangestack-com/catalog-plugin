import json
import os

PLUGINS_FILE = "./docs/plugins.json"
payload = json.loads(os.getenv('EVENT_PAYLOAD'))

repo = payload["repo"]
release = payload["release"]
url = f"https://github.com/{repo}"

plugin = payload["plugin"]
plugin["url"] = url

exists = False
with open(PLUGINS_FILE, 'rt') as prf:
        plugins = json.load(prf)
        if not plugins:
                plugins.append(plugin)
        else:
                for p in plugins:
                        if p["name"] == plugin["name"]:
                                if release not in p["releases"]:
                                        plugin["releases"] = p["releases"]
                                        plugin["releases"].append(release)
                                        plugins.remove(p)
                                        plugins.append(plugin)
                                        exists = True
                                        break
                                else: raise Exception(f'plugin with release {release} already indexed')
        if not exists:
                plugins.append(plugin)

with open(PLUGINS_FILE, 'wt', encoding='utf-8') as pwf:
        json.dump(plugins, pwf, ensure_ascii=False, indent=4)