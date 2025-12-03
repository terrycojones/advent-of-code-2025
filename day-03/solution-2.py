import sys
from lib import largest_from

total = 0
n_digits = 12

for line in sys.stdin:
    ints = list(map(int, line.strip()))
    digits = []
    start = -1

    for _ in range(n_digits):
        biggest, start = largest_from(start + 1, ints, len(ints) - (n_digits - len(digits)))
        digits.append(biggest)

    total += int("".join(map(str, digits)))


print(total)
