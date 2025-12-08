import sys
import heapq
import math


def read_data():
    return [tuple(map(int, line.strip().split(","))) for line in sys.stdin]


def dist(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))


def make_heap(points):
    heap = []
    n = len(points)
    for i in range(n):
        pi = points[i]
        for j in range(i + 1, n):
            pj = points[j]
            heap.append((dist(pi, pj), pi, pj))

    heapq.heapify(heap)

    return heap


def set_of(point, circuits):
    for s in circuits:
        if point in s:
            return s

    raise ValueError("Inconceivable!")
