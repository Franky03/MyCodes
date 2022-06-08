
from datetime import datetime
import requests
import os

TOKEN= "hj33io8567hg"
USERNAME= "kaiky"

#SENDING A DATA WHIT POST

pixela_endpoint= "https://pixe.la/v1/users"
user_params= {
    "token": TOKEN,
    "Username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response= requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

GRAPH_ID= "graph1"
graph_endpoint= f'{pixela_endpoint}/{USERNAME}/graphs'
graph_params= {
    "id": GRAPH_ID,
    "name": "Pages Read",
    "unit": "pages",
    "type": "int",
    "color": "sora"
}
headers={
    "X-USER-TOKEN": TOKEN
}

# response= requests.post(url= graph_endpoint, json=graph_params, headers= headers)
# print(response.text)
now= datetime.now()
DATE= now.strftime("%Y%m%d")
pixel_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params= {
    "date": DATE,
    "quantity": "120",
}

# response= requests.post(url= pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

#UPDATE A DATA WITH PUT

update_pixel= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
update_params= {
    "quantity": "130"
}
# response= requests.put(url= update_pixel, json=update_params, headers=headers)
# print(response.text)

#DELETE A DATA WITH DELETE

response= requests.delete(url=update_pixel, headers=headers)
print(response.text)