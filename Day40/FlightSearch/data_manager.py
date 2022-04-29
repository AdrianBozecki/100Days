import requests
import pandas as pd


class DataManager:

    def __init__(self):
        self.df = {}
        self.list_of_cities = []
        self.count_of_data = 0

    def get_destination_data(self):
        self.df = pd.read_csv("cities_data.csv").to_dict()
        self.count_of_data = range(len(self.df['City']))
        self.list_of_cities = []
        for i in self.count_of_data:
            data = (self.df['City'][i], self.df['IATA Code'][i])
            self.list_of_cities.append(data)
        return self.list_of_cities

    def update_destination_data(self, city, flight_search):
        iata_code = flight_search.get_destination_code(city)
        data = f"\n{city.title()},{iata_code}"
        with open("cities_data.csv", "a") as file:
            file.write(data)

