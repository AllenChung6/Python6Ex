from itertools import product
from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    celsius_temp = (fahrenheit_temp - 32.0) * 5 / 9
    return round(celsius_temp, 2)

    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """


def convert_to_fahrenheit(celsius_temp: float) -> int:
    fahrenheit_temp = (celsius_temp * 9 / 5) + 32
    return int(fahrenheit_temp)

    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    list = []  # create empty list to put tuple
    for x in temperatures:  # create loop to go through elements in temperatures tuple
        if input_unit_of_measurement == 'f':  # check to see what input_unit_of_measurement is
            index = (x, convert_to_celsius(x))  # create a tuple with elements in temperature, and what to convert to
            list.append(index)  # add the new tuple to the list
        elif input_unit_of_measurement == 'c':
            index = (x, convert_to_fahrenheit(x))
            list.append(index)
        elif input_unit_of_measurement == 'a':
            index = ()

    return tuple(list)  # add the list to a tuple (there is no append method for tuples, only lists

    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
