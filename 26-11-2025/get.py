import requests
import json
dummy_data = {
    "name":"abhi",
    "age":24,
}
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(url,dummy_data)
data = response.json()
# print(data)
print(json.dumps(data, indent=4)) 
print("status",response.status_code)