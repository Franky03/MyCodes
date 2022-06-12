from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from flight_data import FlightData

def main():
    data_manager= DataManager()
    sheet_data= data_manager.destination()
    notification = NotificationManager()

    if sheet_data[0]['iataCode']=='':
        from flight_search import FlightSearch
        flight_search= FlightSearch()
        for row in sheet_data:
            row['iataCode']= flight_search.get_code(row['city'])
        print(f'sheet: {sheet_data}')

        data_manager.destination_data= sheet_data
        data_manager.update()
    else:
        return
    ORIGIN_CITY_IATA = "LON" 

    tomorrow= datetime.now() + timedelta(days=1)
    six_months= datetime.now() + timedelta(days= (6* 30))

    for destination in sheet_data:
        flight= flight_search.check_flights(
            ORIGIN_CITY_IATA, 
            destination['iataCode'], 
            from_time= tomorrow, 
            to_time= six_months)
        
        if flight.price < destination["lowestPrice"]:
            notification.send_sms(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )

main()