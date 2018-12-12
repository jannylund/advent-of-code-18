from unittest import TestCase

from day11 import *


class TestGame(TestCase):
    def test_helpers(self):
        self.assertEqual(4, get_power((3, 5), 8))
        self.assertEqual(-5, get_power((122, 79), 57))
        self.assertEqual(0, get_power((217, 196), 39))
        self.assertEqual(4, get_power((101, 153), 71))

    def test_grid(self):
        grid = get_grid(18)
        self.assertEqual(4, grid[(33, 45)])
        self.assertEqual(4, grid[(34, 45)])
        self.assertEqual(4, grid[(35, 45)])
        self.assertEqual(-5, grid[(36, 45)])

    def test_power(self):
        coord, power = get_largest_total_power(18)
        self.assertEqual((33, 45), coord)
        self.assertEqual(29, power)

        coord, power = get_largest_total_power(42)
        self.assertEqual((21, 61), coord)
        self.assertEqual(30, power)

    def test_anysize_power(self):
        coord, power = get_largest_total_power2(18)
        self.assertEqual((90, 269, 16), coord)
        self.assertEqual(113, power)

        coord, power = get_largest_total_power2(42)
        self.assertEqual((232, 251, 12), coord)
        self.assertEqual(119, power)
