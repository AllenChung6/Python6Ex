import unittest
import temperature_utils_v2
from typing import Iterable, Tuple


class TemperatureUtilsV2Test(unittest.TestCase):

    def test_convert_to_kelvin_from_f(self):
        test_cases = [
            (32, 273.15),
            (68, 293.15),
            (100, 310.93),
            (104, 313.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_kelvin_from_f(temp_in))

    def test_convert_to_kelvin_from_c(self):
        test_cases = [
            (-17.7778, 255),
            (0, 273),
            (100, 373)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_kelvin_from_c(temp_in))

    def test_temperature_tuple(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 273.15), (68, 293.15), (100, 310.93), (104, 313.15))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "f")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 255), (0, 273), (100, 373))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "c")
        self.assertEqual(expected, actual)

    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils_v2.temperature_tuple(temps_input, "a"))
