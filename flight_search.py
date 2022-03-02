import requests


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = "us1WARyt_3sGA1E3t-Q8bm4NkprA46OM"


class FlightSearch:

    def get_destination_code(self, city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "term": city_name,
            "local": "en-US",
            "location_types": "city"}

        response = requests.get(url=TEQUILA_ENDPOINT, params=query, headers=headers)
        results = response.json()["locations"]
        for item in results:
            code = item["code"]
            return code

    def search_flights(self, home_city_iata, fly_to_iata, adlt_num, children, adult_bag, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": home_city_iata,
            "fly_to": fly_to_iata,
            "date_from": from_time,
            "date_to": to_time,
            "flight_type": "oneway",
            "one_for_city": 1,
            "adults": adlt_num,
            "children": children,
            "adult_hold_bag": adult_bag,
            "max_stopovers": 2,
            "curr": "USD",
        }

        try:
            response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=query, headers=headers)
            data = response.json()
            # price = data["price"]
            # city = data["cityTo"]
            # print(data[0])
            # print(f"minimum price to pay is {price}")
            print(data)
            return data["data"][0]
        except IndexError:
            return data["data"]
        except KeyError:
            return data
