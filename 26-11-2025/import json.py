import requests
import json

url="https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print("response:",response)
with open("response.json","w") as f:
    json.dump(response.json(),f,indent=4)
print("status",response.json())
