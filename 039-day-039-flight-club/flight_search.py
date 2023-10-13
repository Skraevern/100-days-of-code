import requests

ENDPOINT = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self) -> None:
        pass

    def search(self, city):
        header = {
            "apikey": "4c8ukmUGNlHslIJ95QbGLEogTYx5FRtB",
        }
        parameters = {"term": city}
        response = requests.get(url=ENDPOINT, params=parameters, headers=header)
        print("response.status_code =", response.status_code)
        print("response.text =", response.text)
        data = response.json()
        return data["locations"][0]["code"]
