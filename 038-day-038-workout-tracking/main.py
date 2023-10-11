import os
import requests

APP_ID = os.environ.get("NUTRITIONIXID")
API_KEY = os.environ.get("NUTRITIONIXKEY")
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

print(APP_ID, API_KEY)

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
query = {"query": input("Tell me what exercise you did: ")}

response = requests.post(url=ENDPOINT, json=query, headers=headers)
data = response.json()
workouts = {}

for i in range(0, len(data["exercises"])):
    workouts = {
        "date": "21/08/2020",
        "time": "14:00",
        "exercise": data["exercises"][i]["name"],
        "duration": data["exercises"][i]["duration_min"],
        "calories": data["exercises"][i]["nf_calories"],
    }
    post = requests.post(
        url=f"https://api.sheety.co/{API_KEY}/workoutTracker/workouts", json=workouts
    )


# response = requests.get(f"https://api.sheety.co/{API_KEY}/workoutTracker/workouts")
# data = response.json()
# print(data)
# {'workouts': [{'date': '21/07/2020', 'time': '15:00:00', 'exercise': 'Running', 'duration': 22, 'calories': 130, 'id': 2}]}

# {"exercises":[{"tag_id":317,"user_input":"ran","duration_min":124.3,"met":9.8,"nf_calories":1421.16,"photo":{"highres":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg","thumb":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg","is_user_uploaded":false},"compendium_code":12050,"name":"running","description":null,"benefits":null},{"tag_id":774,"user_input":"workout","duration_min":30,"met":4,"nf_calories":140,"photo":{"highres":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/774_highres.jpg","thumb":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/774_thumb.jpg","is_user_uploaded":false},"compendium_code":2143,"name":"General Workout","description":null,"benefits":null}]}
