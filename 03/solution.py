import re
import sys
from math import prod


def read_input(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()


def all_mul_total(command: str) -> int:
    pairs = re.findall(r'mul\((\d{1,3},\d{1,3})\)', command)
    total = 0
    for pair in pairs:
        total += prod(int(x) for x in pair.split(','))
    return total


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 3')
    input_file = sys.argv[1]
    cmd = read_input(input_file)
    print(f'Sum of valid products: {all_mul_total(cmd)}')

    
    
