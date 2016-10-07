import unittest

from len_two_million import LenTwoMillion


class LenOneMillionTestCase(unittest.TestCase):

    def test_len_one_million_if_number_equals_2000000_returns_7(self):
        len_two_million = LenTwoMillion()
        self.assertEqual(len_two_million.len_string(), 7)

