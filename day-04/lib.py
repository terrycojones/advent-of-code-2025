import sys
from itertools import product


def read_data():
    return [list(line.strip()) for line in sys.stdin]


def symbol(data, row, col):
    return data[row][col] if 0 <= row < len(data) and 0 <= col < len(data[0]) else "x"


def count_adjacent_rolls(data, row, col):
    return sum(
        symbol(data, row + row_inc, col + col_inc) == "@"
        for row_inc, col_inc in product(range(-1, 2), repeat=2)
        if row_inc or col_inc
    )


def can_remove(data, row, col):
    return symbol(data, row, col) == "@" and count_adjacent_rolls(data, row, col) < 4


def removable(data, clear=False):
    count = 0
    for row, col in product(range(len(data)), range(len(data[0]))):
        if can_remove(data, row, col):
            if clear:
                data[row][col] = "x"
            count += 1
    return count
