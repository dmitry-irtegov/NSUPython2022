#!/usr/bin/env python3

from problem4 import prepare_pi, pi_find
import sys


def try_and_return(op, operation_str, *args, **kwargs):
    try:
        return op(*args, **kwargs)
    except Exception as e:
        print(f'During {operation_str} an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
        exit(1)
    except KeyboardInterrupt:
        print()
        exit(0)


def main():
    pi = try_and_return(prepare_pi, "reading the pi.txt file")

    while True:
        print('Enter sequence to search for.')
        inp = try_and_return(input, 'reading input from stdin')
        count, res = try_and_return(pi_find, 'finding input in pi', inp, pi)

        print(f'Found {count} result{"s" if count != 1 else ""}.')
        if len(res) > 0:
            print(f'Position{"s" if count != 1 else ""}:', *res[:5], '...' if count > 5 else '')


if __name__ == '__main__':
    main()
