# merge JSON data from two different weather APIs
import requests
import json

url_1="https://api.open-meteo.com/v1/forecast?latitude=12.9719&longitude=77.5937&hourly=temperature_2m,weather_code"

url_2="https://api.open-meteo.com/v1/forecast?latitude=20.2724&longitude=85.8338&hourly=temperature_2m,weather_code"

response_1 = requests.get(url_1)
data_1 = response_1.json()
response_2 = requests.get(url_2)
data_2 = response_2.json()


with open('merged_weather.json', 'w') as f:
    json.dump(data_1, f, indent=4)
    json.dump(data_2,f,indent=4)