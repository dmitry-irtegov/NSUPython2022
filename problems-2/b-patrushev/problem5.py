#!/usr/bin/env python3
"""
This module implements solution for problem 5 in Problems-2 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-2.pdf
"""

if __name__ == '__main__':
    print('Enter upper bound to generate list of prime numbers')
    num = int(input())
    print([
        i for i in range(2, num + 1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))
    ])
