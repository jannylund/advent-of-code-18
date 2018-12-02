from unittest import TestCase

from day01 import sum_array, twice


class TestGame(TestCase):

    def test_examples_part1(self):
        self.assertEqual(3, sum_array("+1, -2, +3, +1".split(",")))
        self.assertEqual(3, sum_array("+1, +1, +1".split(",")))
        self.assertEqual(0, sum_array("+1, +1, -2".split(",")))
        self.assertEqual(-6, sum_array("-1, -2, -3".split(",")))

    def test_examples_part2(self):
        self.assertEqual(0, twice("+1, -1".split(",")))
        self.assertEqual(2, twice("+1, -2, +3, +1".split(",")))
        self.assertEqual(10, twice("+3, +3, +4, -2, -4".split(",")))
        self.assertEqual(5, twice("-6, +3, +8, +5, -6".split(",")))
        self.assertEqual(14, twice("+7, +7, -2, -7, -4".split(",")))
