#!/usr/bin/env python3
import sys
from io import StringIO
from typing import List


def parse_a_singular_line_of_text(s: str) -> (str, List[str]):
    """Parses the input string (a line (singular)) into a tuple of a word and its translations
    (see example dictionary for reference)"""
    s_split = s.split('-')

    if len(s_split) != 2:
        raise ValueError('Lines have to have the word and its translations separated by "-" symbol')

    key, val = s_split
    key = key.strip()
    val = [i.strip() for i in val.split(',')]

    if not key.isalpha() or False in [i.isalpha() for i in val]:
        raise ValueError('Words have to be alphabetic and non-empty')

    return key, val


def main():
    try:
        default_str = StringIO("apple - malum, pomum, popula\nfruit - baca, bacca, popum\npunishment - malum, multa")
        print('Enter a name of a file that contains a dictionary, leave empty for default input:')

        input_str = input()
        res = {}

        with default_str if input_str == '' else open(input_str) as file:
            for line in file:
                a, b = parse_a_singular_line_of_text(line)
                for i in b:
                    if i not in res.keys():
                        res[i] = []
                for i in b:
                    res[i].append(a)

        for i in sorted(res.keys()):
            print(f'{i} - ', end='')
            print(*sorted(res[i]), sep=', ')

    except Exception as e:
        print('During execution an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()

