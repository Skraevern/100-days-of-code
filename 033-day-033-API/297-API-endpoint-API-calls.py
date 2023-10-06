import requests

API = "http://open-notify.org/Open-Notify-API/ISS-Location-Now/"

response = requests.get(url=API)
print(response)  # <Response [200]>
print(response.status_code)  # 200
response.raise_for_status()

fault_response = requests.get(url="http://api.open-notify.org/issssssssssss-now.json")
print(response)  # <Response [404]>
print(response.status_code)  # 404
# fault_response.raise_for_status()  # requests.exceptions.HTTPError: 404 Client Error: Not Found for url:......

data = response.json()
print(data)
# {'iss_position': {'longitude': '-131.9207', 'latitude': '14.9151'}, 'timestamp': 1696613996, 'message': 'success'}

print(data["iss_position"])
# {'longitude': '-129.8320', 'latitude': '17.5348'}

print(data)
print(data["iss_position"]["longitude"])
# -127.0720

iss_position = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])
print(iss_position)
# ('-121.3263', '27.0343')
