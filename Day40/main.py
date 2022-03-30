from data_manager import DataManager
from datetime import date,timedelta, datetime as dt
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
origin_city_search = FlightSearch()
end = False
while not end:
    sheet_data = data_manager.get_destination_data()
    menu = input("\nWhat do you want to do?\n"
                 "1. Show possible destination,\n"
                 "2. Add destinations,\n"
                 "3. Search for cheapest flights,\n"
                 "4. Exit\n")

    if menu == "1":
        destinations = [x[0] for x in sheet_data]
        print(destinations)
    elif menu == "2":
        new_destination = input("Add new city: ")
        data_manager.update_destination_data(new_destination, flight_search)
        print("New city succesfully added to database")
    elif menu == "3":
        origin_city = input("Which city you want to fly from?")
        origin_city_iata = origin_city_search.get_destination_code(origin_city)
        from_time = int(input("In how many days from today do you want to departure? "))
        to_time = int(input("In how many days from today do you want to arrive home? "))
        departure = dt.now() + timedelta(days=from_time)
        arrival = departure + timedelta(days=to_time)
        least_night_distance = int(input("What's the least amount of days you want to stay? "))
        most_night_distance = int(input("What's the most amount of days you want to stay? "))

        for destination in sheet_data:
            try:
                flight = flight_search.search_for_flights(
                    origin_city_iata,
                    destination[1],
                    from_time=departure,
                    to_time=arrival,
                    nht_in_dst_from=least_night_distance,
                    nht_in_dst_to=most_night_distance,
                )
            except KeyError:
                continue
            try:
                notification_manager.send_message(flight)
            except AttributeError:
                pass
    elif menu == "4":
        end = True
    else:
        print("Type 1 - 4")










