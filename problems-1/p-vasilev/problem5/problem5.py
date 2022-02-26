#!/usr/bin/env python3
import sys
from typing import Dict


def isprime(n: int) -> bool:
    """Checks whether a number is prime."""
    if n <= 0:
        raise ValueError
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    t = 1
    while (6 * t - 1) ** 2 <= n:
        if n % (6 * t - 1) == 0 or n % (6 * t + 1) == 0:
            return False
        t += 1
    return True


def nextprime(n: int) -> int:
    """Gets a number that's bigger than input and prime
    (the input has to be prime)"""
    if n <= 1:
        raise ValueError
    if n == 2:
        return 3
    if n == 3:
        return 5
    t = (n - 1) // 6 if (n - 1) % 6 == 0 else (n + 1) // 6
    while True:
        guess = 6 * t - 1
        if isprime(guess) and guess > n:
            return guess
        guess = 6 * t + 1
        if isprime(guess) and guess > n:
            return guess
        t += 1


def problem5(n: int) -> Dict[int, int]:
    """Splits a number into its prime factors.
    Returns a dictionary representing the result of factorization."""
    res = {}
    t = 2

    # stop if n is prime or is a 1
    while not isprime(n) and not n == 1:

        # if t divides n, get the degree of the factor
        if n % t == 0:
            res[t] = 0
            while n % t == 0:
                n = n // t
                res[t] += 1

        # get the next prime to check
        t = nextprime(t)

    # add n itself into the dictionary if it isn't a 1
    if n != 1:
        res[n] = 1
    return res


def main():
    print('Enter input number:')
    while True:
        try:
            n = int(input())
            if n <= 0:
                print('The input has to be a positive integer. Try again.', file=sys.stderr)
                continue
            break

        except ValueError:
            print('Input should be an integer. Try again.', file=sys.stderr)

        except KeyboardInterrupt:
            print()
            exit(0)

    print(problem5(n))


if __name__ == '__main__':
    main()
