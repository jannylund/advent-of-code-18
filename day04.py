#!/usr/bin/env python3
import operator
from datetime import datetime
import re
from timeit import default_timer as timer

from utils.time import get_time

c = re.compile("\[(.*)\] (.*)")


# generate a structure of {guard:{minute:sleep}}
def read_log(logs):
    logs = sorted(logs)
    result = dict()
    guard = None
    sleep = None
    for log in logs:
        time, msg = c.match(log).groups()
        time = datetime.strptime(time, '%Y-%m-%d %H:%M')

        # msg is either falls asleep, wakes up or begin shift.
        if msg == "falls asleep":
            sleep = time
        elif msg == "wakes up":
            if guard not in result:
                result[guard] = {}

            for i in range(sleep.minute, time.minute):
                if i not in result[guard]:
                    result[guard][i] = 1
                else:
                    result[guard][i] += 1

            sleep = None
        else:
            guard = int(re.findall('\\b\\d+\\b', msg)[0])

    return result


# Return id of the guard with max sleep.
def max_sleep(logs):
    dmax = dict()
    for g in logs:
        dmax[g] = sum(logs[g].values())

    return max(dmax.items(), key=operator.itemgetter(1))[0]


# Return the minute this guard slept the most.
def top_minute(logs, guard):
    return max(logs[guard].items(), key=operator.itemgetter(1))[0]


# Return id of the guard with max frequence.
def max_freq(logs):
    dmax = dict()
    for g in logs:
        dmax[g] = max(logs[g].values())

    return max(dmax.items(), key=operator.itemgetter(1))[0]


if __name__ == "__main__":
    with open('input/day04.txt') as f:
        params = f.read().splitlines()

    start = timer()
    logs = read_log(params)
    sleep_guard = max_sleep(logs)
    sleep_minute = top_minute(logs, sleep_guard)
    print("result day 04 part 1: guard: ", sleep_guard, " minute: ", sleep_minute, " answer: ",
          sleep_guard * sleep_minute, " in ", get_time(start))
    start = timer()
    freq_guard = max_freq(logs)
    freq_minute = top_minute(logs, freq_guard)
    print("result day 04 part 2: guard: ", freq_guard, " minute: ", freq_minute, " answer: ",
          freq_guard * freq_minute, " in ", get_time(start))
