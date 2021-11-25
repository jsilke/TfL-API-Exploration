import os
import json
import requests as re

# Retrieve API keys from environment variables.
PRIMARY_KEY = os.getenv('TfL_pkey')
SECONDARY_KEY = os.getenv('TfL_skey')

# Remove from global namespace later.
url_keys_append = f'?app_id={PRIMARY_KEY}&app_key={SECONDARY_KEY}'
url = "https://api.tfl.gov.uk/AirQuality"


def store_request_json(json: dict, path: str = './data/AirQuality.json') -> None:
    with open(path, 'a') as json_file:
        json_file.write(json)


def main():
    pass


if __name__ == '__main__':
    main()
