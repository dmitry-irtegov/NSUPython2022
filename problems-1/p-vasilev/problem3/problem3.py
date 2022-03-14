#!/usr/bin/env python3
import sys


def problem3(n: int) -> [int]:
    """Returns a list of numbers that emerge from checking Collatz conjecture on the input."""
    if n < 1:
        raise ValueError("Input number has to be positive")
    res = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        res.append(n)
    return res


def main():
    try:
        print('Enter input number:')
        print(*problem3(int(input())), sep=' -> ')
                
    except Exception as e:
        print('During execution an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
