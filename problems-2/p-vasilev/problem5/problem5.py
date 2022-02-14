#!/usr/bin/env python3

def problem5(n):
    """Returns a list of prime numbers that are less than the input"""
    return [a for a in range(2, n + 1)
            if True not in [a % i == 0 for i in range(2, a)]
            ]


if __name__ == '__main__':
    print(problem5(50))
