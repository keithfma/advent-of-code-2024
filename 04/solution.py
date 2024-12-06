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


class Coord:
    """A location on in the word search board, as a row, column (i, j) index
    Basically, just a tuple with elementwise addition enabled.
    """

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def __add__(self, other):
        if not isinstance(other, Coord):
            raise NotImplementedError
        return self.__class__(self.i + other.i, self.j + other.j)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(i={self.i}, j={self.j})'


# a the steps that you can take from an 'X' to find a valid 
# 'XMAS' string
STEPS = (
    Coord( 0,  1),  # right
    Coord( 0, -1),  # left
    Coord( 1,  0),  # down
    Coord(-1,  0),  # up
    Coord( 1,  1),  # diag down right
    Coord( 1, -1),  # diag down left
    Coord(-1,  1),  # diag up right
    Coord(-1, -1),  # diag up left
)


def count_xmas(board: str) -> int:

    num_rows = len(board)
    num_cols = len(board[0])

    # apply a 1-element pad to the board. This guarantees we will not get any 
    # index-out-of-range errors. 1 element is enough because the pad does not
    # contain any of the characters in 'XMAS', so the search always stops there.
    board = pad(board)

    matches = 0
    for i in range(1,num_rows+1):
        for j in range(1,num_cols+1):

            x = Coord(i, j)
            if board[x.i][x.j] != 'X':
                # starting element must be X, else skip
                continue

            # if the starting element is X, then we must check all directions for XMAS
            for step in STEPS:
                m = x + step
                if board[m.i][m.j] != 'M':
                    continue
                a = m + step
                if board[a.i][a.j] != 'A':
                    continue
                s = a + step
                if board[s.i][s.j] != 'S':
                    continue
                # found one!
                matches += 1
    return matches

    


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 4')

    input_file = sys.argv[1]

    ws = read(input_file)
    print(f'Num XMAS found: {count_xmas(ws)}')



                
                    





   
