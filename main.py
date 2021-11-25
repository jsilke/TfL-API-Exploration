from constants import *
import os
import json
import requests as re


def get_json(url: str, authentication: tuple = (PRIMARY_KEY, SECONDARY_KEY)) -> re.Response:
    """Query the LtF AirQuality API"""
    response = re.get(url, auth=authentication)
    if response.status_code == 200:
        return response.json()
    print(f'API returned:{response.status_code}')


def store_response_json(json_object: dict, file_name: str = MOST_RECENT,
                        directory: str = DIRECTORY) -> None:
    """
    Store json in file.
    """
    _path = directory + file_name  # Concatenate the strings.
    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(_path, 'w') as json_file:
        json.dump(json_object, json_file, sort_keys=True, indent=4)


def json_from_file(file_name: str, directory: str = DIRECTORY) -> dict:
    """
    Retrieve json from file.
    """
    _path = directory + file_name  # Concatenate the strings.
    try:
        with open(_path) as json_file:
            query_dict = json.load(json_file)
    except FileNotFoundError:
        print(f'{FILE_NOT_FOUND} {_path}')

    return query_dict


def tomorrow_forecast(json_object: dict) -> str:
    # TODO: Make the output string pretty.
    """Returns tomorrow's forcast."""
    try:
        _tomorrow_forecast_dict = json_object['currentForecast'][1]
        # Explicit line continuation.
        _tomorrow_forecast_str = f"{_tomorrow_forecast_dict['forecastSummary']}\n\
                                   {_tomorrow_forecast_dict['forecastText']}"
    except KeyError:
        print(f'{KeyError}: {JSON_PARSE_HINT}')

    return _tomorrow_forecast_str


# -------------------------------------------------TASK 2-----------------------------------------------


def main():
    json_object = json_from_file()
    print(tomorrow_forecast(json_object))


if __name__ == '__main__':
    main()
