import unittest

from smoking_timeline import SmokingTimeLine


class SmokingTimeLineTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.smoking_timeline = SmokingTimeLine()

    def test_smoking_time_line_returns_14600_mins(self):
        self.assertEqual(self.smoking_timeline.smoking_time_line(10, 5), 182500)

