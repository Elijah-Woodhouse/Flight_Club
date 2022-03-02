from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime
from dateutil.relativedelta import *


data_manager = DataManager()
flight_search = FlightSearch()


TODAY = datetime.now()
HENCEFORTH = TODAY + relativedelta(months=6)
HOME_CITY_IATA = flight_search.get_destination_code("Salt Lake City")
TIME_FORMAT = '%d/%m/%Y'


# ============= getting Google sheet data from Data_Manager and storing it in sheet_data variable ==================
# ============================ getting a list of cities from sheet. ===============================
sheet_data = data_manager.get_destination_data()
list_of_cities = data_manager.get_city()


# ================ passing each individual city into the flight_search finder to =================
# ============================ retrieve iata code for that city =============================================
iata_codes = []
for item in list_of_cities:
    list_of_iata_codes = flight_search.get_destination_code(item)
    iata_codes.append(list_of_iata_codes)
# ============ creating a list of lists where every list item is an aita code to be passed =====================
# ============================= into the update_destination_codes() function. ==================
    append_code_list = [[item] for item in iata_codes]


# ================== Updating google sheets with Iata codes ===================
data_manager.update_destination_codes(append_code_list)
# print(append_code_list)

# =============================== Calling FlightSearch class to search for flights using tequila =======================
for item in iata_codes:
    data = flight_search.search_flights(
        home_city_iata=HOME_CITY_IATA,
        fly_to_iata=str(item),
        adlt_num=1,
        children=0,
        adult_bag=1,
        from_time=TODAY.strftime(TIME_FORMAT),
        to_time=HENCEFORTH.strftime(TIME_FORMAT)
    )
    from flight_data import FlightData
    try:
        flight_data = FlightData(
            flyfrom=data["flyFrom"],
            home_city="Salt Lake City",
            fly_to_iata=data["flyTo"],
            to_city=data["cityTo"],
            price=data["price"],
            date_from=data["local_departure"].split("T"),
            return_date=['duration'],
            stops=data["technical_stops"]
            )

        data_manager.append_to_list(
            flyfrom=flight_data.home_city,
            flyto=flight_data.to_city,
            price=flight_data.price,
            departure=flight_data.date_from,
            stops=flight_data.stops
        )
    except TypeError:
        pass
    except KeyError:
        pass


from_city = [[item] for item in data_manager.from_city]
to_citys = [[item] for item in data_manager.to_citys]
nested_price = [[item] for item in data_manager.prices]
departure = [[item[0]] for item in data_manager.departure_date]
stops = [[item] for item in data_manager.total_stops]


data_manager.update_flight_data(
    flyfrom=from_city,
    flyto=to_citys,
    price=nested_price,
    departure=departure,
    stops=stops
)
