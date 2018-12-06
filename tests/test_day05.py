from unittest import TestCase

from day05 import react, get_units, remove, shortest


class TestGame(TestCase):
    def test_reaction(self):
        self.assertEqual("", react("aA"))
        self.assertEqual("", react("abBA"))
        self.assertEqual("aabAAB", react("aabAAB"))
        self.assertEqual("dabCBAcaDA", react("dabAcCaCBAcCcaDA"))
        self.assertEqual(10, len(react("dabAcCaCBAcCcaDA")))

    def test_remove_unit(self):
        self.assertEqual({"a","b","c","d"}, get_units("dabAcCaCBAcCcaDA"))
        self.assertEqual(6, remove("dabAcCaCBAcCcaDA", "a"))
        self.assertEqual(8, remove("dabAcCaCBAcCcaDA", "b"))
        self.assertEqual(4, remove("dabAcCaCBAcCcaDA", "c"))
        self.assertEqual(6, remove("dabAcCaCBAcCcaDA", "d"))

    def test_shortest(self):
        self.assertEqual(4, shortest("dabAcCaCBAcCcaDA"))
