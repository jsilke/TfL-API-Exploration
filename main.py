import os
import json
import requests as re


# Retrieve API keys from environment variables.
PRIMARY_KEY = os.getenv('TfL_pkey')
SECONDARY_KEY = os.getenv('TfL_skey')


def get_json(url: str = "https://api.tfl.gov.uk/AirQuality/",
             authentication: tuple = (PRIMARY_KEY, SECONDARY_KEY)) -> re.Response:
    """Query the LtF AirQuality API"""
    response = re.get(url, auth=authentication)
    if response.status_code == 200:
        return response.json()
    print(f'API returned:{response.status_code}')


def store_response_json(json_object: dict, file_name='AirQuality.json',
                        directory: str = './data/') -> None:
    """
    Store json in file.
    """
    _path = directory + file_name
    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(_path, 'w') as json_file:
        json.dump(json_object, json_file, sort_keys=True, indent=4)


def json_from_file(path: str = './data/AirQuality.json') -> dict:
    # TODO: test this function!
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
    json_object = get_json()
    store_response_json(json_object)
    print('Done!')


if __name__ == '__main__':
    main()
