#!/usr/bin/env python3
import sys


def problem1(num_list: [int]) -> [int]:
    """Returns a list of cumulative sums of first elements of the input."""
    res: [int] = []
    s: int = 0
    for i in num_list:
        res.append(s)
        s += i
    res.append(s)
    return res


def main():
    try:
        print('Enter the input list (space-separated):')
        input_list = [int(i) for i in input().split()]
        print('Answer: ')
        print(*problem1(input_list))
    except Exception as e:
        print('During execution an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
