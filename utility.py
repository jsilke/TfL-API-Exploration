from constants import *
import os
import json
import requests as re


# -------------------------------------General functions---------------------------------------------

def get_json(url: str = AIR_QUALITY_URL, parameters: dict = {}) -> re.Response:
    """Query the desired API"""
    _response = re.get(url, params=parameters)
    if _response.status_code == 200:
        return _response.json()
    print(f'API returned: {_response.status_code}')


def store_response_json(json_object: dict, file_name: str = MOST_RECENT,
                        directory: str = DIRECTORY) -> None:
    """
    Store response JSON object in a file.
    """
    _PATH = f'{directory}{file_name}'  # Concatenate the strings.
    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(_PATH, 'w') as _json_file:
        json.dump(json_object, _json_file, sort_keys=True, indent=4)


def json_from_file(file_name: str = MOST_RECENT, directory: str = DIRECTORY) -> dict:
    """
    Retrieve a JSON object from a file.
    """
    _PATH = f'{directory}{file_name}'  # Concatenate the strings.
    try:
        with open(_PATH) as json_file:
            query_dict = json.load(json_file)
    except FileNotFoundError:
        print(f'{FILE_NOT_FOUND} {_PATH}')

    return query_dict

# --------------------------------------API Specific Functions--------------------------------------


def tomorrow_forecast(json_object: dict) -> str:
    """Returns tomorrow's forcast."""
    try:
        _tomorrow_forecast_dict = json_object['currentForecast'][1]
        _tomorrow_forecast_str = f"{_tomorrow_forecast_dict['forecastSummary']}\n{_tomorrow_forecast_dict['forecastText']}"
    except KeyError:
        print(f'{KeyError}: {JSON_PARSE_HINT}')

    return _tomorrow_forecast_str


def valid_tfl_transportation(url: str = VALID_MODES_URL) -> tuple[list, int]:
    """
    Takes in response from the GET request to https://api.tfl.gov.uk/Line/Meta/Modes/
    and returns a tuple containing the list of TfL modes of transportation as well
    as the number of elements in the list.
    """
    json_object = get_json(url)
    valid_modes_list = [transportation_mode['modeName']
                        for transportation_mode in json_object
                        if transportation_mode['isTflService']]
    # Make a nicely presentable string.
    tfl_modes = '\n- '.join(valid_modes_list)

    print(
        f'TfL\'s modes of transportation include:\n- {tfl_modes}\nThus, TfL offers {len(valid_modes_list)} forms of transportation at present.')


def get_valid_lines(url: str = ALL_MODES_URL, transportation_modes: str = 'bus, tube') -> re.Response:
    """
    Retrieves all lines for a comma-separated list of modes.

    transportation_modes = comma separated string e.g. bus, tube.
    """
    _FULL_URL = f"{url}{transportation_modes}"
    return get_json(_FULL_URL)


def bus_tube_lines(json_object: list) -> tuple:
    """
    Returns the total number of bus and tube lines as a dictionary and prints all tube 
    line names.
    """
    tube_sum = 0
    bus_sum = 0

    print("The tube lines of Transport for London are:")

    for line in json_object:
        if line['modeName'] == 'tube':
            print(line['name'])
            tube_sum += 1
        else:
            bus_sum += 1

    total_sum = tube_sum + bus_sum

    return (bus_sum, tube_sum, total_sum)


def get_line_stations(id: str = 'victoria', tfl_only: bool = False, url: str = BASE_LINE_URL):
    _FULL_URL = f'{url}{id}/StopPoints'
    return get_json(_FULL_URL, parameters={'tflOperatedNationalRailStationsOnly': tfl_only})


def count_line_stations(json_object: list) -> int:
    _station_sum = 0
    for station in json_object:
        _station_sum += 1

    return _station_sum


def get_stop_points(origin: str = "Heathrow Airport", destination: str = "Tower Bridge", url: str = STOP_POINTS_URL) -> tuple[str, str]:
    """Get stop point coordinates for origin and destination and return them as a tuple."""
    origin, destination = get_json(url, parameters={'query': origin}),\
        get_json(url, parameters={'query': destination})

    # Get the latitude and longitude as comma separated strings for origin and destination.
    origin_lat_lon, destination_lat_lon = f"{origin['matches'][0]['lat'], origin['matches'][0]['lon']}",\
                                          f"{destination['matches'][0]['lat'], destination['matches'][0]['lon']}"

    return (origin_lat_lon.strip('()'), destination_lat_lon.strip('()'))


def plan_journey(from_and_to: tuple[str, str], mode: str, url: str = JOURNEY_RESULTS_URL):
    """Currently only works for bus and tube, can be generalized easily."""
    _JOURNEY_URL = f"{url}{from_and_to[0]}/to/{from_and_to[1]}"

    trip = get_json(_JOURNEY_URL, parameters={'mode': mode})
    store_response_json(trip)
    trip_duration = trip['journeys'][0]['duration']

    # Location needs to be generalized.
    return f'A {mode} trip from Heathrow Airport to Tower Bridge will take {trip_duration} minutes.'


def get_bikepoint_info(url: dict = ALL_BIKEPOINTS_URL):
    """Parse BikePoint JSON to extract the number of bike points and docks."""
    _bike_points = get_json(url)
    _bike_point_quantity = len(_bike_points)

    _bike_sum = 0
    _empty_dock_sum = 0
    _dock_sum = 0

    for _bike_point in _bike_points:
        _empty_dock_sum += int(_bike_point['additionalProperties']
                               [-2]['value'])
        _dock_sum += int(_bike_point['additionalProperties'][-1]['value'])
        _bike_sum += int(_bike_point['additionalProperties'][-3]['value'])

    return f"TfL operates {_bike_point_quantity} bike points at present.\nThese bike points have a total of {sum((_empty_dock_sum, _dock_sum))} docks of which {_empty_dock_sum} are empty and {_dock_sum} are not.\nThere are currently {_dock_sum - (_bike_sum + _empty_dock_sum)} docks in a state of disrepair."
