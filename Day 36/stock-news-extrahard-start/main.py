import os
import requests
import datetime as dt
import random
from twilio.rest import Client

TODAY = dt.datetime.now()

YESTERDAY = TODAY - dt.timedelta(days=1)
YESTERDAY.strftime('%Y-%m-%d')

A_DAY_BEFOR_YESTERDAY = TODAY - dt.timedelta(days=2)
A_DAY_BEFOR_YESTERDAY.strftime('%Y-%m-%d')

TWO_DAY_BEFOR_YESTERDAY = TODAY - dt.timedelta(days=3)
TWO_DAY_BEFOR_YESTERDAY.strftime('%Y-%m-%d')


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MESSAGE_FOR_SEND = ''

STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
account_sid = "YOUR TWILIO ACCOUNT SID"
auth_token = "YOUR TWILIO AUTH TOKEN"


information = {}

reslut_list = []
information['title'] = []
information['description'] = []



print(reslut_list)
print(information)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    
    percentage = round(((reslut_list[1] - reslut_list[0]) * 100) / reslut_list[1], 2)

print(f"PERCENTAGE: {percentage}")
if -1 > percentage or percentage > 1 :

    parameter = {
        'q': STOCK,
        'sortBY': 'popularity',
        'apiKey': NEWS_API_KEY
    }
    respones = requests.get(url='http://newsapi.org/v2/everything', params = parameter)
    respones.raise_for_status()
    data = respones.json()

    reslut_list.append(data['totalResults'])
    print(data['totalResults'])
    for row in range(0,3):
        information['title'].append(data['articles'][row]['title'])
        information['description'].append(data['articles'][row]['description'])

    
    for row in range(3):
        if -5 > percentage:
            MESSAGE_FOR_SEND = f"""
                {STOCK}: 🔻%{percentage}
                TITLE: {information['title'][row]} ({STOCK})\n 
                BRIEF: {information['description'][row]}"""
        elif percentage > 5:
            MESSAGE_FOR_SEND = f"""
                {STOCK}: 🔺%{percentage}
                TITLE: {information['title'][row]} ({STOCK})\n
                BRIEF: {information['description'][row]}"""


        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number.


        client = Client(account_sid, auth_token)
        
        message = client.messages \
                        .create(
                             body=MESSAGE_FOR_SEND,
                             from_=VIRTUAL_TWILIO_NUMBER,
                             to=VERIFIED_NUMBER
                         )




#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


