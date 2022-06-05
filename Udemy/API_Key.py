from twilio.rest import Client
import requests

#TO WORK CORRECTLY, YOU NEED TO PUT YOUR VERIFIED NUMBER ON THE TWILIO WEBSITE AND THE GENERATED NUMBER, IN ADDITION TO THE API SETTINGS.

account_sid = "AC21f571e231bc3849cb530842fc056bcd"
auth_token = "5270f6a43221507c720d77ab96ceb125"

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
will_rain= False

for c in range(12):
    id= data['hourly'][c]['weather'][0]['id']
    if int(id)<700:
        will_rain= True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="Hoje o toró cai ☔. Lembrar de abrir o portão pra Toph 🐶.",
                        from_='+12058807119',
                        to='YOUR_NUMBER'
                    )

    print(message.status)