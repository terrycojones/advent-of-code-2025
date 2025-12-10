class BaseMachine:
    def __init__(self, target, buttons, zero, state=None):
        self.target = target
        self.buttons = buttons
        self.zero = zero
        self.state = state or ([zero] * len(target))

    def __repr__(self):
        return "".join(str(int(s)) for s in self.state)

    def __bool__(self):
        return tuple(self.state) == self.target

    def __len__(self):
        return len(self.buttons)

    def __hash__(self):
        return hash(tuple(self.state))

    def __eq__(self, other):
        return self.state == other.state

    def __str__(self):
        target = "".join("#" if c else "." for c in self.target)
        state = "".join(str(int(s)) for s in self.state)
        buttons = " ".join(f"({','.join(map(str, button))})" for button in self.buttons)
        return f"{state} [{target}] {buttons}"

    def copy(self):
        return self.__class__(self.target, self.buttons, self.zero, list(self.state))
