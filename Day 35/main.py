import os
import requests
from twilio.rest import Client


MY_API_KEY = "f03c0778edecf02a3f6763574c04d29c"
LATITUDE = 11.556374
LONGITUDE = 104.928207

account_sid = "ACe14794c3465457b7b81c43b1e647f9a9"
auth_token = "4735db8492b2e2431195f88a2d99530a"


parameter = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": MY_API_KEY,
    "exclude": "currently,minutely,daily",
}
will_rain = ""

responsese = requests.get(url='https://api.openweathermap.org/data/2.5/onecall?', params = parameter)
responsese.raise_for_status()
data = responsese.json()

weather_data = data['hourly'][:12]
for hour_data in weather_data:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Please bring an Umbrella ☔️.",
        from_='+13347814692',
        to='+85517972058'
    )

    print(message.status)
