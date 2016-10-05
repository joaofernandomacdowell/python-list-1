import unittest

from sum_two_numbers import Calculator


class CalculatorTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calculator = Calculator()

    def test_when_sum_2_plus_2_returns_4(self):
        self.assertEqual(self.calculator.sum_two_numbers(2, 2), 4)

    def test_when_sum_3_plus_4_returns_7(self):
        self.assertEqual(self.calculator.sum_two_numbers(3, 4), 7)
