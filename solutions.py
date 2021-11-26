from main import *

# Abstracted task solution functions go here!


def task_1():
    print(get_json())


def task_2():
    print(tomorrow_forecast(get_json()))


def task_3():
    valid_tfl_transportation()


def task_4():
    pass


def task_5():
    json_object = get_valid_lines()
    b, t, total = bus_tube_lines(json_object)
    print(
        f"\nBus line total: {b}\nTube line total: {t}\nCombined total: {total}")


def task_6():
    all_stations = get_line_stations()
    tfl_stations = get_line_stations(tfl_only=True)
    print(
        f"Assuming ALL stations: {count_line_stations(all_stations)}\nAssuming TfL stations only: {count_line_stations(tfl_stations)}")


def task_7():
    print(plan_journey(get_stop_points(), 'bus'))
    print(plan_journey(get_stop_points(), 'tube'))
