#!/usr/bin/env python3
import operator
from timeit import default_timer as timer

from utils.time import get_time
import re


def parse_game(game):
    return tuple(map(int, re.match("(.*) players; last marble is worth (.*) points", game).groups()))


# Game using python list
class Game:
    def __init__(self):
        self.game = [0]

    def remove(self, pos):
        del self.game[pos]

    def add(self, pos, value):
        self.game.insert(pos, value)

    def size(self):
        return len(self.game)

    def get(self, pos):
        return self.game[pos]


def get_score(game):
    players, marbles = parse_game(game)
    game = Game()
    pos = 0     # position of last placed marble.
    scores = dict()

    for i in range(marbles):
        p = (i % players) + 1   # 1-indexed
        m = i + 1               # marble value
        game_size = game.size()

        if i != 0 and i % 100000 == 0:
            print("loop", i, "done: ", int(m/marbles * 100), "%", get_time(start))

        # Special cases.
        if m % 23 == 0:
            # now find the marble 7 steps left. or it's position.
            pos = (game_size + pos - 7) % game_size
            # add score of marble + the pos 7 left.
            scores = add_score(scores, p, m + game.get(pos))
            game.remove(pos)
        else:
            pos = ((pos + 1) % game_size) + 1
            game.add(pos, m)

    return max(scores.items(), key=operator.itemgetter(1))[1]


def add_score(scores, p, v):
    if p in scores:
        scores[p] = scores[p] + v
    else:
        scores[p] = v
    return scores


if __name__ == "__main__":
    with open('input/day09.txt') as f:
        lines = f.read().splitlines()
        part1 = lines[0]
        part2 = lines[1]

    start = timer()
    print("result day 09 part 1: ", get_score(part1), " in ", get_time(start))

    start = timer()
    print("result day 09 part 2: ", get_score(part2), " in ", get_time(start))
