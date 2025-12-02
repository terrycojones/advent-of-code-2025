import sys

from lib import read_input


def invalid(n):
    s = str(n)
    l = len(s)
    if l % 2 == 0:
        half = l >> 1
        if s[:half] == s[half:]:
            return n
    return 0


total = 0
for a, b in read_input():
    assert b >= a
    for n in range(a, b+1):
        total += invalid(n)

print(total)
