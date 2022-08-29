ALL_FLIGHTS_PATH = "./PricedItineraries/Flights"
ONWARD_PATH = "./OnwardPricedItinerary"
FLIGHT_PATH = "./Flights/Flight"
RETURN_PATH = "./ReturnPricedItinerary"
PRICE_PATH = "./Pricing/ServiceCharges"
TIME_DEPARTURE_PATH = './DepartureTimeStamp'
TIME_ARRIVAL_PATH = './ArrivalTimeStamp'
FLIGHT_NUMBER_PATH = './FlightNumber'
SOURCE_PATH = './Source'
DESTINATION_PATH = './Destination'


def extact_params_from_flight(flights_list):
    source, time_departure, time_arrival, flights_numbers = '', '', '', ''
    for index, itinerary in enumerate(flights_list):
        if index == 0:
            source = itinerary.find(SOURCE_PATH).text
            time_departure = itinerary.find(TIME_DEPARTURE_PATH).text
        destination = itinerary.find(DESTINATION_PATH).text
        source += f' - {destination}'
        flights_numbers += f' - {itinerary.find(FLIGHT_NUMBER_PATH).text}'
        if index == len(flights_list) - 1:
            time_arrival = itinerary.find(TIME_ARRIVAL_PATH).text
    time = {'time_departure': time_departure, 'time_arrival': time_arrival}
    params = {f"flights_numbers {flights_numbers.strip(' - ')}": time}
    return source, params


def make_itineraries_tree(data):
    itineraries_dict = {}
    for full_flight in data.findall(ALL_FLIGHTS_PATH):
        onward_flight = full_flight.find(ONWARD_PATH)
        flights_list = onward_flight.findall(FLIGHT_PATH)
        source, params = extact_params_from_flight(flights_list)
        itineraries_dict.setdefault(source, {}).update(params)
        return_flight = full_flight.find(RETURN_PATH)
        if return_flight:
            flight = return_flight.findall(FLIGHT_PATH)
            source_return, params = extact_params_from_flight(flight)
            return_dict = {"Return_itinerary": {source_return: params}}
            itineraries_dict[source].update(return_dict)
        pricing = full_flight.findall(PRICE_PATH)
        if not pricing:
            continue
        itineraries_dict[source]["Pricing"] = {}
        for charge in pricing:
            charge_dict = {f'{charge.attrib}': charge.text}
            itineraries_dict[source]["Pricing"].update(charge_dict)
    return itineraries_dict
