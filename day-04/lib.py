import sys


def read_data():
    return [list(line.strip()) for line in sys.stdin]


def symbol(data, row, col):
    cols = len(data[0])
    if row < 0 or row > len(data) - 1 or col < 0 or col > cols - 1:
        return "x"
    else:
        return data[row][col]        


def count_adjacent_rolls(data, row, col):
    return sum(
        symbol(data, row + rowinc, col + colinc) == "@"
        for rowinc in range(-1, 2)
        for colinc in range(-1, 2)
        if rowinc or colinc
    )


def can_remove(data, row, col):
    return symbol(data, row, col) == "@" and count_adjacent_rolls(data, row, col) < 4
