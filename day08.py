#!/usr/bin/env python3
from timeit import default_timer as timer

from utils.time import get_time


class Node:
    def __init__(self, license):
        self.qty_child = license[0]
        self.qty_met = license[1]
        del license[:2]
        self.child_nodes = []

        for i in range(self.qty_child):
            self.child_nodes += [Node(license)]

        self.metadata = license[:self.qty_met]
        del license[:self.qty_met]

    def get_metadata(self):
        met = self.metadata[:] # Avoid mutating the original list.
        for c in self.child_nodes:
            met += c.get_metadata()
        return met

    def get_value(self):
        if self.qty_child < 1:
            return sum(self.metadata)
        else:
            val = 0
            for m in self.metadata: # m is the index of child + 1.
                if self.qty_child > m - 1:
                    val += self.child_nodes[m - 1].get_value()
            return val


def get_nodes(license):
    return Node(list(map(int, license.split(" "))))


if __name__ == "__main__":
    with open('input/day08.txt') as f:
        params = f.read().splitlines()[0]

    start = timer()
    nodes = get_nodes(params)
    print("result day 08 part 1: ", sum(nodes.get_metadata()), " in ", get_time(start))

    start = timer()
    print("result day 08 part 2: ", nodes.get_value(), " in ", get_time(start))
