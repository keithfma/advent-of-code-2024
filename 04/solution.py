import sys


def read(filename: str) -> tuple[str, ...]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    return tuple(l.strip() for l in lines)


def pad(data: tuple[str, ...]) -> tuple[str, ...]:
    padded = []
    ncols = len(data[0]) + 2
    padded.append('.' * ncols)
    for line in data:
        padded.append(f'.{line}.')
    padded.append('.' * ncols)
    return tuple(padded)


def count_xmas(board: str) -> int:

    # the (i, j) steps that you can take from an 'X' to find a valid 
    # 'XMAS' string
    steps = (
        ( 0,  1),  # right
        ( 0, -1),  # left
        ( 1,  0),  # down
        (-1,  0),  # up
        ( 1,  1),  # diag down right
        ( 1, -1),  # diag down left
        (-1,  1),  # diag up right
        (-1, -1),  # diag up left
    )

    num_rows = len(board)
    num_cols = len(board[0])

    # apply a 1-element pad to the board. This guarantees we will not get any 
    # index-out-of-range errors. 1 element is enough because the pad does not
    # contain any of the characters in 'XMAS', so the search always stops there.
    board = pad(board)

    matches = 0
    for i in range(1,num_rows+1):
        for j in range(1,num_cols+1):

            if board[i][j] != 'X':
                # starting element must be X, else skip
                continue

            # if the starting element is X, then we must check all directions for XMAS
            for step in steps:
                mi, mj = i + step[0], j + step[1]
                if board[mi][mj] != 'M':
                    continue
                ai, aj = mi + step[0], mj + step[1]
                if board[ai][aj] != 'A':
                    continue
                si, sj = ai + step[0], aj + step[1]
                if board[si][sj] != 'S':
                    continue
                # found one!
                matches += 1
    return matches
    

def count_x_mas(board: tuple[str, ...]) -> int:

    num_rows = len(board)
    num_cols = len(board[0])

    # apply a 1-element pad to the board. This guarantees we will not get any 
    # index-out-of-range errors.
    board = pad(board)

    matches = 0
    for i in range(1,num_rows+1):
        for j in range(1,num_cols+1):

            if board[i][j] != 'A':
                # middle element must be A, else skip
                continue

            # if the middle element is A, then we must check both diagonals for M and S
            diag = {board[i-1][j-1], board[i+1][j+1]}
            if diag != {'M', 'S'}:
                continue

            diag = {board[i+1][j-1], board[i-1][j+1]}
            if diag != {'M', 'S'}:
                continue
            
            # found one!
            matches += 1
    return matches


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 4')

    input_file = sys.argv[1]

    ws = read(input_file)
    print(f'Num XMAS found: {count_xmas(ws)}')
    print(f'Num X-MAS found: {count_x_mas(ws)}')

