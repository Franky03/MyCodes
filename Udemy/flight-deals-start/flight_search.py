import requests
from datetime import datetime
from flight_data import FlightData


KIWI_ENDPOINT= "https://tequila-api.kiwi.com"
KIWI_API_KEY= "Bs0OT8mfUZunoZRNGNPLkXpDZH6JK-iO"

class FlightSearch:
    def get_code(self, city):
        loc_endpoint= f"{KIWI_ENDPOINT}/locations/query"
        headers= {
            "apikey": KIWI_API_KEY
        }
        query= {
            "term": city,
            "location_types": "city"
        }
        response= requests.get(url=loc_endpoint, headers=headers, params=query)
        results= response.json()['locations']
        code= results[0]['code']
        
        return code
    def check_flights(self, origin_city, destination_city, from_time, to_time):
        headers= {
            "apikey": KIWI_API_KEY
        }
        params= {
            "fly_from": origin_city,
            "fly_to": destination_city,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response= requests.get(url= f"{KIWI_ENDPOINT}/v2/search", headers=headers, params=params)
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None
        
        flight_data= FlightData(price= data["price"], 
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
            )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
