"""
Advent of Code 2018. Day 8

Usage:
    day8.py part1
    day8.py part2
    day8.py test
"""
import re
import sys
from collections import defaultdict
import math
from docopt import docopt

PART1_SOLUTION = 2971
PART2_SOLUTION = 4254


def load_input_data():
    instructions = []
    with open("input") as f:
        for line in f:
            r = re.match(
                "([a-z]+) *(inc|dec) *(-?\d+) *if *([a-z]+) *(.*)",
                line
            )
            if not r:
                print(line)
                print("Error on input file. Exiting...")
                sys.exit()
            instructions.append(
                {
                    "register": r.group(1),
                    "operator": r.group(2),
                    "mod": int(r.group(3)),
                    "cond_reg": r.group(4),
                    "condition": r.group(5)
                }
            )
    return instructions


def part1():
    instructions = load_input_data()
    registers = defaultdict(int)
    for i in instructions:
        condition = f"registers['{i['cond_reg']}'] {i['condition']}"
        if eval(condition):
            op = 1 if i["operator"] == "inc" else -1
            registers[i["register"]] += (op * i["mod"])
    return registers[max(registers, key=registers.get)]


def part2():
    highest_value = -math.inf
    instructions = load_input_data()
    registers = defaultdict(int)
    for i in instructions:
        condition = f"registers['{i['cond_reg']}'] {i['condition']}"
        if eval(condition):
            op = 1 if i["operator"] == "inc" else -1
            registers[i["register"]] += (op * i["mod"])
            if registers[i["register"]] > highest_value:
                highest_value = registers[i["register"]]
    return highest_value


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
