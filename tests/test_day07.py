from unittest import TestCase

from day07 import read_inst, timed_order_inst, get_char_time


class TestGame(TestCase):
    def test_steps(self):
        with open('../input/day07_test.txt') as f:
            params = f.read().splitlines()

        instructions = read_inst(params)
        self.assertEqual("CABDFE", timed_order_inst(instructions)[1])

    def test_char_time(self):
        self.assertEqual(1, get_char_time('A'))
        self.assertEqual(26, get_char_time('Z'))

    def test_timed_steps(self):
        with open('../input/day07_test.txt') as f:
            params = f.read().splitlines()

        instructions = read_inst(params)
        self.assertEqual((15, "CABFDE"), timed_order_inst(instructions, 2, 0))
