import unittest

from meters_to_mm import Convertion


class ConvertionTestCase(unittest.TestCase):

    def test_meters_to_mm_if_1_meter_returns_1000_mm(self):
        convertion = Convertion()
        self.assertEqual(convertion.meters_to_mm(1), 1000)
