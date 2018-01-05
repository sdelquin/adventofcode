import sys
import re
import numpy as np


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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        assert part1() == 44670
        assert part2() == 285
    else:
        print(part1())
        print(part2())
