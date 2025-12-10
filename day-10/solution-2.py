import sys

from lib import parse_joltage, parse_buttons, depth_first
from machine import BaseMachine


class Machine(BaseMachine):
    def __init__(self, target, buttons, zero, state=None):
        super().__init__(target, buttons, zero, state)

    @classmethod
    def from_string(cls, specification):
        return cls(parse_joltage(specification), parse_buttons(specification), 0)

    def press(self, button):
        for n in self.buttons[button]:
            self.state[n] += 1

    def valid(self):
        return all(a <= b for a, b in zip(self.state, self.target))


def main():
    machines = [Machine.from_string(line.strip()) for line in sys.stdin]
    total = 0

    for m in machines:
        for machine, depth in depth_first(m):
            if machine:
                total += depth

    print(total)


if __name__ == "__main__":
    main()
