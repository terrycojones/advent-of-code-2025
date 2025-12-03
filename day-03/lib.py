def largest_from(start, ints, n_ints):
    for target in range(9, -1, -1):
        for i in range(start, n_ints + 1):
            if ints[i] == target:
                return target, i

    raise ValueError("Inconceivable!")
