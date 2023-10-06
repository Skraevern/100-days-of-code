import requests
import datetime

API = "https://api.sunrise-sunset.org/json"
SILJAN_LAT = 59.276020
SILJAN_LNG = 9.713000

parameters = {"lat": SILJAN_LAT, "lng": SILJAN_LNG}

response = requests.get(url=API, params=parameters)
response.raise_for_status()
data = response.json()

# data = {
#     "results": {
#         "sunrise": "5:35:17 AM",
#         "sunset": "4:43:24 PM",
#         "solar_noon": "11:09:20 AM",
#         "day_length": "11:08:07",
#         "civil_twilight_begin": "4:56:47 AM",
#         "civil_twilight_end": "5:21:53 PM",
#         "nautical_twilight_begin": "4:09:33 AM",
#         "nautical_twilight_end": "6:09:07 PM",
#         "astronomical_twilight_begin": "3:20:40 AM",
#         "astronomical_twilight_end": "6:58:00 PM",
#     },
#     "status": "OK",
# }
print(data["results"]["sunrise"])  # 5:35:17 AM
print(data["results"]["sunset"])  # 4:43:24 PM

# __________________________________________________________________#

parameters = {"lat": SILJAN_LAT, "lng": SILJAN_LNG, "formatted": 0}

response = requests.get(url=API, params=parameters)
response.raise_for_status()
data = response.json()
# data = {
#     "results": {
#         "sunrise": "2023-10-06T05:35:17+00:00",
#         "sunset": "2023-10-06T16:43:24+00:00",
#         "solar_noon": "2023-10-06T11:09:20+00:00",
#         "day_length": 40087,
#         "civil_twilight_begin": "2023-10-06T04:56:47+00:00",
#         "civil_twilight_end": "2023-10-06T17:21:53+00:00",
#         "nautical_twilight_begin": "2023-10-06T04:09:33+00:00",
#         "nautical_twilight_end": "2023-10-06T18:09:07+00:00",
#         "astronomical_twilight_begin": "2023-10-06T03:20:40+00:00",
#         "astronomical_twilight_end": "2023-10-06T18:58:00+00:00",
#     },
#     "status": "OK",
# }

now = datetime.datetime.now()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)  # 2023-10-06T05:35:17+00:00
print(sunset)  # 2023-10-06T16:43:24+00:00
print(now)  # 2023-10-06 20:41:52.017534

print(sunrise.split("T"))  # '2023-10-06', '05:35:17+00:00']
print(sunrise.split("T")[1])  # 05:35:17+00:00
print(sunrise.split("T")[1].split(":"))  # [05, 35, 17+00, 00]
sunrise_hour = sunrise.split("T")[1].split(":")[0]  # 05
sunrise_min = sunrise.split("T")[1].split(":")[1]  # 35
sunrise_formatted = f"{sunrise_hour}:{sunrise_min}"
print(sunrise_formatted)  # 05:35
