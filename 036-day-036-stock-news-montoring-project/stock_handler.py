import requests
import os
import datetime
from datetime import timedelta

API = f"https://www.alphavantage.co/query"  # ?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=60min&apikey={os.environ.get("ALPHAVANTAGE_KEY")}'
PARAMETERS = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "TSLA",
    "interval": "60min",
    "apikey": os.environ.get("ALPHAVANTAGE_KEY"),
}
print(PARAMETERS)


class StockHandler:
    def __init__(self) -> None:
        self.response = requests.get(url=API, params=PARAMETERS)
        self.response.raise_for_status()
        self.data = self.response.json()

    def get_price(self, day_index):
        today = datetime.date.today()
        price = None
        index = day_index
        while price == None:
            try:
                index += 1
                price = self.data["Time Series (60min)"][
                    f"{today - timedelta(days=index)} 19:00:00"
                ]["4. close"]
            except KeyError:
                continue
            else:
                break
        return float(price)

    def get_diff_percentage(self, num_1, num_2):
        diff = num_1 - num_2
        percentage = (diff / num_1) * 100
        return percentage


test = StockHandler()
print(test.price1, test.price2)
