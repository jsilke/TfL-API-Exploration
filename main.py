from constants import *
import os
import json
import requests as re


# -------------------------------------General functions---------------------------------------------

def get_json(url: str, authentication: tuple = (PRIMARY_KEY, SECONDARY_KEY)) -> re.Response:
    """Query the desired API"""
    response = re.get(url, auth=authentication)
    if response.status_code == 200:
        return response.json()
    print(f'API returned:{response.status_code}')


def store_response_json(json_object: dict, file_name: str = MOST_RECENT,
                        directory: str = DIRECTORY) -> None:
    """
    Store response JSON object in a file.
    """
    _path = directory + file_name  # Concatenate the strings.
    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(_path, 'w') as json_file:
        json.dump(json_object, json_file, sort_keys=True, indent=4)


def json_from_file(file_name: str, directory: str = DIRECTORY) -> dict:
    """
    Retrieve a JSON object from a file.
    """
    _path = directory + file_name  # Concatenate the strings.
    try:
        with open(_path) as json_file:
            query_dict = json.load(json_file)
    except FileNotFoundError:
        print(f'{FILE_NOT_FOUND} {_path}')

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


def main():
    json_object = json_from_file(MOST_RECENT)
    solution_3 = valid_tfl_transportation(json_object)
    print(solution_3)


if __name__ == '__main__':
    main()
