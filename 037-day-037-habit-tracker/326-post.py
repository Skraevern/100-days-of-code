# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
import requests
import os
import datetime

# https://pixe.la

USERNAME = "skraevern"
TOKEN = os.environ.get("PIXELA_TOKEN")
ENDPOINT = "https://pixe.la/v1/users"  # API

headers = {"X-USER-TOKEN": TOKEN}

today = datetime.datetime.now()
# https://www.w3schools.com/python/gloss_python_date_format_codes.asp
print(today)
print(today.strftime("%Y%m%d"))

element = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

graph_endpoint = f"{ENDPOINT}/{USERNAME}/graphs/graph1"

response = requests.post(url=graph_endpoint, json=element, headers=headers)
print(response.text)
# {"message":"Success.","isSuccess":true}
# https://pixe.la/v1/users/skraevern/graphs/graph1.html
