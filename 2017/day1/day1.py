"""
Advent of Code 2018. Day 1

Usage:
    day1.py part1
    day1.py part2
    day1.py test
"""
from docopt import docopt

PART1_SOLUTION = 1253
PART2_SOLUTION = 1278


def load_input_data():
    with open("input") as f:
        return f.readline().strip()


def part1():
    input = load_input_data()
    matches = []
    input_size = len(input)
    for i in range(input_size):
        next = (i + 1) % input_size
        if input[i] == input[next]:
            matches.append(int(input[i]))
    return sum(matches)


def part2():
    input = load_input_data()
    matches = []
    input_size = len(input)
    step = input_size // 2
    for i in range(input_size):
        next = (i + step) % input_size
        if input[i] == input[next]:
            matches.append(int(input[i]))
    return sum(matches)


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
