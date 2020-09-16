import unittest
from main import get_total
from main import get_price


class MainTestCase(unittest.TestCase):
    """Tests for main.py"""

    def test_get_total(self):
        """Does the output for every age make sense?"""
        # Test edge cases
        self.assertEqual(get_total([3, 4, 18, 19, 64, 65, 100]), (46, True))

        # Test discount
        self.assertEqual(get_total([1, 24, 76, 34]), (28, False))
        self.assertEqual(get_total([1, 24, 76, 34, 90]), (36, True))

    def test_get_price_normal_input(self):
        # Test every age

        prices = [
            0, 0, 0, 5, 5,  # 0 to 4
            5, 5, 5, 5, 5,  # 5 to 9
            5, 5, 5, 5, 5,  # 10 to 14
            5, 5, 5, 10, 10,  # 15 to 19
            10, 10, 10, 10, 10,  # 20 to 24
            10, 10, 10, 10, 10,  # 25 to 29
            10, 10, 10, 10, 10,  # 30 to 34
            10, 10, 10, 10, 10,  # 35 to 39
            10, 10, 10, 10, 10,  # 40 to 44
            10, 10, 10, 10, 10,  # 45 to 49
            10, 10, 10, 10, 10,  # 50 to 54
            10, 10, 10, 10, 10,  # 55 to 59
            10, 10, 10, 10, 8,  # 60 to 64
            8, 8, 8, 8, 8,  # 65 to 69
            8, 8, 8, 8, 8,  # 70 to 74
            8, 8, 8, 8, 8,  # 75 to 79
            8, 8, 8, 8, 8,  # 80 to 84
            8, 8, 8, 8, 8,  # 85 to 89
            8, 8, 8, 8, 8,  # 90 to 94
            8, 8, 8, 8, 8,  # 95 to 99
            8, 8, 8, 8, 8  # 100 to 104
        ]

        for i in range(1, len(prices)):
            self.assertEqual(get_price(i), prices[i - 1])

    def test_get_price_abnormal_input(self):
        self.assertEqual(get_price("test"), ValueError)
        self.assertEqual(get_price(14.5), 1)
