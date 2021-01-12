import requests
from pprint import pprint

MY_ENDPOINT = "https://api.sheety.co/2d0507519de57998fa6115e50b8fa641/flightDealsProject/prices"


class DataManager:

    def __init__(self):

        response = requests.get(MY_ENDPOINT)

        self.raw_data = response.json()


    def return_data_tomain(self):

        return self.raw_data

