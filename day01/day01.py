#!/usr/bin/env python3


# Convert params to int
def params_as_int(parameters):
    return list(map(int, parameters))


# Return the sum of the full array
def sum_array(parameters):
    return sum(params_as_int(parameters))


# Return the first value we'll reach twice.
def twice(parameters):
    values = params_as_int(parameters)
    pos = 0
    result = 0
    history = set()

    while True:
        pos = pos % len(values)
        result = values[pos] + result

        if result in history:
            return result
        else:
            pos = pos + 1
            history.add(result)


if __name__ == "__main__":
    with open('input-day01.txt') as f:
        params = f.readlines()
    print("result day 01 part 1: ", sum_array(params))
    print("result day 01 part 2: ", twice(params))
