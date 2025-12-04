from lib import read_data, symbol, count_adjacent_rolls

data = read_data()
total = 0

while True:
    to_remove = [
        (row, col)
        for row in range(len(data))
        for col in range(len(data[0]))
        if symbol(data, row, col) == "@" and count_adjacent_rolls(data, row, col) < 4
    ]

    if to_remove:
        total += len(to_remove)
        for row, col in to_remove:
            data[row][col] = "x"
    else:
        break

print(total)
