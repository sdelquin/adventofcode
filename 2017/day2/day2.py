"""
Advent of Code 2018. Day 2

Usage:
    day2.py part1
    day2.py part2
    day2.py test
"""
from docopt import docopt
import re
import numpy as np

PART1_SOLUTION = 44670
PART2_SOLUTION = 285


def load_input_data():
    spreadsheet = []
    with open("input") as f:
        for line in f:
            spreadsheet.append(
                [int(x) for x in re.split(r"\s+", line.strip())]
            )
    return spreadsheet


def part1():
    spreadsheet = np.array(load_input_data())
    max_values = np.amax(spreadsheet, axis=1)
    min_values = np.amin(spreadsheet, axis=1)
    return sum(max_values - min_values)


def part2():
    spreadsheet = np.array(load_input_data())
    evenly_divisibles = []
    for row in spreadsheet:
        for value in row:
            r = row / value
            match = [v for v in r if round(v) == v and v > 1]
            if match:
                evenly_divisibles.append(int(match[0]))
                break

    return sum(evenly_divisibles)


def test():
    assert part1() == PART1_SOLUTION
    assert part2() == PART2_SOLUTION


if __name__ == "__main__":
    arguments = docopt(__doc__)
    if arguments["part1"]:
        print(part1())
    elif arguments["part2"]:
        print(part2())
    elif arguments["test"]:
        test()
