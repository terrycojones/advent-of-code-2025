import sys
import bisect


class Ingredients:
    def __init__(self):
        ranges = []
        ingredients = []

        for line in sys.stdin:
            line = line.strip()
            if line:
                fields = list(map(int, line.split("-")))
                try:
                    a, b = fields
                except ValueError:
                    ingredients.append(fields[0])
                else:
                    if b < a:
                        a, b = b, a
                    ranges.append((a, b))

        self.ranges = self.merge_ranges(sorted(ranges))
        self.ingredients = ingredients

    def merge_ranges(self, ranges):
        result = []
        last_a, last_b = ranges[0]

        for a, b in ranges[1:]:
            if a <= last_b:
                last_b = max(b, last_b)
            else:
                result.append((last_a, last_b))
                last_a, last_b = a, b

        result.append((last_a, last_b))

        return result

    def is_fresh(self, ingredient):
        pos = bisect.bisect_left(self.ranges, (ingredient, ingredient))
        if pos <= len(self.ranges):
            a, b = self.ranges[pos - 1]
            return a <= ingredient <= b
        else:
            return False

    def count_fresh(self):
        return sum(self.is_fresh(ingredient) for ingredient in self.ingredients)

    def total_fresh(self):
        return sum((b - a + 1) for a, b in self.ranges)
