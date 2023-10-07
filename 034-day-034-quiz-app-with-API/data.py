import requests
import html

API = "https://opentdb.com/api.php?amount=10&type=boolean"

question_data = []
response = requests.get(url=API)
response.raise_for_status()
data = response.json()
question_data = data["results"]

for i in question_data:
    i["question"] = html.unescape(i["question"])
