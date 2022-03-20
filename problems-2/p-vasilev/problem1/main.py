#!/usr/bin/env python3

from problem1 import problem1
import sys


def main():
    print('Enter input number:')

    n = 0
    try:
        n = int(input())
        if n < 1:
            raise ValueError('Input has to be positive.')

    except Exception as e:
        operation_str = "input collection"
        print(f'During {operation_str} an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
        exit(1)
    except KeyboardInterrupt:
        print()
        exit(0)

    res = problem1(n)

    for i in res:
        print(i)


if __name__ == '__main__':
    main()
