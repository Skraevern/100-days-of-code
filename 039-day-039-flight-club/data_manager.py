import requests

ENDPOINT = "https://api.sheety.co/204aa5b88022ac7dc10f9ac9804eaf62/flightDeals/prices"
PUT_ENDPOINT = "https://api.sheety.co/204aa5b88022ac7dc10f9ac9804eaf62/flightDeals/prices"  # [Object ID]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.response = requests.get(ENDPOINT)
        self.data = self.response.json()
        # print("response.status_code =", self.response.status_code)
        # print("response.text =", self.response.text)

    def get_sheet(self):
        return self.data

    def update_iataCode(self, row):
        data = {"price": row}
        response = requests.put(url=f'{ENDPOINT}/{row["id"]}', json=data)
        # print("response.status_code =", response.status_code)
        # print("response.text =", response.text)

    def update_price(self, row, cheapest):
        data = {"price": {"lowestPrice": cheapest}}
        response = requests.put(url=f'{ENDPOINT}/{row["id"]}', json=data)
