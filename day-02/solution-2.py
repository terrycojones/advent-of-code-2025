from itertools import batched
from lib import read_input


def invalid(n):
    s = str(n)
    for plen in range(1, (len(s) >> 1) + 1):
        batches = ["".join(b) for b in batched(s, plen)]
        if len(set(batches)) == 1:
            return n
    return 0


total = 0

for a, b in read_input():
    for n in range(a, b+1):
        total += invalid(n)

print(total)
