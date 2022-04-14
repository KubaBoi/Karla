import os
import requests

with open(os.path.join(__file__, "..", "recording2.wav"), "rb") as f:
    data = f.read()

r = requests.post("http://localhost:8004/recognition/fromWav", data=data)
print(r.text)