from collections import defaultdict
from lib import read_data

data = read_data()
pending = ["you"]
counts = defaultdict(int)
counts["you"] = 1

while pending:
    device = pending.pop(0)
    for next_ in data[device]:
        if next_ != "out" and next_ not in pending:
            pending.append(next_)
        counts[next_] += counts[device]

print(counts["out"])
