import requests

api_key= "e9646cb2e053f510dc1e29ef788d3518"
lat= -6.767500
long= -38.229752

parameters= {
    "lat": lat,
    "lon": long,
    "appid": api_key,
    "exclude": 'current,minutely,daily,arlets'
}

response= requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data= response.json()
for c in range(12):
    id= str(data['hourly'][0]['weather'][0]['id'])
    print(id[0])
