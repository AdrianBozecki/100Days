# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime as dt, timedelta
import twilio

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "KRK"
tomorrow = dt.now() + timedelta(days=1)
six_month_from_today = tomorrow + timedelta(days=180)
print(sheet_data)

# checking if every city has a IATA code
for single_sample in sheet_data:
    if single_sample['iataCode'] == '':
        single_sample['iataCode'] = flight_search.get_destination_code(single_sample['city'])

data_manager.destination_data = sheet_data
#data_manager.update_destination_data()

for destination in sheet_data:
    flight = flight_search.search_for_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city} - {flight.origin_airport}" \
                  f" to {flight.destination_city} - {flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        print(message)
    except AttributeError:
        pass










