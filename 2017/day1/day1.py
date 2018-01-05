import sys


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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        assert part1() == 1253
        assert part2() == 1278
    else:
        print(part1())
        print(part2())
