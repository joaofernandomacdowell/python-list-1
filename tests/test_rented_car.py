import unittest

from rented_car import RentedCar


class RentedCarTestCase(unittest.TestCase):

    def test_rented_car_returns_60_15(self):
        rented_car = RentedCar()
        self.assertEqual(rented_car.rented_car(1, 10), 61.50)

