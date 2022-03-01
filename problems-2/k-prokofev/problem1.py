#!/usr/bin/env python3

from math import sqrt
import unittest


def triplets(maxNumber: int) -> list:
    return [
        [x, y, int(sqrt(x ** 2 + y ** 2))]
        for x in range(1, maxNumber)
        for y in range(x + 1, maxNumber)
        if sqrt(x ** 2 + y ** 2) <= maxNumber and sqrt(x ** 2 + y ** 2) % 1 == 0
    ]


if __name__ == '__main__':
    print("Number: ", end="")
    number = input()
    while not number.isdigit():
        print("Warning: Incorrect value. Please, enter an integer number", end=": ")
        number = input()
    number = int(number)
    print(f"Result: {triplets(number)}")


class TestTriplets(unittest.TestCase):
    def test_1(self):
        self.assertEqual(triplets(1), [])

    def test_2(self):
        self.assertEqual(triplets(5), [[3, 4, 5]])

    def test_3(self):
        self.assertEqual(triplets(10), [[3, 4, 5], [6, 8, 10]])
