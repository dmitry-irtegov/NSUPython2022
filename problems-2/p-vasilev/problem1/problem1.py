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
    print('Enter input number:')
    while True:
        try:
            n = int(input())
            if n < 1:
                print('Input has to be positive. Try again.', file=sys.stderr)
                continue
            break

        except ValueError:
            print('Input should be an integer. Try again.', file=sys.stderr)

        except KeyboardInterrupt:
            print()
            exit(0)

    for i in problem1(n):
        print(i)


if __name__ == '__main__':
    main()
