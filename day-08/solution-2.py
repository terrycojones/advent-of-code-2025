import heapq
from lib import read_data, make_heap, set_of

data = read_data()
heap = make_heap(data)
circuits = {frozenset((point,)) for point in data}


while True:
    _, pi, pj = heapq.heappop(heap)
    pis = set_of(pi, circuits)
    pjs = set_of(pj, circuits)

    if pis is not pjs:
        circuits.add(frozenset(set(pis) | set(pjs)))
        circuits.remove(pis)
        circuits.remove(pjs)

        if len(circuits) == 1:
            print(pi[0] * pj[0])
            break
