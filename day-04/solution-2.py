from lib import read_data, can_remove

data = read_data()
total = 0

while True:
    if to_remove := [
        (row, col)
        for row in range(len(data))
        for col in range(len(data[0]))
        if can_remove(data, row, col)
    ]:
        total += len(to_remove)
        for row, col in to_remove:
            data[row][col] = "x"
    else:
        break

print(total)
