import datetime as dt
import random
import smtplib
import pandas

now = dt.datetime.now()
THIS_MONTH =now.month
TODAY = now.day
SENDER = 'einoyakoreal@gmail.com'
PASSWORD = 'Ainghongsin'
PERSONAL_BIRTH = (THIS_MONTH, TODAY)

csv_data = pandas.read_csv('birthdays.csv')


Birthday_dist = {(data_row['month'], data_row['day']): data_row for (index, data_row) in csv_data.iterrows()}

if (THIS_MONTH, TODAY) in Birthday_dist:
    birth = Birthday_dist[PERSONAL_BIRTH]
    NAME = (birth['name'])

    SEND_TO_EMAIL = birth['email']


    path_file = (f"./letter_templates/letter_{random.randint(1,3)}.txt")
    with open(path_file) as file:
        data = file.read()
    MESSAGE = data.replace("[NAME]", NAME)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(SENDER, PASSWORD)

        connection.sendmail(from_addr=SENDER, to_addrs=SEND_TO_EMAIL, msg = (f"Subject:Happy Birthday\n\n{MESSAGE}"))

