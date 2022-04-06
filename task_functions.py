from utility import *


def task_1():
    print(get_json())


def task_2():
    print(tomorrow_forecast(get_json()))


def task_3():
    valid_tfl_transportation()


def task_4():
    print(get_bikepoint_info())


def task_5():
    json_object = get_valid_lines()
    b, t, total = bus_tube_lines(json_object)
    print(f"\nBus line total: {b}\nTube line total: {t}\nCombined total: {total}")


def task_6():
    all_stations = get_line_stations()
    print(
        f"The victoria line has {count_line_stations(all_stations)} stations along it."
    )


def task_7():
    print(plan_journey(get_stop_points(), "bus"))
    print(plan_journey(get_stop_points(), "tube, bus"))
