import requests
import os

# https://pixe.la

USERNAME = "skraevern"
TOKEN = os.environ.get("PIXELA_TOKEN")
ENDPOINT = "https://pixe.la/v1/users"  # API

headers = {"X-USER-TOKEN": TOKEN}

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

graph_endpoint = f"{ENDPOINT}/{USERNAME}/graphs"

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
# {"message":"Success.","isSuccess":true}
# https://pixe.la/v1/users/skraevern/graphs/graph1.html
