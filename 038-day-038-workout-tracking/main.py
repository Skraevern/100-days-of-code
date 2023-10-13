import os
import requests
import datetime

APP_ID = os.environ.get("NUTRITIONIXID")
API_KEY = os.environ.get("NUTRITIONIXKEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = (
    "https://api.sheety.co/204aa5b88022ac7dc10f9ac9804eaf62/workoutTracker/workouts"
)
now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
query = {"query": input("Tell me what exercise you did: ")}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=query, headers=headers)
r_data = response.json()

for i in range(0, len(r_data["exercises"])):
    data = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": r_data["exercises"][i]["name"].title(),
            "duration": r_data["exercises"][i]["duration_min"],
            "calories": r_data["exercises"][i]["nf_calories"],
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=data)
    print("response.status_code =", response.status_code)
    print("response.text =", response.text)


# response = requests.get(
#     f"https://api.sheety.co/204aa5b88022ac7dc10f9ac9804eaf62/workoutTracker/workouts"
# )
# data = response.json()
# print(data)
# {'workouts': [{'date': '21/07/2020', 'time': '15:00:00', 'exercise': 'Running', 'duration': 22, 'calories': 130, 'id': 2}]}
