import sys


def read_data():
    splitters = []
    first = True
    for line in sys.stdin:
        line = line.strip()
        if first:
            beam = line.find("S")
            width = len(line)
            first = False
        else:
            splitters.append(set(i for i, char in enumerate(line) if char == "^"))

    return width, beam, splitters
