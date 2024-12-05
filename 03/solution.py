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


def enabled_mul_total(command: str) -> int:
    # can be do(), don't(), or mul(#, #)
    valid = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)", command)

    total = 0
    enabled = True  # start with mul() commands enabled
    for v in valid:
        if v == "don't()":
            enabled = False
        elif v == "do()":
            enabled = True
        elif enabled:
            total += prod(int(x) for x in re.findall(r'\d{1,3}', v))

    return total

if __name__ == '__main__':
    print('Advent of Code 2024 - Day 3')
    input_file = sys.argv[1]
    cmd = read_input(input_file)
    print(f'Sum of all mul() commands: {all_mul_total(cmd)}')
    print(f'Sum of enabled mul() commands: {enabled_mul_total(cmd)}')



    
    
