import os

# ------------------------------------------API-specific--------------------------------------------

AIR_QUALITY_URL = "https://api.tfl.gov.uk/AirQuality/"
VALID_MODES_URL = "https://api.tfl.gov.uk/Line/Meta/Modes/"
ALL_BIKEPOINTS_URL = "https://api.tfl.gov.uk/BikePoint/"
ALL_MODES = "https://api.tfl.gov.uk/Line/Mode/"
BASE_LINE = "https://api.tfl.gov.uk/Line/"

# ----------------------------------------Local Pathing---------------------------------------------

DIRECTORY = './data/'
MOST_RECENT = 'most_recent.json'

# ---------------------------------------Reusable Strings-------------------------------------------

JSON_PARSE_HINT = 'Expected JSON-formatted response from the TfL API.'
FILE_NOT_FOUND = 'FileNotFoundError - No such file or directory:'  # Custom message
