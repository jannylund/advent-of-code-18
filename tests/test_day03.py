from unittest import TestCase

from day03 import get_grids, duplicates, unique


class TestGame(TestCase):
    def test_parse_claims(self):
        claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        grids = get_grids(claims)
        print(grids)
        self.assertEqual(4, len(duplicates(grids)))

        print(unique(grids))
