import os
import requests
from datetime import datetime

API_ID= os.environ['API_ID']
API_KEY= os.environ['API_KEY']
TOKEN= os.environ['TOKEN']

exercise= input("The exercises you did: ")

headers= {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

parameters= {
 "query": exercise,
 "gender":"male",
 "weight_kg":64.00,
 "height_cm":166.00,
 "age":17
}

response= requests.post(" https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)

data= response.json()

sheet_endpoint= os.environ['SHEET_ENDPOINT']

today= datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_headers= {
    "Authorization": TOKEN
}

for exercise in data['exercises']:
    sheet_params= {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response= requests.post(sheet_endpoint, json=sheet_params, headers= sheet_headers)
    print(sheet_response.text)


