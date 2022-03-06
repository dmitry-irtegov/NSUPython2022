#!/usr/bin/env python3
import sys


def problem5(n):
    """Returns a list of prime numbers that are less than the input"""
    # this implementation is naive and thus is slow
    return [a for a in range(2, n + 1)
            if True not in [a % i == 0 for i in range(2, a)]
            ]


def main():
    try:
        print('Enter input number:')

        n = int(input())

        print(problem5(n))

    except Exception as e:
        print('During execution an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}')
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
