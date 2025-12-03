import sys
from lib import largest_from

total = 0

for line in sys.stdin:
    ints = list(map(int, line.strip()))
    first, start = largest_from(0, ints, len(ints) - 2)
    second, _ = largest_from(start + 1, ints, len(ints) - 1)
    total += 10 * first + second


print(total)
