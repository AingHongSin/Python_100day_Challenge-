import requests

class API():

    def __init__(self, name):
        self.genderAPI_endpoint = f"https://api.genderize.io?name={name}"
        self.ageAPI_endpoint = f"https://api.agify.io?name={name}"

    def gender_request(self):
        response = requests.get(url=self.genderAPI_endpoint)
        data = response.json()
        return data["gender"]

    def age_request(self):
        response = requests.get(url=self.ageAPI_endpoint)
        data = response.json()
        return data["age"]
