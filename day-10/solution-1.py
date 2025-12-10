import sys

from lib import parse_target, parse_buttons, depth_first
from machine import BaseMachine


class Machine(BaseMachine):
    def __init__(self, target, buttons, zero, state=None):
        super().__init__(target, buttons, zero, state)

    @classmethod
    def from_string(cls, specification):
        return cls(parse_target(specification), parse_buttons(specification), False)

    def press(self, button):
        for n in self.buttons[button]:
            self.state[n] = not self.state[n]

    def valid(self):
        return True


def read_machines():
    return [Machine.from_string(line.strip()) for line in sys.stdin]


def main():
    machines = read_machines()
    total = 0

    for m in machines:
        for machine, depth in depth_first(m):
            if machine:
                total += depth

    print(total)


if __name__ == "__main__":
    main()
