import string
from typing import List

from utils import read_file

data = read_file('03')
sample_data = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw'
]
priorities = {v: i + 1 for i, v in enumerate(string.ascii_letters)}


def get_priority_sum(rucksacks: List[str]):
    total = 0
    for r in rucksacks:
        mid = len(r) // 2
        compartment_1, compartment_2 = r[:mid], r[mid:len(r)]
        common_char = list(set(compartment_1) & set(compartment_2))
        total += priorities[common_char[0]]
    return total


def get_priority_sum_2(rucksacks: List[str]):
    total = 0
    rucksacks.append('blah')  # sentinel
    for i in range(0, len(rucksacks), 3):
        if i < len(rucksacks) - 3:
            r1, r2, r3 = rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]
            common_char = list(set(r1) & set(r2) & set(r3))
            total += priorities[common_char[0]]
    return total


p1 = get_priority_sum(data)
p2 = get_priority_sum_2(data)

print(p1)
print(p2)
