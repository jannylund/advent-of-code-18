#!/usr/bin/env python3
from timeit import default_timer as timer

import re

from day06 import get_limits
from utils.time import get_time

c = re.compile("position=<(.*),(.*)> velocity=<(.*),(.*)>")


class Point:
    def __init__(self, line):
        self.pos_y, self.pos_x, self.move_y, self.move_x = map(int, c.match(line).groups())

    def step(self):
        self.pos_x = self.pos_x + self.move_x
        self.pos_y = self.pos_y + self.move_y

    def get(self):
        return self.pos_x, self.pos_y


def get_points(points):
    result = set()
    for p in points:
        result.add(Point(p))
    return result


def is_alone(coord, other):
    x, y = coord

    neighbours = set([(x + 1, y),
                      (x - 1, y),
                      (x, y - 1),
                      (x, y + 1),
                      (x + 1, y + 1),
                      (x + 1, y - 1),
                      (x - 1, y + 1),
                      (x - 1, y - 1)])

    for n in neighbours:
        if n in other:
            return False

    return True


# convert point set to set of tuples, then loop through coordinates and plot them
def sky(pointset):
    step = 0
    while True:
        # move everything one step.
        step += 1
        for p in pointset:
            p.step()

        # check if coordinates are now aligned.
        ts = set([p.get() for p in pointset])

        # if we have loners, we are not done.
        alone = False
        for t in ts:
            if is_alone(t, ts):
                alone = True
                break

        if alone:
            continue
        else:
            print("Message shown after ", step, " seconds.")
            break

    min_x, min_y, max_x, max_y = get_limits(ts)
    ret = ""
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in ts:
                ret += "#"
            else:
                ret += "."
        ret += "\n"
    return ret


if __name__ == "__main__":
    with open('input/day10.txt') as f:
        lines = f.read().splitlines()

    start = timer()
    print("result day 10 part 1+2: \n")
    print(sky(get_points(lines)), " in ", get_time(start))
