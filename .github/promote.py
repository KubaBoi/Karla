import os
import json

settPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "appSettings.json"))

try:

    with open(settPath, "r") as f:
        data = json.loads(f.read())

    v = data["version"]
    v = v.split(".")
    v = v[0] + "." + v[1] + "." + str(int(v[2])+1)

    data["version"] = v

    with open(settPath, "w") as f:
        f.write(json.dumps(data, indent=4, sort_keys=True))

    print("Promoted to version " + v)
except:
    print("Promotion failed")