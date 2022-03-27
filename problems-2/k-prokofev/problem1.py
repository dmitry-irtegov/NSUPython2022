#!/usr/bin/env python3

from math import sqrt
import unittest
import sys

def triplets(maxNumber: int) -> list:
    return [
        [x, y, int(sqrt(x ** 2 + y ** 2))]
        for x in range(1, maxNumber)
        for y in range(x + 1, maxNumber)
        if sqrt(x ** 2 + y ** 2) <= maxNumber and sqrt(x ** 2 + y ** 2).is_integer()
    ]


if __name__ == '__main__':
    while True:
        try:
            print("Number: ", end="")
            number = int(input())
            break
        except ValueError as e:
            print('Input is not integer. Try again.', file=sys.stderr)

    print(f"Result: {triplets(number)}")
    unittest.main()


class TestTriplets(unittest.TestCase):
    def test_1(self):
        self.assertEqual(triplets(1), [])

    def test_2(self):
        self.assertEqual(triplets(5), [[3, 4, 5]])

    def test_3(self):
        self.assertEqual(triplets(10), [[3, 4, 5], [6, 8, 10]])
