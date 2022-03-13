#!/usr/bin/env python3
import sys
import math


def problem1(n):
    """Returns all the Pythagorean triples from numbers not bigger than the input."""
    return [(x, y, int(math.sqrt(x * x + y * y)))
            for x in range(1, n + 1)
            for y in range(x, n + 1)
            if math.ceil(math.sqrt(x * x + y * y)) == math.floor(math.sqrt(x * x + y * y))
            and int(math.sqrt(x * x + y * y)) <= n]


def main():
    try:
        print('Enter input number:')
        n = int(input())
        if n < 1:
            raise ValueError('Input has to be positive. Try again.')

        for i in problem1(n):
            print(i)

    except Exception as e:
        print('During execution an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
