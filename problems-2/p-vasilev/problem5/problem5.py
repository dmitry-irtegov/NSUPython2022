#!/usr/bin/env python3
import sys


def problem5(n):
    """Returns a list of prime numbers that are less than the input"""
    # this implementation is naive and thus is slow
    return [a for a in range(2, n + 1)
            if True not in [a % i == 0 for i in range(2, a)]
            ]


def main():
    print('Enter input number:')
    while True:
        try:
            n = int(input())
            break

        except ValueError:
            print('Input should be an integer. Try again.', file=sys.stderr)

        except KeyboardInterrupt:
            print()
            exit(0)

    print(problem5(n))


if __name__ == '__main__':
    main()
