#!/usr/bin/env python3

from typing import List, Tuple
import math
import unittest


def problem1(n: int) -> List[Tuple[int, int, int]]:
    """Returns all the Pythagorean triples from numbers not bigger than the input."""
    res = []
    for x in range(1, n + 1):
        for y in range(x, n + 1):
            z = math.sqrt(x * x + y * y)
            if z.is_integer() and z <= n:
                res.append((x, y, int(z)))
    return res


class Problem1Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(problem1(3), [])

    def test_5(self):
        self.assertEqual(problem1(5), [(3, 4, 5)])

    def test_negative(self):
        self.assertEqual(problem1(-1), [])

    def test_19(self):
        self.assertEqual(problem1(19), [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)])


if __name__ == '__main__':
    unittest.main(verbosity=2)
