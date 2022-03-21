#!/usr/bin/env python3

from io import StringIO
from problem2 import reverse_dictionary_from_file
import sys


def main():
    input_str = ""

    if len(sys.argv) == 2:
        input_str = sys.argv[1]
    elif len(sys.argv) > 2:
        print("This program takes at most 1 (one) (singular) argument.", file=sys.stderr)
        exit(1)

    if input_str == '-h' or input_str == '--help':
        print('Pass filename as an argument, pass nothing to get default dictionary')
        exit(0)

    default_str = StringIO("apple - malum, pomum, popula\nfruit - baca, bacca, popum\npunishment - malum, multa")
    print('Enter a name of a file that contains a dictionary, leave empty for default input:')

    res = {}

    try:
        with default_str if input_str == '' else open(input_str) as file:
            try:
                res = reverse_dictionary_from_file(file)
            except Exception as e:
                op_str = "while parsing input"
                print(f'An exception was raised {op_str}:', file=sys.stderr)
                print(f'{type(e).__name__}: {e}', file=sys.stderr)
                exit(1)

    except Exception as e:
        op_str = "while trying to open the file"
        print(f'An exception was raised {op_str}:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
        exit(1)

    for i in sorted(res.keys()):
        print(f'{i} - ', end='')
        print(*res[i], sep=', ')


if __name__ == '__main__':
    main()