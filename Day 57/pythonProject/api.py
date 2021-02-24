import requests

def gender_request(name):
    genderAPI_endpoint = f"https://api.genderize.io?name={name}"
    response = requests.get(url=genderAPI_endpoint)
    data = response.json()
    return data["gender"]

def age_request(name):
    ageAPI_endpoint = f"https://api.agify.io?name={name}"
    response = requests.get(url=ageAPI_endpoint)
    data = response.json()
    return data["age"]

def blog_request():
    response = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965")
    data = response.json()
    return data

