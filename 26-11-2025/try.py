import requests
response = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={9186fd2ae165bef2d229771090dba518}")
data = response.json()
try :
    response.status_code == 200
    print(data)
except :
    print("wrong api")