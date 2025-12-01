import sys


def move_clicks(current, specification, size):
    clicks = 0
    direction = specification[0]
    assert direction in "LR"
    sign = 1 if direction == "R" else -1
    distance = int(specification[1:])
    revolutions, remainder = divmod(distance, size)
    clicks += revolutions

    for _ in range(remainder):
        current = (current + sign) % size
        if current == 0:
            clicks += 1

    return current, clicks


size = 100
current = 50
total_clicks = 0

for line in sys.stdin:
    current, clicks = move_clicks(current, line, size)
    total_clicks += clicks

print(total_clicks)
