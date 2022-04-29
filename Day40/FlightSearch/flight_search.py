import requests
from flight_data import FlightData
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "QjwG1VH8-7wNpsZFfLxw-Hkb2cbLsVTW"

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

    def search_for_flights(self, origin_city_code, destination_city_code, from_time, to_time, nht_in_dst_from,
                           nht_in_dst_to):
        params = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": nht_in_dst_from,
            "nights_in_dst_to": nht_in_dst_to,
            "flight_type": "round",
            'one_for_city': 1,
            'curr': 'GBP',
            'max_stopovers': 0,
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            try:
                params['max_stopovers'] = 1
                response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=headers)
                data = response.json()["data"][0]

                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    max_stopovers=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
            except IndexError:
                print(f"We didn't find flight to {destination_city_code}")
                return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
