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
print(response.text)
