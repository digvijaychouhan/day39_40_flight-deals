# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests

FLIGHT_TOKEN = ""
# sheet_endpoint = "https://api.sheety.co/df7f4f644a6e5cc30eb6dafeb0961f82/flightDeals/prices"
# sheet_headers = {"Authorization": "Basic "}
#
# sheet_response = requests.get(url=sheet_endpoint, headers=sheet_headers)
# print(sheet_response.text)


flight_endpoint = "https://tequila-api.kiwi.com/v2/search"
flight_params = {

    "fly_from": "LGA",
    "fly_to": "MIA",
    "dateFrom": "01/09/2022",
    "dateTo": "02/11/2022"
}
flight_headers = {
    "apikey": FLIGHT_TOKEN,
    "Content-Type": "application/json"
}
flight_response = requests.get(url=flight_endpoint, params=flight_params, headers=flight_headers)
print(flight_response.text)
