#!/usr/bin/env python3
from timeit import default_timer as timer
from utils.time import get_time


def list_checksum(boxes):
    r = []
    for box in boxes:
        r.append(checksum(box))
    return sum(list(zip(*r))[0]) * sum(list(zip(*r))[1])


def checksum(box):
    return has_count(box, 2), has_count(box, 3)


def has_count(box, count):
    chars = set(box)
    for c in chars:
        if box.count(c) == count:
            return 1
    return 0


def diff_one(ids):
    id_list = list(map(list, set(ids)))
    for box_a in id_list:
        for box_b in id_list:
            if box_a != box_b:
                mask = diff_mask(box_a, box_b)
                if sum(mask) == 1:
                    return unmask(box_a, mask)


# Create an (inverted) mask of the diff. 0 means match, 1 means drop
def diff_mask(box_a, box_b):
    return [0 if x == y else 1 for x, y in list(zip(box_a, box_b))]


# get the match according to mask.
def unmask(box, mask):
    return "".join(["" if m == 1 else v for m, v in list(zip(mask, box))])


if __name__ == "__main__":
    with open('input/day02.txt') as f:
        params = f.read().splitlines()

    start = timer()
    print("result day 02 part 1: ", list_checksum(params), " in ", get_time(start))
    start = timer()
    print("result day 02 part 2: ", diff_one(params), " in ", get_time(start))
