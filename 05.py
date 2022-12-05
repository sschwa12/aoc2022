import re
from typing import List

from utils import read_file

d = read_file('05')


# def get_stacks():
#     return [
#         ['Z', 'N'],
#         ['M', 'C', 'D'],
#         ['P'],
#     ]

def get_stacks():
    return [
        ['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'],
        ['D', 'Q', 'L'],
        ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
        ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],
        ['V', 'G', 'L', 'F', 'Z', 'S'],
        ['D', 'G', 'N', 'P'],
        ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],
        ['C', 'P', 'D', 'M', 'S'],
        ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']
    ]


def get_moves(raw):
    moves = []
    for m in [x for x in raw if x.startswith('m')]:
        moves.append([int(s) for s in re.findall(r'\b\d+\b', m)])
    return moves


def rearrange(instructions: List[str], reverse_stacks=False):
    stacks = get_stacks()
    moves = get_moves(instructions)
    for i, move in enumerate(moves):
        num_moves, move_from, move_to = move
        from_stack = move_from - 1
        to_stack = move_to - 1
        s = []
        while num_moves:
            popped = stacks[from_stack].pop()
            s.append(popped)
            num_moves -= 1
        if reverse_stacks:
            stacks[to_stack].extend(reversed(s))
        else:
            stacks[to_stack].extend(s)
    return ''.join([s[-1] for s in stacks])


p1 = rearrange(d)
p2 = rearrange(d, reverse_stacks=True)
print(p1)
print(p2)
