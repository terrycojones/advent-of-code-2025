from lib import read_data, symbol, count_adjacent_rolls

data = read_data()
total = 0

for row in range(len(data)):
    for col in range(len(data[0])):
        total += (
            symbol(data, row, col) == "@" and count_adjacent_rolls(data, row, col) < 4
        )

print(total)
