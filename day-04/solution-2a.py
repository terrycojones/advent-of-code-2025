from itertools import takewhile, count
from lib import read_data, count_removable

data = read_data()

print(sum(takewhile(lambda x: x, (count_removable(data, True) for _ in count()))))
