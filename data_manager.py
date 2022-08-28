import requests

SHEETY_PRICE_ENDPOINT = "https://api.sheety.co//flightDeals/prices"
SHEETY_HEADERS = {"Authorization": "Basic "}


class DataManager:
    def __init__(self):
        self.destination_data = {}

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
