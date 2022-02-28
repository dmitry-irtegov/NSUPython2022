#!/usr/bin/env python3
"""
This module implements solution for problem 5 in Problems-1 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-1.pdf
"""
from math import sqrt


def primes(num):
    """
    Function implements prime factorization of given number
    :param num: number to factorize into prime numbers
    :return: a list in which each prime factor p and its degree k corresponds to the pair (p, k)
    """
    res = []
    for p in range(2, int(sqrt(num) + 1)):
        k = 0
        while num % p == 0:
            num //= p
            k += 1
        if k != 0:
            res.append([p, k])
    if num > 2:
        res.append([num, 1])
    return res if len(res) > 0 else [[num, 1]]


if __name__ == '__main__':
    while True:
        try:
            num = int(input("Enter number to factorize into prime numbers: "))
            if num < 1:
                print("Sorry, input must be a positive integer. Try again")
                continue
            print(primes(num))
            break
        except ValueError as e:
            print(f"Invalid input: \n{e} \nTry again")
