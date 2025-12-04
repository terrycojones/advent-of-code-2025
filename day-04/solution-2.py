from lib import read_data, count_removable

data = read_data()
total = 0

while count := count_removable(data, True):
    total += count

print(total)
