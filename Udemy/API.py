import requests

response= requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response)
#response status code is the number, in this case the response code is 200
#if the url is wrong, the status code will return 404 (not found)

#INSTEAD THIS...

# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code==401:
#     raise Exception("You are not authorised to access this data.")
# elif response.status_code != 200:
#     raise Exception("Bad response from ISS API")

#DO THIS...
response.raise_for_status()

data= response.json()
longitude= data["iss_position"]['longitude']
latitude= data["iss_position"]['latitude']
iss_position= (longitude, latitude)
print(iss_position)
print(f'Longitude:{longitude}\nLatitude:{latitude}')


#API PARAMETERS

response= requests.get('https://api.sunrise-sunset.org/json.')