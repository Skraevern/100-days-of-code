import requests
import os

# Create user at:
# https://pixe.la

TOKEN = os.environ.get("PIXELA_TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"  # API

user_params = {
    "token": TOKEN,
    "username": "skraevern",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@skraevern , it is your profile page!","isSuccess":true}
