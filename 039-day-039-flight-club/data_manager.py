import requests

ENDPOINT = "https://api.sheety.co/204aa5b88022ac7dc10f9ac9804eaf62/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.response = requests.get(ENDPOINT)
        self.data = self.response.json()

    def get_sheet(self):
        return self.data
