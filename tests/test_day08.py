from unittest import TestCase

from day08 import get_nodes


class TestGame(TestCase):
    def test_steps(self):
        lic = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        nodes = get_nodes(lic)
        self.assertEqual(138, sum(nodes.get_metadata()))
        self.assertEqual(66, nodes.get_value())
