#!/usr/bin/env python3

def problem3(n: int) -> [int]:
    """Returns a list of numbers that emerge from checking Collatz conjecture on the input."""
    if n < 1:
        raise ValueError("Input number has to be positive")
    res = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        res.append(n)
    return res


if __name__ == '__main__':
    print(*problem3(10), sep=' -> ')
