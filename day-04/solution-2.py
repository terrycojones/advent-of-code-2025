from lib import read_data, removable

data = read_data()
total = 0

while count := removable(data, True):
    total += count

print(total)
