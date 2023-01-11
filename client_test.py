from client import getRatio
import unittest


class TestCases(unittest.TestCase):
    def test_ratio_prices(self):
        self.assertEqual(getRatio(117.38, 116.505), 1.0075104072786576)

    def test_for_zero(self):
        self.assertIsNone(getRatio(125.84, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            getRatio('5', 2)
