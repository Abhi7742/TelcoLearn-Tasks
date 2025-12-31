import requests
import json
url="https://nationalize.io/"
response = requests.get(url)
print("statuscode:",response.status_code)
print(response)