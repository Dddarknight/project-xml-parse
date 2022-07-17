import xml.etree.ElementTree as ET
import os
import json
from xml_diff.dict_diff import make_dict_diff


def xml_difference(file1, file2, output):
    tree1 = ET.parse(file1)
    root1 = tree1.getroot()
    tree2 = ET.parse(file2)
    root2 = tree2.getroot()
    dict1 = make_itineraries(root1)
    dict2 = make_itineraries(root2)
    dict = make_dict_diff(dict1, dict2)
    with open(output, 'w') as write_file:
        write_file.write(json.dumps(dict, indent=4))


def extact_elems_from_flight(flights_list):
    source, time_departure, time_arrival, flights_numbers = '', '', '', ''
    for index, itinerary in enumerate(flights_list):
        if index == 0:
            source = itinerary.find('./Source').text
            time_departure = itinerary.find('./DepartureTimeStamp').text
        destination = itinerary.find('./Destination').text
        source += ' - ' + destination
        flights_numbers += ' - ' + itinerary.find('./FlightNumber').text
        if index == len(flights_list) - 1:
            time_arrival = itinerary.find('./ArrivalTimeStamp').text
    return source, {f'flights_numbers {flights_numbers.strip(" - ")}': {
        'time_departure': time_departure, 'time_arrival': time_arrival
            }
        }  


def make_itineraries(root):
    dict_itineraries = {}
    path_full = "./PricedItineraries/Flights"
    for full_flight in root.findall(path_full):
        onward_flight = full_flight.find("./OnwardPricedItinerary")
        flights_list = onward_flight.findall('./Flights/Flight')
        source, params = extact_elems_from_flight(flights_list)
        dict_itineraries.setdefault(source, {}).update(params)
        return_flight = full_flight.find("./ReturnPricedItinerary")
        if return_flight:
            flight = return_flight.findall('./Flights/Flight')
            source_return, params = extact_elems_from_flight(flight)
            dict_itineraries[source].update({f"Return_itinerary": {source_return: params}})
        pricing = full_flight.findall('./Pricing/ServiceCharges')
        if not pricing:
            continue
        dict_itineraries[source]["Pricing"]={}
        for charge in pricing:
            dict_itineraries[source]["Pricing"].update({f'{charge.attrib}': charge.text})
    return dict_itineraries
