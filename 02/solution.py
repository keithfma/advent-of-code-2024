import sys
from math import copysign 



# TODO: try as a generator, just to flex
def read_input(filename: str) -> list[tuple[int, ...]]:
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(
                tuple(int(x) for x in line.split())
            )
    return data
    

def is_safe(report: tuple[int, ...]) -> bool:

    # note: if difference is 0, then the sign doesn't matter anyway
    expected_sign = report[1] - report[0] > 0  

    for cur, nxt in zip(report, report[1:]):
        # unsafe if step size is not 1, 2, 3
        dif = nxt - cur
        if dif == 0 or abs(dif) > 3:
            return False
        # unsafe if not all increasing or decreasing
        sign = dif > 0 
        if sign != expected_sign:
            return False

    # safe!
    return True


def is_safe_damp(report: tuple[int, ...]) -> bool:

    for idx in range(len(report)):
        damped = report[0:idx] + report[idx+1:]
        if is_safe(damped):
            # safe if any damped variant is safe
            return True
    # all variants unsafe!
    return False


if __name__ == '__main__':

    print('Advent of Code 2024 - Day 2')
    input_file = sys.argv[1]
    print(f'Input file: {input_file}')
    reports = read_input(input_file)

    num_safe = sum(is_safe(r) for r in reports)
    print(f'Number safe reports: {num_safe}')
    
    num_safe_damp = sum(is_safe_damp(r) for r in reports)
    print(f'Number safe reports with dampener: {num_safe_damp}')

