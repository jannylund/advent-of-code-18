#!/usr/bin/env python3

from timeit import default_timer as timer

from utils.time import get_time


# Python is superslow on large lists, but rather ok with strings.
def react(polymer):
    units = get_units(polymer)

    last = polymer
    while True:
        for u in units:
            polymer = polymer.replace(u + u.upper(), "")
            polymer = polymer.replace(u.upper() + u, "")

        if polymer != last:
            last = polymer
        else:
            break

    return polymer


# return a set of all unique units (just lowercase)
def get_units(polymer):
    return set(polymer.lower())


def remove(polymer, unit):
    p = polymer.replace(unit, "").replace(unit.swapcase(), "")
    return len(react(p))


def shortest(polymer):
    return min([remove(polymer, x) for x in get_units(polymer)])


if __name__ == "__main__":
    with open('input/day05.txt') as f:
        params = f.read().splitlines()[0]

    start = timer()
    print("result day 05 part 1: ", len(react(params)), " in ", get_time(start))

    start = timer()
    print("result day 05 part 2: ", shortest(params), " in ", get_time(start))
