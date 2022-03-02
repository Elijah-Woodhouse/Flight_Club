from flight_search import FlightSearch
flight_search = FlightSearch()


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API_KEY = "us1WARyt_3sGA1E3t-Q8bm4NkprA46OM"


class FlightData:
    def __init__(self, flyfrom, home_city,
                 fly_to_iata, to_city,
                 price, date_from,
                 return_date, stops):
        self.fly_from = flyfrom
        self.home_city = home_city
        self.fly_to = fly_to_iata
        self.to_city = to_city
        self.price = price
        self.date_from = date_from
        self.date_to = return_date
        self.stops = stops

