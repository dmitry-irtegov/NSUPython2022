import math


class Vector:

    def __init__(self, vals):
        self.vals = tuple(vals)

    def __len__(self):
        return len(self.vals)

    def __add__(self, other):
        return Vector([self.vals[i] + other.vals[i] for i in range(len(self))])

    def __neg__(self):
        return Vector([-x for x in self.vals])

    def __sub__(self, other):
        return self + (-other)

    def __getitem__(self, item):
        return self.vals[item]

    def __mul__(self, other):
        return sum(self.vals[i] * other.vals[i] for i in range(len(self)))

    def __str__(self):
        return str(self.vals)

    def __eq__(self, other):
        return self.vals == other.vals

    def length(self):
        return math.sqrt(sum(self.vals[i] ** 2 for i in range(len(self))))

    def multiply_by_scalar(self, num):
        return Vector([x * num for x in self.vals])
