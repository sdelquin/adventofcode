"""
Advent of Code 2018. Day 6

Usage:
    day6.py part1
    day6.py part2
    day6.py test
"""
import numpy as np
from docopt import docopt

PART1_SOLUTION = 4074
PART2_SOLUTION = 2793


def load_input_data():
    with open("input") as f:
        return [int(data) for data in f.readline().strip().split("\t")]


def part1():
    memory_banks = np.array(load_input_data())
    memory_banks_history = []
    memory_banks_history.append(memory_banks.tolist())
    redistribution_cycles = 0
    while True:
        selected_bank = np.argmax(memory_banks)
        blocks = memory_banks[selected_bank]
        memory_banks[selected_bank] = 0
        for i in range(selected_bank, selected_bank + blocks):
            memory_banks[(i + 1) % memory_banks.size] += 1
        redistribution_cycles += 1
        if memory_banks.tolist() in memory_banks_history:
            break
        memory_banks_history.append(memory_banks.tolist())
    return redistribution_cycles


def find_memory_banks(memory_banks, memory_banks_history):
    for i, m in enumerate(memory_banks_history):
        if m == memory_banks:
            return i


def part2():
    memory_banks = np.array(load_input_data())
    memory_banks_history = []
    memory_banks_history.append(memory_banks.tolist())
    redistribution_cycles = 0
    while True:
        selected_bank = np.argmax(memory_banks)
        blocks = memory_banks[selected_bank]
        memory_banks[selected_bank] = 0
        for i in range(selected_bank, selected_bank + blocks):
            memory_banks[(i + 1) % memory_banks.size] += 1
        k = find_memory_banks(memory_banks.tolist(), memory_banks_history)
        if k is not None:
            break
        memory_banks_history.append(memory_banks.tolist())
        redistribution_cycles += 1
    return redistribution_cycles - k + 1


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
