import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_PRICE = ""
API_KEY_NEWS = ""
account_sid = ""
auth_token = ""
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_PRICE,
}

url = 'https://www.alphavantage.co/query'
r = requests.get(url, params=parameters)
data = r.json()

closing_prices = {k[-2:]: v['4. close'] for (k, v) in data['Time Series (Daily)'].items()}

closing_list = list(closing_prices.values())


def price_change():
    return abs(1 - float(closing_list[0]) / float(closing_list[1])) * 100

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

new_parameters = {
    "apiKey": "",
    "q": COMPANY_NAME,
}

url = 'https://newsapi.org/v2/everything'
r = requests.get(url, params=new_parameters)
data = r.json()

articles = [items for items in data['articles'][:3]]
message = [f"Headline: {x['title']}:\nBrief: {x['description']}" for x in articles]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

def send_sms(text):
    proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=text,
        from_='+17408833348',
        to=''
    )
    print(message.status)


if price_change() > 0.05:
    for single_message in message:
        formated_message = f"\n{STOCK}: {round(price_change())}%\n{single_message}"
        send_sms(formated_message)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
