import requests

class Post:

    def __init__(self):
        self.endpiont = "https://api.npoint.io/5abcca6f4e39b4955965"

    def request_post(self):
        response = requests.get(url=self.endpiont)
        date = response.json()
        return date


