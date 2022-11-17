import requests
import os
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
BASIC = os.environ.get("BASIC")
# response = requests.get(f"https://api.sheety.co/{BASIC}/flightDeals/prices",
#                         auth=(USERNAME, PASSWORD))
# print(response.json())


class DataManager:
    def __init__(self):
        self.destination_data = {}
        # self.update_destination_code()

    def get_destination_data(self):
        sheet_endpoint = f"https://api.sheety.co/{BASIC}/flightDeals/prices"
        response = requests.get(sheet_endpoint,
                                auth=(USERNAME, PASSWORD))
        data = response.json()["prices"]

        return data

    def update_destination_code(self):
        print(self.destination_data)
        for row in self.destination_data:
            # self.update_destination_code(row["id"])
            print(row)
            sheety_header = {
                "Authorization": f"Basic {'Zm5hbWxhaDoxMjM0NTY3ODlGYWlzYWw='}",
                "Content-Type": "application/json"
            }
            sheet_endpoint = f"https://api.sheety.co/{BASIC}/flightDeals/prices/{row['id']}"
            body = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            put_req = requests.put(url=sheet_endpoint, json=body, headers=sheety_header)
            print(put_req.status_code)
        # print(put_req.status_code)

