import json
import os

plugins_file = "./docs/plugins.json"

#payload = json.loads(os.getenv('EVENT_PAYLOAD'))
s = '{"plugin":{"computedInputs":{"app_class_name":"{{inputs.project_name|title|replace(' ', '')}}"},"description":"Languages environment base plugin","inputs":[{"label":"Application name:","name":"project_name","type":"text"},{"condition":{"operator":"==","value":"kotlin","variable":"language"},"label":"Application group id:","name":"project_group_id","type":"text"},{"label":"Application version:","name":"project_group_id","type":"text"}],"languages":["kotlin"],"name":"languages-env-base-plugin","tags":["environment","kotlin","container"],"type":"env"},"release":"1.0.1","repo":"Orangestack-com/languages-env-base-plugin"}'
payload = json.loads(s)

repo = payload["repo"]
release = payload["release"]
url = f"https://github.com/{repo}"

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
                                        break
                                else: raise Exception(f'plugin with release {release} already indexed')
                        else: 
                                plugins.append(plugin)
                                break


with open(plugins_file, 'wt', encoding='utf-8') as pwf:
        json.dump(plugins, pwf, ensure_ascii=False, indent=4)