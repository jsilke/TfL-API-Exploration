import os
import json
import requests as re

# Retrieve API keys from environment variables.
PRIMARY_KEY = os.getenv('TfL_pkey')
SECONDARY_KEY = os.getenv('TfL_skey')

# Remove from global namespace later.
url_keys_append = f'?app_id={PRIMARY_KEY}&app_key={SECONDARY_KEY}'
url = "https://api.tfl.gov.uk/AirQuality"


def store_response_json(json_object: dict, path: str = './data/AirQuality.json') -> None:
    """
    Store json in file.
    """
    with open(path, 'a') as json_file:
        json.dump(json_object, json_file)


def dict_from_json(path: str = './data/AirQuality.json') -> dict:
    """
    Retrieve json from file.
    """
    try:
        with open(path) as json_file:
            query_dict = json.load(json_file)
    except FileNotFoundError:
        print(f'FileNotFoundError - No such file or directory: {path}')

    return query_dict


def main():
    dict_from_json()


if __name__ == '__main__':
    main()
