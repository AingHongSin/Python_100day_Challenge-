import smtplib
import datetime as dt
import random

sender_email = 'ainghongsin9999@gmail.com'
sending_to = 'ainghongsin@yahoo.com'

with open('quotes.txt', mode = 'r') as file:
    data = file.readlines()
    qoutes_list = [quote for quote in data]

qoute_for_today = random.choice(qoutes_list)
qoute_for_today.encode("utf-8")

today = dt.datetime.now()

if today.weekday() == 0:
    print(f"Mail sent ot {sending_to}\nSubject: Quote For Today\n{qoute_for_today}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(sender_email, '#############')
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=sending_to,
            msg=f"Subject:Monday Motivation\n\n{qoute_for_today}")