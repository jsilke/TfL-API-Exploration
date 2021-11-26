import os

# ------------------------------------------API-specific--------------------------------------------

# Retrieve API keys from environment variables.
PRIMARY_KEY = os.getenv('TfL_pkey')
SECONDARY_KEY = os.getenv('TfL_skey')
AIR_QUALITY_URL = "https://api.tfl.gov.uk/AirQuality/"
VALID_MODES_URL = "https://api.tfl.gov.uk/Line/Meta/Modes/"

# ----------------------------------------Local Pathing---------------------------------------------

DIRECTORY = './data/'
MOST_RECENT = 'most_recent.json'

# ---------------------------------------Reusable Strings-------------------------------------------

JSON_PARSE_HINT = 'Expected JSON-formatted response from the TfL API.'
FILE_NOT_FOUND = 'FileNotFoundError - No such file or directory:'  # Custom message
