from utils import read_file

sample_data = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']


def process_input(data):
    return [[[int(i) for i in s.split('-')] for s in d.split(',')] for d in data]


def range_contains_other(r1, r2):
    (r1_lo, r1_hi), (r2_lo, r2_hi) = r1, r2
    if r1_lo >= r2_lo and r1_hi <= r2_hi:
        return True
    return False


def range_contains_other_p2(r1, r2):
    (r1_lo, r1_hi), (r2_lo, r2_hi) = r1, r2
    return bool(set(range(r1_lo, r1_hi + 1)) & set(range(r2_lo, r2_hi + 1)))


def num_overlapping_sections(ranges):
    c = 0
    for r in ranges:
        r1, r2 = r
        if range_contains_other(r1, r2) or range_contains_other(r2, r1):
            c += 1
    return c


def num_overlapping_sections_p2(ranges):
    c = 0
    for r in ranges:
        r1, r2 = r
        if range_contains_other_p2(r1, r2):
            c += 1
    return c


sections = process_input(read_file('04'))

p1 = num_overlapping_sections(sections)
p2 = num_overlapping_sections_p2(sections)
print(p1)
print(p2)
