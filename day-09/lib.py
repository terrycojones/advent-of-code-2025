import sys


def read_data():
    result = []
    for line in sys.stdin:
        row, col = tuple(map(int, line.strip().split(",")))
        result.append((row - 1, col - 1))

    return result
