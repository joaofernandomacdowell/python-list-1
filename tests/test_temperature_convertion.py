import unittest

from temperature_convertion import TemperatureConvertion


class TemperatureConvertionTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_convertion = TemperatureConvertion()

    def test_convert_celsius_to_fahrenheit_returns_86(self):
        self.assertEqual(self.temp_convertion.convert_celsius_to_fahrenheit(30), 86)

    def test_convert_fahrenheit_to_celsius_returns_30(self):
        self.assertEqual(self.temp_convertion.convert_fahrenheit_to_celsius(86), 30)
