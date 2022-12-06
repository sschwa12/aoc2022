from collections import deque

from utils import read_file

data = read_file('06')[0]

sample_data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'


def num_chars_to_process(signal: str, num_recent=4) -> int:
    seen = deque(signal[0:num_recent], maxlen=num_recent)
    for i in range(4, len(signal)):
        if len(set(seen)) == num_recent:
            return i
        c = signal[i]
        seen.append(c)


p1 = num_chars_to_process(data)
p2 = num_chars_to_process(data, 14)
print(p1)
print(p2)
