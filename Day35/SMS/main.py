import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACd8fac052d9624e3b7249cb123212ac2e"
auth_token = os.environ.get("AUTH_TOKEN")

lat = 50.064651
long = 19.944981

parameters = {
    "lat": lat,
    "lon": long,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

prediction = [data["hourly"][x]["weather"][0]["id"] for x in range(12)]


def will_rain():
    for x in prediction:
        if x < 700:
            return True


if will_rain():
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="Bring an umbrella",
        from_='+17408833348',
        to=''
    )
    print(message.status)
