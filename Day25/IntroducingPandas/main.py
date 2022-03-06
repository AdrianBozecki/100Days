# with open("weather_data.csv") as data_file:
#     data = data_file.read()
#     separated_data = data.split("\n")
#     print(separated_data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
#print(data['temp'])

data_dict = data.to_dict()
#print(data_dict)
temp_list =data["temp"].to_list()
#print(data_list)

maximum_value = data["temp"].max()
#print(maximum_value)

#Get Data in Columns

#print(data.condition)
#print(data["condition"])

#Get Data in Row

#print(data[data.temp == maximum_value])

# monday = data[data.day == "Monday"]
# monday_temp = (int(monday.temp) * 9/5) + 32
# print(monday_temp)


#Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)