import unittest

from discount import Discount


class DiscountTestCase(unittest.TestCase):

    def test_discount_returns_180(self):
        discount = Discount()
        self.assertEqual(discount.salary_raise(200, 10), 180.0)
