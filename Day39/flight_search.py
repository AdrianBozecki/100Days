import requests
from flight_data import FlightData
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = ""

headers = {
    'apikey': TEQUILA_API_KEY
}


class FlightSearch:

    def get_destination_code(self, city):
        params = {
            'term': city
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=headers)
        code = response.json()['locations'][0]['code']
        return code

    def search_for_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 1,
            "nights_in_dst_to": 2,
            "flight_type": "round",
            'one_for_city': 1,
            'curr': 'GBP',
            'max_stopovers': 0,
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            #print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        #print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
