from constants import *
import os
import json
import requests as re


# -------------------------------------General functions---------------------------------------------

def get_json(url: str = AIR_QUALITY_URL, parameters: dict = None) -> re.Response:
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
    # TODO: Make the output string pretty.
    """Returns tomorrow's forcast."""
    try:
        _tomorrow_forecast_dict = json_object['currentForecast'][1]
        _tomorrow_forecast_str = f"{_tomorrow_forecast_dict['forecastSummary']}\n\
                                   {_tomorrow_forecast_dict['forecastText']}"  # ^ Explicit line continuation. 🤡
    except KeyError:
        print(f'{KeyError}: {JSON_PARSE_HINT}')

    return _tomorrow_forecast_str


def valid_tfl_transportation(json_object: list) -> tuple[list, int]:
    """
    Takes in response from the GET request to https://api.tfl.gov.uk/Line/Meta/Modes/
    and returns a tuple containing the list of TfL modes of transportation as well
    as the number of elements in the list.
    """
    valid_modes_list = [transportation_mode['modeName']
                        for transportation_mode in json_object
                        if transportation_mode['isTflService']]
    # Make a nicely presentable string.
    valid_modes_string = '\n- '.join(valid_modes_list)

    return (valid_modes_string, len(valid_modes_list))


def get_valid_lines(url: str = ALL_MODES, transportation_modes: str = 'bus, tube') -> re.Response:
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


def get_line_stations(id: str = 'victoria', tfl_only: bool = False, url: str = BASE_LINE):
    _FULL_URL = f'{url}{id}/StopPoints'
    return get_json(_FULL_URL, parameters={'tflOperatedNationalRailStationsOnly': tfl_only})


def count_line_stations(json_object: list) -> int:
    _station_sum = 0
    for station in json_object:
        _station_sum += 1

    return _station_sum


def main():
    json_object = get_line_stations()
    print(count_line_stations(json_object))


if __name__ == '__main__':
    main()
