#!/usr/bin/env python3
import re
from timeit import default_timer as timer

from utils.time import get_time

c = re.compile("#(\d*) @ (\d*),(\d*)\: (\d*)x(\d*)")


def get_grids(claims):
    grid = {}
    for claim in claims:
        g = c.match(claim).groups()
        id, x, y, a, b = list(map(int, g))
        for gx in range(a):
            for gy in range(b):
                coo = (gx + x, gy + y)
                if coo in grid:
                    grid[coo] += [id]
                else:
                    grid[coo] = [id]
    return grid


# compare all grids to all others and store unique intersection
def duplicates(grids):
    return [coo for coo, v in grids.items() if len(v) > 1]


# unique grid simply mean non of the coordinates we had in duplicates.
def unique(grids):
    ids = set()
    bad = set()
    for coo, v in grids.items():
        ids = ids | set(v)
        if len(v) > 1:
            bad = bad | set(v)
    return ids.difference(bad).pop()


if __name__ == "__main__":
    with open('input/day03.txt') as f:
        params = f.read().splitlines()

    start = timer()
    grids = get_grids(params)
    print("got grids ", len(grids), " in ", get_time(start))
    start = timer()
    print("result day 03 part 1: ", len(duplicates(grids)), " in ", get_time(start))
    start = timer()
    print("result day 03 part 2: ", unique(grids), " in ", get_time(start))

