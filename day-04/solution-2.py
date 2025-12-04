from lib import read_data, removable

data = read_data()
total = 0

while True:
    if to_remove := removable(data):
        total += len(to_remove)
        for row, col in to_remove:
            data[row][col] = "x"
    else:
        break

print(total)
