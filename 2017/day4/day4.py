import sys

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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        assert part1() == PART1_SOLUTION
        assert part2() == PART2_SOLUTION
    else:
        print(part1())
        print(part2())
