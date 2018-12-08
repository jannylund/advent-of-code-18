#!/usr/bin/env python3
from timeit import default_timer as timer

from utils.time import get_time
import re

c = re.compile("Step (.) must be finished before step (.) can begin.")


def read_inst(logs):
    guide = dict()
    all = []
    for l in logs:
        a, b = c.match(l).groups()
        all += a
        if b in guide:
            guide[b] += [a]
        else:
            guide[b] = [a]

    # now we may still have some things that has no dependencies. add those as well.
    for b in set(all):
        if b not in guide:
            guide[b] = []

    return guide


# Try to find the proper order, first the ones without dependency.
def timed_order_inst(instructions, workers=1, offset=0):
    done = []
    time = - 1
    w = dict()

    while len(done) < len(instructions):
        time += 1

        for c, v in w.items():
            if v == 1:
                done += c
            else:
                w[c] = v - 1

        # remove the ready things from workers.
        for c in done:
            if c in w:
                del w[c]

        o = []
        for k, v in instructions.items():
            if k not in set(w.keys()) | set(done):  # don't put the same work again.
                if len(set(v) - set(done)) == 0:
                    o += k
        o.sort()

        # Add work if we have free workers.
        while len(w) < workers and len(o) > 0:
            job = o[0]
            w[job] = offset + get_char_time(job)
            o.remove(job)

        print("time:", time, " w: ", w, " done: ", "".join(done))
    return time, "".join(done)


def get_char_time(c):
    return ord(c) - 64


if __name__ == "__main__":
    with open('input/day07.txt') as f:
        params = f.read().splitlines()

    start = timer()
    instructions = read_inst(params)
    print("result day 07 part 1: ", timed_order_inst(instructions), " in ", get_time(start))

    start = timer()
    print("result day 07 part 2: ", timed_order_inst(instructions, 5, 60), " in ", get_time(start))
