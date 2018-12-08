#!/usr/bin/env python3
import operator
from timeit import default_timer as timer

from utils.time import get_time


# Convert coordinate strings to tuples.
def get_coord(coord):
    return set(tuple(map(int, c.split(","))) for c in coord)


# Get limits of the area we need to care about (min/max coordinates)
def get_limits(coords):
    min_x = min(x[0] for x in coords)
    min_y = min(y[1] for y in coords)
    max_x = max(x[0] for x in coords)
    max_y = max(y[1] for y in coords)
    return min_x, min_y, max_x, max_y


# Calculate manhattan distance between two coordinates.
def mht(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


# Calculate which coordinate is closest to a given coordinate.
# {distance: {c1, c2}}
def closest(target, coords):
    if target in coords:
        return target
    else:
        dist = dict()
        for c in coords:
            d = mht(target, c)
            if d in dist:
                dist[d] += [c]
            else:
                dist[d] = [c]
        min_d = min(dist.keys())
        if len(dist[min_d]) == 1:
            return dist[min_d][0]

        return None


# Calculate closest coordinate for all positions in range
# {pos: closest}
def calc_area(coords):
    min_x, min_y, max_x, max_y = get_limits(coords)
    area = dict()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            area[(x, y)] = closest((x, y), coords)
    return area


# Remove all coordinates that got closest in infinite area
# basically, we need to find all outlying coordinates, then find all closest from that and remove them.
def remove_infinite(coords, area):
    infinite = set()
    min_x, min_y, max_x, max_y = list(get_limits(coords))
    limits_x = [min_x, max_x]
    limits_y = [min_y, max_y]
    for pos in area:
        if pos[0] in limits_x or pos[1] in limits_y:
            infinite.add(area[pos])

    return coords - infinite


def largest_area(coords):
    area = calc_area(coords)
    finite_coords = remove_infinite(coords, area)

    area_size = dict()
    for fc in finite_coords:
        area_size[fc] = len([pos for pos, c in area.items() if c == fc])

    return max(area_size.items(), key=operator.itemgetter(1))[1]


# calculate the largest region with less than max_distance to any coordinate
def calc_region(coords, max_distance):
    min_x, min_y, max_x, max_y = get_limits(coords)
    area = dict()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            d = calc_distance((x, y), coords)
            if d < max_distance:
                area[(x, y)] = d
    return len(area)


def calc_distance(pos, coords):
    return sum([mht(pos, c) for c in coords])


if __name__ == "__main__":
    with open('input/day06.txt') as f:
        params = f.read().splitlines()

    start = timer()
    coords = get_coord(params)
    print("result day 06 part 1: ", largest_area(coords), " in ", get_time(start))

    start = timer()
    print("result day 06 part 2: ", calc_region(coords, 10000), " in ", get_time(start))
