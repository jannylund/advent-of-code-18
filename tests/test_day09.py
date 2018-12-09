from unittest import TestCase

from day09 import get_score, Game


class TestGame(TestCase):
    def test_game(self):
        game = Game()
        game.add(1, 2)
        game.add(2, 1)
        game.add(3, 3)

        # Size should now be 4
        self.assertEqual(4, game.size())

        # Getting position 2 should return 1.
        self.assertEqual(1, game.get(2))

        # Adding to position 2 should be possible and size should grow to 5
        self.assertEqual(None, game.add(2, 111))
        self.assertEqual(5, game.size())

        # Getting position 2 now should return 111 and 1 moved to pos 3
        self.assertEqual(111, game.get(2))
        self.assertEqual(1, game.get(3))

        # Deleting position 2 and then getting it again, should return 1
        self.assertEqual(None, game.remove(2))
        self.assertEqual(4, game.size())
        self.assertEqual(1, game.get(2))


    def test_steps(self):
        self.assertEqual(32, get_score("9 players; last marble is worth 25 points"))
        self.assertEqual(8317, get_score("10 players; last marble is worth 1618 points"))
        self.assertEqual(146373, get_score("13 players; last marble is worth 7999 points"))
        self.assertEqual(2764, get_score("17 players; last marble is worth 1104 points"))
        self.assertEqual(54718, get_score("21 players; last marble is worth 6111 points"))
        self.assertEqual(37305, get_score("30 players; last marble is worth 5807 points"))
