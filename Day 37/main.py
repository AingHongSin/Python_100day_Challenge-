import requests
from datetime import datetime

username = "hongsin"
token = "thisisforsecret"
GRAPH_ID = 'graph1'
# today = datetime.now()
print()


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_params = {
    'id': GRAPH_ID,
    'name': 'Reading Graph',
    'unit': 'page',
    'type': 'int',
    'color': 'sora',
}
HEADER = {
    'X-USER-TOKEN': token
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=HEADER)
# print(response.text)


post_pixelEnpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}"


OPTIONAL_DATA = {
    "The mirical Morning": {
        "chapter1": "It’s Time To Wake Up To Your FULL Potential",
        "chapter": "The Miracle Morning Origin: Born Out of Desperation"
    }
}
today = datetime(year=2021, month = 1, day = 8)

post_pixel_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity": "12",
}

print(today.strftime('%Y%m%d'))


# response = requests.post(url=post_pixelEnpoint, json=post_pixel_config, headers=HEADER)
# print(response.text)


update_pixelendpoint = f"{post_pixelEnpoint}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "5"
}

# response = requests.put(url=update_pixelendpoint, json=update_data, headers=HEADER)
# print(response.text)



delete_pixelendpoint = f"{post_pixelEnpoint}/{today.strftime('%Y%m%d')}"


response = requests.delete(url=delete_pixelendpoint,  headers=HEADER)
print(response.text)