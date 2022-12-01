import heapq
from typing import List

from utils import read_file

data = read_file('01')

sample = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']


def max_calories(calorie_count: List[str], n_max: int = 1) -> int:
    joined = ' '.join(calorie_count)
    sums = []
    for s in joined.split('  '):
        cur_sum = 0
        for n in s.split(' '):
            cur_sum += int(n)
        heapq.heappush(sums, cur_sum)

    return sum(heapq.nlargest(n_max, sums))


p1 = max_calories(data)
p2 = max_calories(data, 3)

print(p1)
print(p2)
