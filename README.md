# Transport for London API exploration ![Issues](https://img.shields.io/github/issues/jsilke/TfL-API-Exploration) ![Last Commit](https://img.shields.io/github/last-commit/jsilke/TfL-API-Exploration) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repo is adapted from the [first mini-project](https://github.com/lighthouse-labs/mini-project-I) in Lighthouse Labs' Data Science bootcamp.

## Motivation

The main goal of this project is to practice making HTTP requests and extracting values from complex lists and nested dictionaries using the [Transport for London API](https://api-portal.tfl.gov.uk/apis).

The results of the following tasks were suggested for presentation:

- [x] Print a response JSON object from TfL's [AirQuality API](https://api-portal.tfl.gov.uk/api-details#api=AirQuality&operation=AirQuality_Get).
- [x] Parse the dictionary and print the AirQuality predictions for tomorrow.
- [x] List the different modes of transport which are operated by TfL. State how many modes they have.
- [x] State the number of BikePoints in London that are operated by TfL. State the total number of docks in **all** BikePoints.
- [x] State the number of tube and bus lines in London. Print the names of all tube lines.
- [x] State the number of stations on the `victoria` line.
- [x] Plan the journey from Heathrow Airport to Tower Bridge using Bus and Tube and display the version of each in minutes.

The solutions to these tasks are provided in the [solutions notebook](./solutions.ipynb).

## Structure

```bash
.
│   .gitignore
│   README.md
│   constants.py      # API configuration constants.
│   solutions.ipynb   # Notebook containing task solutions.
│   task_functions.py # Abstracted functions for each task.
│   utility.py        # Utility functions to solve the tasks.
```

## How to use this project

Open the [solutions notebook](./solutions.ipynb) and run all cells to produce current solutions to the tasks directly from [TfL's API](https://api-portal.tfl.gov.uk/apis).