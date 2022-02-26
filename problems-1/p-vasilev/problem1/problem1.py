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
    print('Enter the input list (space-separated):')
    while True:
        try:
            input_list = [int(i) for i in input().split()]
            break
        except ValueError:
            print('Input should only contain integers. Try again.', file=sys.stderr)
        except KeyboardInterrupt:
            print()
            exit(0)

    print('Answer: ')
    print(*problem1(input_list))


if __name__ == '__main__':
    main()
