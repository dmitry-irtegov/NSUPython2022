#!/usr/bin/env python3
"""
This module implements solution for problem 2 in Problems-1 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-1.pdf
"""

def trim(nums, a, b):
    """
    Takes as input a sequence of numbers, as well as a lower bound and an upper
    bound, and “trim” all numbers in accordance with this range
    :param nums: list of numbers
    :param a: lower bound
    :param b: upper bound
    :return: result list
    """
    res = []
    for num in nums:
        if num < a:
            res.append(a)
        elif num > b:
            res.append(b)
        else:
            res.append(num)
    return res


if __name__ == '__main__':
    print("Enter the numbers (space separated):")
    nums = map(int, input().split())
    print("Enter two bounds (space separated):")
    a, b = map(int, input().split())
    print(trim(nums, a, b))
