import requests

ENDPOINT = "https://tequila.kiwi.com/locations/query"
API_KEY = "_717Yrhb74mvHAbzLFad5uEWomLwPTvL"

class FlightSearch:

    def __init__(self, citi):

        header = {
            "apikey": API_KEY
        }

        request_data = {
            "term": citi,
            "location_types": "city",
        }

        response = requests.get(url=ENDPOINT, headers=header, params=request_data)
        print(response.text)

