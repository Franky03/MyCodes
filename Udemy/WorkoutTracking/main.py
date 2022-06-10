import requests
from datetime import datetime

API_ID= "9ba8b3b0"
API_KEY= "0b7c9aef79a8e79bd661788782670ca7"

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

sheet_endpoint= "https://api.sheety.co/6e3b81f17f597c3092672a4632fc3fb7/workoutTracking/workouts"

today= datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

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

    sheet_response= requests.post(sheet_endpoint, json=sheet_params)
    print(sheet_response.text)


