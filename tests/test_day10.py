from unittest import TestCase

from day10 import get_points, sky


class TestGame(TestCase):
    def test_game(self):
        with open('../input/day10_test.txt') as f:
            lines = f.read().splitlines()

        print(sky(get_points(lines)))

