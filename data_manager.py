import gspread


class DataManager:
    # connecting to google sheets with gspread.
    def __init__(self):
        self.destination_data = {}
        self.flight_data = {}
        self.service_account = gspread.service_account()
        self.sheet = self.service_account.open("Flight Club")
        self.flight_input = self.sheet.worksheet("flight_search_input")
        self.flight_data = self.sheet.worksheet("flight_data")
        self.from_city = []
        self.to_citys = []
        self.prices = []
        self.departure_date = []
        self.total_stops = []

# ============= retrieving data from "Sheet1" in google sheets using get_all_records() ==================
    def get_destination_data(self):
        self.destination_data = self.flight_input.get_all_records()
        return self.destination_data

# ============== accessing individual city names in google sheets ====================
    def get_city(self):
        a_key = "City"
        city_values = [item[a_key] for item in self.destination_data]
        return city_values

    def get_price(self):
        a_key = "Prices"
        price_values = [item[a_key] for item in self.destination_data]
        return price_values

# ===================== Updates destination codes in Google sheets ======================
    def update_destination_codes(self, aiatacodes):
        self.flight_input.update("B2:B100", aiatacodes)

# ==================== appends data to a list to be manipulated later ===================
    def append_to_list(self, flyfrom, flyto, price, departure, stops):
        self.from_city.append(flyfrom)
        self.to_citys.append(flyto)
        self.prices.append(price)
        self.departure_date.append(departure)
        self.total_stops.append(stops)

# ======================== updates data in flight_data sheet ====================
    def update_flight_data(self, flyfrom, flyto, price, departure, stops):
        self.flight_data.update("A2:A100", flyfrom)
        self.flight_data.update("B2:B100", flyto)
        self.flight_data.update("C2:C100", price)
        self.flight_data.update("D2:D100", departure)
        self.flight_data.update("E2:E100", stops)

# list_of_values = wks.get_all_records()
# dict_of_values = wks.get_all_values()
# list_of_cities = wks.get("A2:A10")
# print(list_of_cities)
#
# print(list_of_values)
# print(list_of_values)
