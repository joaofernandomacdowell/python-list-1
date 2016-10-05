import unittest

from car_travel import CarTravel


class CarTravelTestCase(unittest.TestCase):

    def test_car_travel_returns_180(self):
        car_travel = CarTravel()
        self.assertEqual(car_travel.car_travel(160, 80), 2)

    def test_car_travel_returns_3_64(self):
        car_travel = CarTravel()
        self.assertGreaterEqual(car_travel.car_travel(200, 55), 3.64)

