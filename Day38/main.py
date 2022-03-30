import requests
from datetime import datetime as dt
date = dt.now().strftime("%d/%m/%Y")
time = dt.now().strftime("%H:%M:%S")

training = input("Tell me which excercise you did: ")

sheety_header = {
    "Authorization": "Bearer sekretnytoken"
}

excercise_headers = {
    "x-app-id": "175ce311",
    "x-app-key": "a0b0b1071486f0d0ba03548b67ace302",
    "x-remote-user-id": "0"
}

excercise_parameters = {
    "query": training,
    "gender": "male",
    "weight_kg": 109,
    "height_cm": 188,
    "age": 22,
}

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_respond = requests.post(url=excercise_endpoint, json=excercise_parameters, headers=excercise_headers)
exercise_data = exercise_respond.json()

post_sheety_endpoint = "https://api.sheety.co/a4b9e8bccf3f7f8f27f08f8b1e918461/myWorkouts/workouts"

for exercise in exercise_data["exercises"]:

    post_sheety_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": f"{exercise['duration_min']} min",
            "calories": exercise["nf_calories"],
        }
    }
    post_sheety_respond = requests.post(url=post_sheety_endpoint, json=post_sheety_parameters, headers=sheety_header)


