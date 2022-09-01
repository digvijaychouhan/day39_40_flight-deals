from os import environ
import requests

SHEETY_PRICE_ENDPOINT = environ.get("SHEETY_PRICE_ENDPOINT")
SHEETY_ENDPOINT_EMAILS = environ.get("SHEETY_ENDPOINT_EMAILS")
SHEETY_HEADERS = {"Authorization": environ.get("SHEET_API")}


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.email_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICE_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_emails(self):
        response = requests.get(url=SHEETY_ENDPOINT_EMAILS, headers=SHEETY_HEADERS)
        self.email_data = response.json()["users"]
        return self.email_data
