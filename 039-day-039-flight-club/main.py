# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_sheet()

flight_search = FlightSearch()

flight_data = FlightData()

for row in sheet_data["prices"]:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.search_iataCode(row["city"])
        data_manager.update_iataCode(row)

    cheapest = flight_search.search_flights(row["iataCode"])
    data_manager.update_price(row, cheapest)
