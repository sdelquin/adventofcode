import sys

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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        assert part1() == PART1_SOLUTION
        assert part2() == PART2_SOLUTION
    else:
        print(part1())
        print(part2())
