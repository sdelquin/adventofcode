"""
Advent of Code 2018. Day 9

Usage:
    day9.py part1
    day9.py part2
    day9.py test
"""
from docopt import docopt


PART1_SOLUTION = 16021
PART2_SOLUTION = 7685


def load_input_data():
    with open("input") as f:
        return f.readline().strip()


def part1():
    stream = load_input_data()
    num_groups, depth, i, garbage = 0, 1, 0, False
    while i < len(stream):
        if stream[i] == "{" and not garbage:
            depth += 1
        elif stream[i] == "}" and not garbage:
            depth -= 1
            num_groups += depth
        elif stream[i] == "!":
            i += 1
        elif stream[i] == "<":
            garbage = True
        elif stream[i] == ">":
            garbage = False
        i += 1
    return num_groups


def part2():
    stream = load_input_data()
    i, garbage, garbage_size = 0, False, 0
    while i < len(stream):
        if stream[i] == "!":
            i += 1
        elif stream[i] == "<":
            if garbage:
                garbage_size += 1
            else:
                garbage = True
        elif stream[i] == ">":
            garbage = False
        elif garbage:
            garbage_size += 1
        i += 1
    return garbage_size


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
