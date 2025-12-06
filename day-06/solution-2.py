import sys
from operator import mul, add
from functools import reduce


def read_data():
    rows = []
    max_len = -1
    for line in sys.stdin:
        line = line.rstrip()
        if len(line) > max_len:
            max_len = len(line)
        if line.find("*") > -1 or line.find("+") > -1:
            ops = [mul if op == "*" else add for op in line.strip().split()]
        else:
            rows.append(line)

    for i, line in enumerate(rows):
        if len(line) < max_len:
            rows[i] += " " * (max_len - len(line))

    return rows, ops


data, ops = read_data()
n_rows = len(data)
n_cols = len(data[0])
col = total = 0

for op in ops:
    gap_col = col

    while any(data[row][gap_col] != " " for row in range(n_rows)):
        gap_col += 1
        if gap_col == n_cols:
            break

    args = []
    for col in range(col, gap_col):
        digits = []
        for row in range(n_rows):
            char = data[row][col]
            if char != " ":
                digits.append(char)
        args.append(int("".join(digits)))

    total += reduce(op, args)
    col = gap_col + 1

print(total)
