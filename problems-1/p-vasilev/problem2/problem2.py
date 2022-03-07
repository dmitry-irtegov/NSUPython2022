#!/usr/bin/env python3
import sys


def problem2(num_list: [int], lower_bound: int = None, higher_bound: int = None) -> [int]:
    """Returns the input list that is limited by the given bounds"""

    try:
        if lower_bound > higher_bound:
            raise ValueError("Lower bound has to be lower than the higher bound")
    except TypeError:
        pass

    # check that lower_bound/higher_bound is set
    # then compare and set the element accordingly
    return [lower_bound if lower_bound and i < lower_bound else
            higher_bound if higher_bound and i > higher_bound else
            i for i in num_list]


def main():
    try:
        print('Enter the input list (space-separated):')
        input_list = [int(i) for i in input().split()]

        print('Enter the two bounds (space-separated, enter "-" to skip a bound):')
        bounds = input().split()
        a = int(bounds[0]) if bounds[0] != '-' else None
        b = int(bounds[1]) if bounds[1] != '-' else None

        if a and b and a > b:
            raise ValueError('The lower bound should go first, higher should go second.')

        print('Answer: ')
        print(problem2(input_list, a, b))

    except Exception as e:
        print('During execution an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
