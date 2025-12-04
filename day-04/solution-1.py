from lib import read_data, can_remove

data = read_data()

print(
    sum(
        can_remove(data, row, col)
        for row in range(len(data))
        for col in range(len(data[0]))
    )
)
