from unittest import TestCase

from day02.day02 import checksum, list_checksum, diff_one


class TestGame(TestCase):

    def test_checksum(self):
        self.assertEqual((0, 0), checksum("abcdef"))
        self.assertEqual((1, 1), checksum("bababc"))
        self.assertEqual((1, 0), checksum("abbcde"))
        self.assertEqual((0, 1), checksum("abcccd"))
        self.assertEqual((1, 0), checksum("aabcdd"))
        self.assertEqual((1, 0), checksum("abcdee"))
        self.assertEqual((0, 1), checksum("ababab"))

    def test_list_checksum(self):
        l = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        self.assertEqual(12, list_checksum(l))

    def test_find_diff_one(self):
        l = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
        self.assertEqual("fgij", diff_one(l))
