"""
Advent of Code 2018. Day 3

Usage:
    day3.py part1
    day3.py part2
    day3.py test
"""
from docopt import docopt
import numpy as np
from collections import namedtuple
from itertools import product

TARGET = 312051
PART1_SOLUTION = 430
PART2_SOLUTION = 312453


def get_movements():
    MOVEMENTS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    while True:
        for m in MOVEMENTS:
            yield m


def part1():
    current_pos = np.array([0, 0])
    movements_generator = get_movements()
    current_index, i = 1, 1
    while True:
        for _ in range(2):
            current_movement = next(movements_generator)
            for j in range(i):
                current_pos += current_movement
                current_index += 1
                if current_index == TARGET:
                    return sum(abs(current_pos))
        i += 1


def summary_value(memory, current_pos):
    adjacents = [(current_pos + x).tolist()
                 for x in product([0, 1, -1], repeat=2)]
    adjacent_values = [m.value for m in memory if [m.i, m.j] in adjacents]
    return sum(adjacent_values)


def part2():
    memory = []
    MemoryItem = namedtuple("MemoryItem", ["i", "j", "value"])
    current_pos = np.array([0, 0])
    memory.append(MemoryItem(*current_pos, 1))
    movements_generator = get_movements()
    i = 1
    while True:
        for _ in range(2):
            current_movement = next(movements_generator)
            for j in range(i):
                current_pos += current_movement
                memory_item = MemoryItem(
                        *current_pos,
                        summary_value(memory, current_pos)
                    )
                memory.append(memory_item)
                if memory_item.value > TARGET:
                    return memory_item.value
        i += 1


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
