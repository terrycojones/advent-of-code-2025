import sys
import numpy as np
from operator import mul, add
from functools import reduce


def read_data():
    rows = []
    for line in sys.stdin:
        fields = line.strip().split()
        if fields[0] in "*+":
            ops = [mul if op == "*" else add for op in fields]
        else:
            rows.append(list(map(int, fields)))

    return np.array(rows).T, ops


data, ops = read_data()

print(sum(reduce(op, args) for op, args in zip(ops, data)))
