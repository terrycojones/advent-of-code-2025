import sys


def move(current, specification, size):
    direction = specification[0]
    assert direction in "LR"
    sign = 1 if direction == "R" else -1
    distance = int(specification[1:])
    return (current + distance * sign) % size


size = 100
current = 50
zeroes = 0

for line in sys.stdin:
    current = move(current, line, size)
    if current == 0:
        zeroes += 1

print(zeroes)
