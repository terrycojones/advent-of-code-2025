import sys
import heapq
from lib import read_data, make_heap, set_of

joins = int(sys.argv[1])
data = read_data()
heap = make_heap(data)
circuits = {frozenset((point,)) for point in data}

for _ in range(joins):
    _, pi, pj = heapq.heappop(heap)
    pis = set_of(pi, circuits)
    pjs = set_of(pj, circuits)

    if pis is not pjs:
        circuits.add(frozenset(set(pis) | set(pjs)))
        circuits.remove(pis)
        circuits.remove(pjs)

lens = sorted(len(c) for c in circuits)

print(lens[-1] * lens[-2] * lens[-3])
