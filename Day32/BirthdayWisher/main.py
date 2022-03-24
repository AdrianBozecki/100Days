import pandas
import datetime as dt
import smtplib
from random import randint

now = dt.datetime.now()
month = now.month
day = now.day
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict()

for key, value in birthdays_dict['day'].items():
    index = list(birthdays_dict['day'].keys()).index(key)
    if value == day and birthdays_dict['month'][index] == month:
        name = birthdays_dict['name'][index]
        email = birthdays_dict['email'][index]

        random_letter = randint(1, 3)
        with open(f"letter_templates/letter_{random_letter}.txt") as file:
            template = file.read()
            addressed_template = template.replace(f"[NAME]", name)
            print(addressed_template)

        my_email = ""
        password = ""
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # making connection secure
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject:Happy Birthday\n\n{addressed_template}")








