from typing import List, Tuple

from utils import read_file

data = read_file('02')

sample_data = ['A Y', 'B X', 'C Z']

score_map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'Z': 3,
    'Y': 2,
    'X': 1,
}

eq_map = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

gt_map = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

lt_map = {
    'B': 'Z',
    'A': 'Y',
    'C': 'X'
}


class RPS():
    def __init__(self, choice: str):
        self.choice = choice

    def __gt__(self, other):
        if gt_map[self.choice] == other.choice:
            return True
        return False

    def __eq__(self, other):
        if eq_map[self.choice] == other.choice:
            return True
        return False

    def __str__(self):
        return f'{self.choice}'

    __repr__ = __str__

    def get_value(self):
        return score_map[self.choice]


def get_total_rps_score(rounds):
    total = 0
    for r in rounds:
        # p1, p2 = RPS(r[0]), RPS(r[2]) // part 1
        p1 = RPS(r[0])
        p2 = ''
        if r[2] == 'Y':
            p2 = RPS(eq_map[r[0]])
        elif r[2] == 'Z':
            p2 = RPS(lt_map[r[0]])
        else:
            p2 = RPS(gt_map[r[0]])

        p1_score, p2_score = p1.get_value(), p2.get_value()
        if p1 > p2:
            total += p2_score
        elif p1 == p2:
            total += 3 + p2_score
        else:
            total += 6 + p2_score

    return total


part2 = get_total_rps_score(data)
print(part2)
