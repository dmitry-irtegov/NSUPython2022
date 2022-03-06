#!/usr/bin/env python3
import sys


def problem1(n):
    """Returns all the Pythagorean triples from numbers not bigger than the input."""
    rng = range(1, n + 1)
    return [(x, y, z)
            for x in rng
            for y in rng
            for z in rng
            if (x ** 2 + y ** 2 == z ** 2 and x < y)]


def main():
    try:
        print('Enter input number:')
        n = int(input())
        if n < 1:
            raise ValueError('Input has to be positive. Try again.')

        for i in problem1(n):
            print(i)

    except Exception as e:
        print('During execution an exception was raised:')
        print(f'{type(e).__name__}: {e}')
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
