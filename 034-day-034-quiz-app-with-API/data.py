import requests

API = "https://opentdb.com/api.php?amount=10&type=boolean"

question_data = []
response = requests.get(url=API)
response.raise_for_status()
data = response.json()
question_data = data["results"]

print(question_data)
