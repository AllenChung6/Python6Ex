from itertools import product
from typing import Iterable, Tuple


def convert_to_kelvin_from_f(fahrenheit_temp: float) -> float:
    kelvin_temp = ((fahrenheit_temp - 32) * 5 / 9 + 273.15)
    return round(kelvin_temp, 2)

    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """


def convert_to_kelvin_from_c(celsius_temp: float) -> int:
    kelvin_temp = (celsius_temp + 273.15)
    return int(kelvin_temp)


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    list = []  # create empty list to put tuple
    for x in temperatures:  # create loop to go through elements in temperatures tuple
        if input_unit_of_measurement == 'f':  # check to see what input_unit_of_measurement is
            index = (x, convert_to_kelvin_from_f(x))  # create a tuple with elements in temperature, and what to convert to
            list.append(index)  # add the new tuple to the list
        elif input_unit_of_measurement == 'c':
            index = (x, convert_to_kelvin_from_c(x))
            list.append(index)
        elif input_unit_of_measurement == 'a':
            index = ()

    return tuple(list)  # add the list to a tuple (there is no append method for tuples, only lists