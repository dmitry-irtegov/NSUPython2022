#!/usr/bin/env python3

def problem1(n):
    """Returns all the Pythagorean triples from numbers not bigger than the input."""
    if n < 1:
        raise ValueError('Input has to be positive')

    rng = range(1, n + 1)
    return [(x, y, z)
            for x in rng
            for y in rng
            for z in rng
            if (x ** 2 + y ** 2 == z ** 2 and x < y)]


if __name__ == '__main__':
    print(problem1(100))
