## This project host in https://repl.it
## Run this project
## DATA HAS BEEN STORED IN LINK: https://docs.google.com/spreadsheets/d/1eXarLyPOCmXbpzjy49ggKimYEH3BAaIW8ZI0mOsAGf0/edit#gid=0

import os
import requests
import datetime

today = datetime.datetime.now()
TODAY = today.strftime('%d/%m/%Y')
TIME_NOW = today.strftime("%X")


EMAIL = os.environ.get("MY_EMAIL")
PROFECT_NAME = "My Workouts"
USER_NAME = "AING HONGSIN"

ENDPOINT = os.environ.get("MYNUTRITIONIX_ENDPOINT")
print(ENDPOINT)

APP_ID = os.environ.get("MY_APP_ID")
API_KEY = os.environ.get("MY_API_KEY")

GENDER = os.environ.get("MY_GENDER")
WEIGHT_KG = "60"
HEIGHT_CM = "170"
AGE = "18"


HEARDER = {
    "x-app-id":  APP_ID,
    "x-app-key": API_KEY,
}

## i ran 3 miles and walked for 2 miles

userInput = input("Tell me which exercise you did: ")

POST_DATA = {
    "query": userInput,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=ENDPOINT, json=POST_DATA, headers = HEARDER)
data = response.json()
# print(response.text)

SHEET_HEARDER = {
    "Authorization": "Bearer 1a2i3n4g5h6o7n8g9s0i1n"
}

for exercise in data["exercises"]:
    PARAMETER = {
        "workout": {
            "date": TODAY,
            "time": TIME_NOW,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # SHEELY_ENDPOINT = f"https://api.sheety.co/{USER_NAME}/{PROFECT_NAME}/workouts"
    SHEELY_ENDPOINT = os.environ.get("MY_SHEELY_ENDPOINT")


    response = requests.post(url=SHEELY_ENDPOINT, json=PARAMETER, headers = SHEET_HEARDER)

    print(response.text)
    print(PARAMETER)

    print(response.raise_for_status())
