#!/usr/bin/env python3
import unittest
import sys


def cumulativeSums(list):
    result = [0]
    currentSum = 0
    for element in list:
        currentSum += element
        result.append(currentSum)
    return result


if __name__ == '__main__':
    while True:
        try:
            in_s = input('Enter the numbers: ')
            list = map(int, in_s.split())
            result = cumulativeSums(list)
            print('Result is:', result)
            break
        except ValueError as e:
            print('Input is not integers. ', sys.stderr)
    print('Tests:', unittest.main())

class TestSums(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cumulativeSums([1, 3, 5, 7]), [0, 1, 4, 9, 16])


    def test_2(self):
        self.assertEqual(cumulativeSums([0]), [0, 0])

    def test_3(self):
        self.assertEqual(cumulativeSums([]), [0])

    def test_4(self):
        self.assertEqual(cumulativeSums(range(1, 18)), [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153])
