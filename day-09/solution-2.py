from collections import defaultdict
from lib import read_data
import heapq

points = read_data()
red_points = set(points)
green_points = set()

for i in range(len(points)):
    p1 = points[i]
    p2 = points[(i + 1) % len(points)]
    p1_row, p1_col = p1
    p2_row, p2_col = p2

    if p1_row == p2_row:
        assert p1_col != p2_col
        for col in range(min(p1_col, p2_col) + 1, max(p1_col, p2_col)):
            green_points.add((p1_row, col))

    elif p1_col == p2_col:
        for row in range(min(p1_row, p2_row) + 1, max(p1_row, p2_row)):
            green_points.add((row, p1_col))

    else:
        raise ValueError("Inconceivable!")


assert not (red_points & green_points)

red_or_green = red_points | green_points

row_cols = defaultdict(set)
col_rows = defaultdict(set)

for row, col in red_or_green:
    row_cols[row].add(col)
    col_rows[col].add(row)

min_col_for_row = {}
max_col_for_row = {}
min_row_for_col = {}
max_row_for_col = {}

for row, cols in row_cols.items():
    min_col_for_row[row] = min(cols)
    max_col_for_row[row] = max(cols)

for col, rows in col_rows.items():
    min_row_for_col[col] = min(rows)
    max_row_for_col[col] = max(rows)


def red_green_rect(p1, p2):
    p1_row, p1_col = p1
    p2_row, p2_col = p2

    min_col = min(p1_col, p2_col)
    max_col = max(p1_col, p2_col)
    min_row = min(p1_row, p2_row)
    max_row = max(p1_row, p2_row)

    # Move vertically and check left / right.
    for row in range(min_row, max_row + 1):
        if min_col < min_col_for_row[row] or max_col > max_col_for_row[row]:
            return False

    # Move horizontally and check up / down.
    for col in range(min_col, max_col + 1):
        if min_row < min_row_for_col[col] or max_row > max_row_for_col[col]:
            return False

    return True


rectangles = []

for i in range(len(points)):
    pi = points[i]
    for j in range(i + 1, len(points)):
        pj = points[j]
        area = (abs(pi[0] - pj[0]) + 1) * (abs(pi[1] - pj[1]) + 1)
        rectangles.append((-area, pi, pj))

heapq.heapify(rectangles)

while True:
    area, pi, pj = heapq.heappop(rectangles)
    if red_green_rect(pi, pj):
        print(-area)
        break
