import sys


def read_data():
    result = {}
    for line in sys.stdin:
        line = line.strip()
        name = line.split(": ")[0]
        outputs = line.split()[1:]
        assert(len(outputs) == len(set(outputs)))
        result[name] = outputs

    return result
