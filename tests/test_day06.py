from unittest import TestCase

from day06 import get_coord, get_limits, mht, closest, calc_area, remove_infinite, largest_area, calc_region


class TestGame(TestCase):
    def test_coordinates(self):
        params = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
        expected = set([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
        coords = get_coord(params)
        self.assertEqual(expected, coords)

        limits = (1, 1, 8, 9)
        self.assertEqual(limits, get_limits(coords))

    def test_manhattan(self):
        coord = (0, 0)
        self.assertEqual(0, mht(coord, coord))
        self.assertEqual(1, mht(coord, (0, 1)))
        self.assertEqual(1, mht(coord, (1, 0)))
        self.assertEqual(6, mht(coord, (3, 3)))

    def test_closest(self):
        coords = set([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
        self.assertEqual((1, 1), closest((1, 1), coords))
        self.assertEqual((1, 1), closest((1, 2), coords))
        self.assertEqual((1, 6), closest((1, 5), coords))
        self.assertEqual(None, closest((1, 4), coords))

    def test_remove_infinite(self):
        coords = set([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
        finite = set([(3, 4), (5, 5)])
        area = calc_area(coords)
        self.assertEqual(finite, remove_infinite(coords, area))

    def test_calc_area(self):
        coords = set([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
        self.assertEqual(17, largest_area(coords))

    def test_calc_regions(self):
        coords = set([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
        self.assertEqual(16, calc_region(coords, 32))
