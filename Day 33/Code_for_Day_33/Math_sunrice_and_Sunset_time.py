import requests
import datetime as dt
import smtplib
import time

MY_LAT = 11.556374
MY_LOG = 104.928207
time_now = dt.datetime.now().hour

MY_EMAIL = 'einoyakoreal@gmail.com'
MY_PASSWORD = 'Ainghongsin'

def is_iss_overhacd():

    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()

    iss_longtitude = int(data['iss_position']['longitude'])
    iss_latitude = int(data['iss_position']['latitude'])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LOG - 5 <= iss_longtitude <= MY_LOG + 5 :
        return True


def is_night():

    parameter = {
        "lat": MY_LAT,
        "lng": MY_LOG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()

    data = response.json()

    sunrise_GMT = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset_GMT = int(data['results']['sunset'].split("T")[1].split(":")[0])

    sunrise = (sunrise_GMT + 7) % 24
    sunset = (sunset_GMT + 7) % 24

    if time_now <= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhacd and is_night:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr= MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                smg = f"Subject:Look Up\n\n The ISS is above you in the sky.")



