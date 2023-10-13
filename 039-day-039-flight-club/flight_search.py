import requests
import datetime

ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
FLIGHT_FROM = "LON"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self) -> None:
        self.header = {
            "apikey": "4c8ukmUGNlHslIJ95QbGLEogTYx5FRtB",
        }

    def search_iataCode(self, city):
        parameters = {"term": city}
        response = requests.get(url=ENDPOINT, params=parameters, headers=self.header)
        # print("response.status_code =", response.status_code)
        # print("response.text =", response.text)
        data = response.json()
        return data["locations"][0]["code"]

    def search_flights(self, iataCode):
        now = datetime.datetime.now()
        fl_from_date = (now + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        fl_to_date = (now + datetime.timedelta(days=1)).strftime("%d/%m/%Y")

        parameters = {
            "fly_from": FLIGHT_FROM,
            "fly_to": iataCode,
            "date_from": fl_from_date,
            "date_to": fl_to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "limit": 100,
        }
        response = requests.get(
            url=FLIGHT_SEARCH_ENDPOINT, params=parameters, headers=self.header
        )
        # print("response.status_code =", response.status_code)
        # print("response.text =", response.text)
        data = response.json()
        return data["data"][0]["price"]
