#!/usr/bin/env python3
import pytest


def factor(number):
    result = []
    multiplier = 2
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
    try:
        a = int(input('Enter number: '))
        result = factor(a)
        print(result)
    except ValueError as e:
        print('Please enter an integer. Try again.', e)


class Factor:
    def test_1(self):
        assert factor(12) == [[2, 2], [3, 1]]

    def test_2(self):
        assert factor(0) == []

    def test_3(self):
        assert factor(1) == [1, 1]

    def test_4(self):
        assert factor(13) == [13, 1]
