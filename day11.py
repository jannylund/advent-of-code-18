#!/usr/bin/env python3
import operator
from timeit import default_timer as timer

from utils.time import get_time


def get_power(coord, serial):
    x, y = coord
    rack_id = x + 10
    power = rack_id * y  # step 1: rack * y
    power = power + serial  # step 2: power + serial
    power = power * rack_id  # step 3: power * rack_id
    power = int(power / 100) % 10  # step 4: keep only the 100 digit. 12345 -> 3
    power = power - 5  # step 5: remove 5
    return power


# make a 1,1 -> 300,300 grid with powers
def get_grid(serial):
    grid = dict()
    for x in range(1, 301):
        for y in range(1, 301):
            grid[(x, y)] = get_power((x, y), serial)
    return grid


def get_largest_total_power(serial):
    grid = get_grid(serial)

    # summarize 3x3 groups to the starting coordinate.
    power = dict()
    for x in range(1, 299):
        for y in range(1, 299):
            # get the 3x3 coordinates
            triple = [(rx, ry) for rx in range(x, x + 3) for ry in range(y, y + 3)]
            # get the values from the grid and summarize them
            f = operator.itemgetter(*triple)
            power[(x, y)] = sum(f(grid))

    # return the largest power and it's coordinates.
    coord = max(power.items(), key=operator.itemgetter(1))[0]
    return coord, power[coord]


# same but but unlimited size
def get_largest_total_power2(serial):
    grid = get_grid(serial)
    grid_limit = 301  # add one since range is excluding last one.

    # summarize any size groups to the starting coordinate + size.
    power = dict()
    power[0] = 0
    for x in range(1, grid_limit):
        print("Checking x: ", x)
        for y in range(1, grid_limit):
            # we always look at a square, so it's size is between 1x1 and 300x300, whatever fits.
            size_max = min(grid_limit - x, grid_limit - y)  # go with the minimum size.

            # No need to loop size 1, we already know it.
            power[(x, y, 1)] = grid[(x, y)]
            for size in range(2, size_max):
                # Start from previous sum and just add the extra outliers
                s_sum = power[(x, y, size - 1)]

                # Add all y-max coordinates.
                ry = y + size - 1
                for rx in range(x, x + size):
                    s_sum += grid[(rx, ry)]

                # Add all x-max coordinates (minus the last since we already added the corner.)
                rx = x + size - 1
                for ry in range(y, y + size - 1):
                    s_sum += grid[(rx, ry)]

                power[(x, y, size)] = s_sum

    # return the largest power and it's coordinates.
    coord = max(power.items(), key=operator.itemgetter(1))[0]
    return coord, power[coord]


if __name__ == "__main__":
    start = timer()
    coord, power = get_largest_total_power(1723)
    print("result day 11 part 1: ", coord, " power: ", power, " in ", get_time(start))
    coord, power = get_largest_total_power2(1723)
    print("result day 11 part 2: ", coord, " power: ", power, " in ", get_time(start))
