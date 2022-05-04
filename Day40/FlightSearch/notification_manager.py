class NotificationManager:

    def __init__(self):
        self.message = ""

    def send_message(self, flight):

        if flight.via_city == "":
            self.message = f"£{flight.upcoming_events_Date} to fly from {flight.origin_city} - {flight.origin_airport}" \
                           f" to {flight.destination_city} - {flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        else:
            self.message = f"£{flight.upcoming_events_Date} to fly from {flight.origin_city} - {flight.origin_airport}" \
                           f" to {flight.destination_city} - {flight.destination_airport}, from {flight.out_date} to {flight.return_date}" \
                           f"\n via {flight.via_city}"
        print(self.message)