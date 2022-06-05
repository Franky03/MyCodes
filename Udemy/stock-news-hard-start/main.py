from twilio.rest import Client
from datetime import datetime
import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = "AC21f571e231bc3849cb530842fc056bcd"
auth_token = "7fd074874e6197972209dea4fdf487a5"

api_key= "e9646cb2e053f510dc1e29ef788d3518"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY= "HTZTMD670VM9LONO"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY= "7a9e6b0a82224a00a96c14ec027a6678"


parameters={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_KEY,
}

response= requests.get("https://www.alphavantage.co/query", params=parameters)
data= response.json()['Time Series (Daily)']

data_list= [values for (key, values) in data.items()]
yesterday= float(data_list[0]['4. close'])
bf_yesterday= float(data_list[1]['4. close'])

diference= yesterday-bf_yesterday

percent= 100- round(100*yesterday/bf_yesterday)
if percent>0:
    result= (f"TSLA: 🔺{percent}%")

else:
    result= (f"TSLA: 🔻{str(percent)[1::]}%")

news_parameters={
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_KEY,
    }
news_response= requests.get("https://newsapi.org/v2/everything", params= news_parameters)
new_data= news_response.json()['articles'][:3]


formatted= [f"Title: {article['title']}\nDescription: {article['description']}" for article in new_data]

client = Client(account_sid, auth_token)
message = client.messages \
                    .create(
                        body= f"{result}",
                        from_='+12058807119',
                        to='+5583991157521'
                    )

print(message.status)

for c in formatted:
    message = client.messages \
                        .create(
                            body= f"{c}",
                            from_='+12058807119',
                            to='+5583991157521'
                        )

    print(message.status)

