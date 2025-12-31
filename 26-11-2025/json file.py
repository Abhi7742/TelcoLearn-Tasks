import requests
import json

url="https://marine-api.open-meteo.com/v1/marine?latitude=17.9418&longitude=77.428&hourly=wave_height"

response=requests.get(url)
data=response.json() 
print(json.dumps(data, indent=5))