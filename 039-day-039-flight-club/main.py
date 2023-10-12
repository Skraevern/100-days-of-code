# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_sheet()

flight_search = FlightSearch()

for column in sheet_data["prices"]:
    if column["iataCode"] == "":
        flight_search.search(column["city"])
