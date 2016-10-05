import unittest

from time_to_seconds import TimeConvertion


class TimeConvertionTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.time_convertion = TimeConvertion()

    def test_time_to_seconds_return_86400_seconds_if_days_equals_to_1(self):
        self.assertEqual(self.time_convertion.time_to_seconds(1, 0, 0, 0), 86400)

    def test_time_to_seconds_returns_3600_seconds_if_hour_equals_to_1(self):
        self.assertEqual(self.time_convertion.time_to_seconds(0, 1, 0, 0), 3600)

    def test_time_to_seconds_returns_60_seconds_if_min_equals_to_1(self):
        self.assertEqual(self.time_convertion.time_to_seconds(0, 0, 1, 0), 60)

    def test_time_to_seconds_returns_60_seconds_if_sec_equals_to_50(self):
        self.assertEqual(self.time_convertion.time_to_seconds(0, 0, 0, 50), 50)

    def test_time_to_seconds_returns_95430_if_time_equals_to_1_2_30_30(self):
        self.assertEqual(self.time_convertion.time_to_seconds(1, 2, 30, 30), 95430)

    def test_time_to_seconds_raise_error_if_any_value_is_less_then_0(self):
        # self.assertRaises(ValueError, self.time_convertion.time_to_seconds, 0, 0, -1, 0)
        with self.assertRaises(ValueError):
            self.time_convertion.time_to_seconds(0, 0, -1, 0)
