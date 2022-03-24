import requests
from datetime import datetime
import smtplib

my_email = ""
password = ""

MY_LAT = 50.064651
MY_LONG = 19.944981

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

sunrise = int(data['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['sunset'].split("T")[1].split(":")[0])
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()['results']
time_now = datetime.now()
hour_now = time_now.hour


def is_iss_overhead():
    if -5 <= MY_LAT - iss_latitude <= 5 and -5 <= MY_LONG - iss_longitude <= 5:
        return True


def is_night():
    if hour_now >= sunset or hour_now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # making connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="adrian.bozecki@yahoo.com",
                            msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky.")
