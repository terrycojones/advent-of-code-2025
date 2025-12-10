def parse_target(specification):
    return tuple(
        True if c == "#" else False for c in specification.split()[0][1:-1]
    )


def parse_joltage(specification):
    return tuple(
        map(int, specification.split()[-1][1:-1].split(","))
    )


def parse_buttons(specification):
    return tuple(
        tuple(map(int, button[1:-1].split(",")))
        for button in specification.split()[1:-1]
    )


def depth_first(origin):
    buttons = list(range(len(origin)))
    seen = set()
    machines = [(origin, 0)]

    while machines:
        machine, depth = machines.pop(0)
        seen.add(machine)
        for button in buttons:
            new = machine.copy()
            new.press(button)
            if new.valid() and new not in seen:
                seen.add(new)
                machines.append((new, depth + 1))
        yield machine, depth
