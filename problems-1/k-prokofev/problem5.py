#!/usr/bin/env python3
import unittest
import sys


def factor(number):
    result = []
    multiplier = 2
    if not isinstance(number, int):
        return []

    while multiplier * multiplier <= number:
        pow = 0
        while number % multiplier == 0:
            pow += 1
            number //= multiplier
        if pow > 0:
            result.append([multiplier, pow])
        else:
            multiplier += 1
    if number >= 1:
        result.append([number, 1])
    return result


if __name__ == '__main__':
    while True:
        try:
            a = int(input('Enter number: '))
            result = factor(a)
            print(result)
            break
        except ValueError as e:
            print('Please enter an integer. ', sys.stderr)
        print('Tests:', unittest.main())


class TestFactor(unittest.TestCase):
    def test_0(self):
        self.assertEqual(factor(0), [])

    def test_1(self):
        self.assertEqual(factor(1), [[1, 1]])

    def test_2(self):
        self.assertEqual(factor('someText'), [])

    def test_3(self):
        self.assertEqual(factor(1000000000000), [[2, 12], [5, 12], [1, 1]])

    def test_4(self):
        self.assertEqual(factor(-100), [])
