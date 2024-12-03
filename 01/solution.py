"""Advent of Code 2024 - Day 1
"""
from collections import Counter


def read_input(filename: str) -> tuple[list[int], list[int]]:
    aa = []
    bb = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            a, b = line.split()
            aa.append(int(a))
            bb.append(int(b))
    return aa, bb


def total_distance(aa: list[int], bb: list[int]) -> None:
    dist = 0
    for a, b in zip(sorted(aa), sorted(bb)):
        dist += abs(a - b)
    print(f'Total distance: {dist}')


def similarity_score(aa: list[int], bb: list[int]) -> None:
    counts = Counter(bb)
    score = 0
    for num in aa:
        try:
            score += num * counts[num]
        except KeyError:
            pass
    print(f'Similarity score: {score}')
    


# -----

EXAMPLE = 'ex1.txt'
REAL = 'input.txt'

# selected = EXAMPLE
selected = REAL

data = read_input(selected)
total_distance(*data)
similarity_score(*data)
    

