import requests

API = (
    "https://api.met.no/weatherapi/locationforecast/2.0/compact"  # ?lat=60.10&lon=9.58
)
SILJAN_LAT = 59.276020
SILJAN_LNG = 9.713000
UTC_CORRECTION = 3

headers = {
    "User-Agent": "My User Agent 1.0",
    "From": "youremail@domain.example",  # This is another valid field
}


parameters = {
    "lat": SILJAN_LAT,
    "lon": SILJAN_LNG,
}

response = requests.get(url=API, params=parameters, headers=headers)
response.raise_for_status()
data = response.json()


def format_time(data):
    for i in range(0, len(data["properties"]["timeseries"])):
        time = data["properties"]["timeseries"][i]["time"]
        date = time.split("T")[0]
        hour = int(time.split("T")[1].split(":")[0]) + UTC_CORRECTION
        if hour < 10:
            hour = f"0{hour}"
        minute = time.split("T")[1].split(":")[1]
        data["properties"]["timeseries"][i]["time"] = f"{date} {hour}:{minute}"
    return data


print(data["properties"]["timeseries"][0]["time"])
print(data)
data = format_time(data)


rain_list = []
for i in range(0, len(data["properties"]["timeseries"])):
    # print(
    #     data["properties"]["timeseries"][i]["time"],
    #     data["properties"]["timeseries"][i]["data"]["instant"]["details"][
    #         "air_temperature"
    #     ],
    # )
    # 2023-10-09 15:00 9.0
    try:
        rain_list.append(
            data["properties"]["timeseries"][i]["data"]["next_6_hours"]["details"][
                "precipitation_amount"
            ]
        )
    except KeyError:
        rain_list.append(0)


for i in range(0, len(data["properties"]["timeseries"])):
    if rain_list[i] > 0:
        print(f'{rain_list[i]}mm rain at:{data["properties"]["timeseries"][i]["time"]}')
        # 0.6mm rain at:2023-10-10 09:00
        # 0.8mm rain at:2023-10-10 10:00
        # 1.0mm rain at:2023-10-10 11:00
        # 1.2mm rain at:2023-10-10 12:00
        # 1.2mm rain at:2023-10-10 13:00
        # 1.2mm rain at:2023-10-10 14:00
        # 3.1mm rain at:2023-10-13 14:00
        # 3.1mm rain at:2023-10-13 20:00

# --- Rain next hour --- #
rain_data = {}
first_hour = data["properties"]["timeseries"][0]
six_hour = data["properties"]["timeseries"][5]

rain_data["time"] = first_hour["time"].split(" ")[1]
rain_data["1h"] = first_hour["data"]["next_1_hours"]["details"]["precipitation_amount"]
rain_data["6h"] = first_hour["data"]["next_6_hours"]["details"]["precipitation_amount"]
rain_data["12h"] = six_hour["data"]["next_6_hours"]["details"]["precipitation_amount"]

if rain_data["1h"] > 0:
    print(f'{rain_data["1h"]}mm rain expected the next hour from {rain_data["time"]}')
if rain_data["6h"] > 0:
    print(
        f'{rain_data["6h"]}mm rain expected for the next 6 hours from {rain_data["time"]}'
    )
if rain_data["12h"] > 0:
    print(
        f'Rain {rain_data["12h"]}mm rain expected for the next 12 hours from {rain_data["time"]}'
    )
if (rain_data["1h"] == 0) and (rain_data["6h"] == 0) and (rain_data["12h"] == 0):
    print(f'No rain expected the next 12 hours from {rain_data["time"]}')
