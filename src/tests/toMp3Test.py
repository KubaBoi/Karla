import os
import json
import requests


r = requests.post("http://localhost:8004/recognition/toMp3", data=json.dumps({"TEXT": "hello"}))
print(r.content)
with open(os.path.join(__file__, "..", "answer.mp3"), "wb") as f:
    f.write(r.content)