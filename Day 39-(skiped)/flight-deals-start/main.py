from data_manager import DataManager
from flight_search import FlightSearch


dataManager = DataManager()


sheetdata = dataManager.return_data_tomain()

# print(sheetdata)

citiList = [city['city'] for city in sheetdata['prices']]

for city in citiList:
    flightSearch = FlightSearch(city)
    print(flightSearch)