
import requests
from pprint import pprint

sheety_endpoint= "https://api.sheety.co/6e3b81f17f597c3092672a4632fc3fb7/flightDeals/prices"

class DataManager:
    def __init__(self):    
        self.destination_data= {}

    def destination(self):
        self.response= requests.get(url= sheety_endpoint)
        data= self.response.json()
        self.destination_data= data['prices']
        return self.destination_data
    
    def update(self):
        for city in self.destination_data:
            new_data= {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            response= requests.put(url= f"https://api.sheety.co/6e3b81f17f597c3092672a4632fc3fb7/flightDeals/prices/{city['id']}", json=new_data)
            print(response.text)
    
    
