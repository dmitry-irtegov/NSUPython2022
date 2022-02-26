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

    print('Enter the two bounds (space-separated, enter "-" to skip a bound):')
    while True:
        try:
            a = input().split()
            b = int(a[1]) if a[1] != '-' else None
            a = int(a[0]) if a[0] != '-' else None

            if a and b and a > b:
                print('The lower bound should go first, higher should go second. Try again.')
                continue
            
            break
        except ValueError:
            print('The bounds should be integers or "-". Try again.', file=sys.stderr)
        except IndexError:
            print('Two bounds should be entered. Try again.', file=sys.stderr)
        except KeyboardInterrupt:
            print()
            exit(0)

    print('Answer: ')
    print(problem2(input_list, a, b))


if __name__ == '__main__':
    main()
