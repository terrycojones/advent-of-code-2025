from lib import read_input


def invalid(n):
    s = str(n)
    length = len(s)
    if length % 2 == 0:
        half = length >> 1
        if s[:half] == s[half:]:
            return n
    return 0


total = 0

for a, b in read_input():
    for n in range(a, b+1):
        total += invalid(n)

print(total)
