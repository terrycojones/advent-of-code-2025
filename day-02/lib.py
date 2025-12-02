import sys

def read_input():
    for pair in sys.stdin.read().split(","):
        yield map(int, pair.split("-"))
