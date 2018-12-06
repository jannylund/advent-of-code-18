from unittest import TestCase

from day04 import read_log, max_sleep, top_minute, max_freq


class TestGame(TestCase):
    def test_max_sleep(self):
        with open('../input/day04_test.txt') as f:
            params = f.read().splitlines()

        logs = read_log(params)
        sleep_guard = max_sleep(logs)
        self.assertEqual(10, sleep_guard)
        self.assertEqual(24, top_minute(logs, sleep_guard))

        # max freq
        freq_guard = max_freq(logs)
        self.assertEqual(99, freq_guard)
        self.assertEqual(45, top_minute(logs, freq_guard))
