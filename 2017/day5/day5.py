"""
Advent of Code 2018. Day 5

Usage:
    day5.py part1
    day5.py part2
    day5.py test
"""
from docopt import docopt

PART1_SOLUTION = 394829
PART2_SOLUTION = 31150702


def load_input_data():
    with open("input") as f:
        return [int(line.strip()) for line in f]


def part1():
    maze = load_input_data()
    maze_size = len(maze)
    instruction, steps = 0, 0
    while instruction < maze_size:
        offset = maze[instruction]
        maze[instruction] += 1
        instruction += offset
        steps += 1
    return steps


def part2():
    maze = load_input_data()
    maze_size = len(maze)
    instruction, steps = 0, 0
    while instruction < maze_size:
        offset = maze[instruction]
        if offset >= 3:
            maze[instruction] -= 1
        else:
            maze[instruction] += 1
        instruction += offset
        steps += 1
    return steps


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
