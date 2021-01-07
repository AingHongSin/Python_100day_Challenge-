import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


MY_API_KEY = os.environ.get("API_KEY")
LATITUDE = 11.556374
LONGITUDE = 104.928207

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUATH_TOKEN")
TO_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")


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

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

client = Client(account_sid, auth_token, http_client=proxy_client)

if will_rain:

    message = client.messages \
        .create(
        body="It's going to rain today. Please bring an Umbrella ☔️.",
        from_='+13347814692',
        to=TO_PHONE_NUMBER
    )
    print(message.status)

else:

    message = client.messages \
        .create(
        body="The weather today is clearly ☀️⛅️️.",
        from_='+13347814692',
        to=TO_PHONE_NUMBER
    )
    print(message.status)

