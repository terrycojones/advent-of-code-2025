from collections import defaultdict
from lib import read_data

width, beam, row_splitters = read_data()
state_count = defaultdict(int)
state_count[beam] = 1

for splitters in row_splitters:
    if splitters:
        next_state_counts = defaultdict(int)
        for state, count in state_count.items():
            if state in splitters:
                if state - 1 >= 0:
                    next_state_counts[state - 1] += count
                if state + 1 < width:
                    next_state_counts[state + 1] += count
            else:
                next_state_counts[state] += count
        state_count = next_state_counts


print(sum(state_count.values()))
