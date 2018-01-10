"""
Advent of Code 2018. Day 7

Usage:
    day7.py part1
    day7.py part2
    day7.py test
"""
import re
from anytree import Node
from collections import defaultdict
from docopt import docopt

PART1_SOLUTION = "fbgguv"
PART2_SOLUTION = 1864


def load_input_data():
    tower = {}
    with open("input") as f:
        for line in f:
            sections = re.split("\s*->\s*", line)
            father_name, weight = re.match(
                "([a-z]+)\s+\((\d+)\)",
                sections[0]
            ).groups()
            if father_name not in tower:
                tower[father_name] = Node(father_name)
            tower[father_name].weight = int(weight)

            if len(sections) > 1:
                for child_name in re.split(",\s*", sections[1].strip()):
                    if child_name not in tower:
                        tower[child_name] = Node(child_name)
                    tower[child_name].parent = tower[father_name]
    return list(tower.items())[0][1].root


def part1():
    tower = load_input_data()
    return tower.name


def calculate_partial_weights(node):
    aux = 0
    for child in node.children:
        aux += calculate_partial_weights(child)
    node.partial_weight = node.weight + aux
    return node.partial_weight


def find_different(nodes):
    d = defaultdict(list)
    for node in nodes:
        d[node.partial_weight].append(node)
    if len(d) > 1:
        group1, group2 = d.items()
        partial_weight1, partial_weight2 = group1[0], group2[0]
        grouped_nodes1, grouped_nodes2 = group1[1], group2[1]
        if len(grouped_nodes1) == 1:
            target_node = grouped_nodes1[0]
            diff = partial_weight2 - partial_weight1
        else:
            target_node = grouped_nodes2[0]
            diff = partial_weight1 - partial_weight2
        target_node.balanced_weight = target_node.weight + diff
        return target_node
    return None


def follow_unbalanced_path(node):
    unbalanced_node = find_different(node.children)
    if unbalanced_node:
        return follow_unbalanced_path(unbalanced_node)
    else:
        return node


def part2():
    tower = load_input_data()
    calculate_partial_weights(tower)
    unbalanced_node = follow_unbalanced_path(tower)
    return unbalanced_node.balanced_weight


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
