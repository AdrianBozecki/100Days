import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = "adison"

user_parameters = {
    'token': TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

# response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

posting_endpoint = f"{pixela_graph_endpoint}/{graph_config['id']}"

date = datetime.now()

posting_config = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "40.08",
}

# response = requests.post(url=posting_endpoint, json=posting_config, headers=headers)
# print(response.text)

delete_endpoint = f"{posting_endpoint}/20220322"
update_endpoint = f"{posting_endpoint}/20220322"
print(delete_endpoint)

next_pixel_data = {
    "quantity": "50",
}

#response = requests.put(url=update_endpoint,json=next_pixel_data, headers=headers)
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)



