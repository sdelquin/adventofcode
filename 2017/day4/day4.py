"""
Advent of Code 2018. Day 4

Usage:
    day4.py part1
    day4.py part2
    day4.py test
"""
from docopt import docopt

PART1_SOLUTION = 337
PART2_SOLUTION = 231


def load_input_data():
    with open("input") as f:
        return [line.strip() for line in f]


def part1():
    passphrases = load_input_data()
    valid_passphrases = 0
    for passphrase in passphrases:
        words = passphrase.split()
        if len(words) == len(set(words)):
            valid_passphrases += 1
    return valid_passphrases


def any_is_anagram(target_word, words):
    sorted_target_word = sorted(target_word)
    for word in words:
        if sorted(word) == sorted_target_word:
            return True
    return False


def part2():
    passphrases = load_input_data()
    valid_passphrases = 0
    for passphrase in passphrases:
        words = passphrase.split()
        for i, word in enumerate(words):
            current_words = words[:]
            current_words.pop(i)
            if any_is_anagram(word, current_words):
                break
        else:
            valid_passphrases += 1
    return valid_passphrases


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
