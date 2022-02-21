#!/usr/bin/env python3
"""
This module implements solution for problem 3 in Problems-1 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-1.pdf
"""


def collatz(n):
    """
    Function implements Collatz hypothesis - i.e. get a positive number n.
    If it is even, we will replace it with n/2, if not, we will replace it with 3n+1.
    We apply the same actions to the resulting number, and so on, until we get 1.
    :param n: positive number
    :return: result of testing Collatz hypothesis
    """
    if n < 1:
        raise ValueError("Number must be positive")
    res = [n]
    num = n
    while num > 1:
        num = (num // 2) if num % 2 == 0 else (3 * num + 1)
        res.append(num)
    return res


def chain_printer(nums):
    """
    Pretty print for result of collatz function
    :param nums: result of collatz function
    """
    print(' -> '.join(str(x) for x in nums))


if __name__ == '__main__':
    print("Enter positive number to test Collatz hypothesis:")
    chain_printer(collatz(int(input())))
