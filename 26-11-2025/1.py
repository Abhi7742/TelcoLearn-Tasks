import json

with open("file.json") as f:
    data = json.load(f)

print(data["name"])
print(data["age"])
print(data["city"])
