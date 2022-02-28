#!/usr/bin/env python3
import pytest


def cumulativeSums(list):
    result = [0]
    currentSum = 0
    for element in list:
        currentSum += element
        result.append(currentSum)
    return result


if __name__ == '__main__':
    in_s = input('Enter the numbers: ')
    try:
        list = map(int, in_s.split())
        result = cumulativeSums(list)
        print('Result is:', result)
    except ValueError:
        print('Please enter integers. Try again.')


class TestSums():
    def test_1(self):
        assert cumulativeSums([1, 3, 5, 7]) == [0, 1, 4, 9, 16]

    def test_2(self):
        assert cumulativeSums([0]) == [0, 0]

    def test_3(self):
        assert cumulativeSums([]) == [0]

    def test_4(self):
        assert cumulativeSums(range(1, 18)) == [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153]
