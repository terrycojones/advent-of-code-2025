from collections import defaultdict
from lib import read_data

data = read_data()
pending = ["svr"]
counts = defaultdict(lambda: [0, 0, 0])
counts["svr"] = [1, 0, 0]

while pending:
    device = pending.pop(0)
    for next_ in data[device]:
        if next_ != "out" and next_ not in pending:
            pending.append(next_)
        inc = next_ in {"dac", "fft"}
        for i in (0, 1) if inc else (0, 1, 2):
            counts[next_][i + inc] += counts[device][i]

print(counts["out"][2])
