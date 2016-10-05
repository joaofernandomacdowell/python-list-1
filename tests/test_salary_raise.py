import unittest

from salary_raise import SalaryRaise


class SalaryRaiseTestCase(unittest.TestCase):

    def test_calculate_raise_returns_1_1(self):
        calculate = SalaryRaise()
        self.assertEqual(calculate.calculate_raise(10), 1.1)

    def test_salary_raise_returns_100(self):
        salary_raise = SalaryRaise()
        self.assertEqual(salary_raise.salary_raise(100, 10), 110)

    def test_salary_raise_returns_130(self):
        salary_raise = SalaryRaise()
        self.assertEqual(salary_raise.salary_raise(100, 30), 130)
