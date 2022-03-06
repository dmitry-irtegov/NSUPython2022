#!/usr/bin/env python3
import sys
from typing import Dict, List
import re


def rev_dict(d: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Reverses a dictionary (like the one in the example, not a `dict`)."""
    res = {}
    for i in [a for b in d.values() for a in b]:
        res[i] = []
    for i in d.items():
        for j in i[1]:
            res[j].append(i[0])
    return res


def parse_dict(s: str) -> Dict[str, List[str]]:
    """Parses a dictionary."""
    res = {}
    for i in [j.split('-') for j in s.splitlines()]:
        try:
            key = i[0].strip()
            val = [k.strip() for k in i[1].split(',')]
        except IndexError:
            raise ValueError('Lines have to have the word and its translations separated by "-" symbol')
        if not key.isalpha() or False in [i.isalpha() for i in val]:
            raise ValueError('Words have to be alphabetic and non-empty')
        res[key] = val
    return res


def problem2(s: str):
    """Prints a Latin-English dictionary given an English-Latin dictionary."""
    res = rev_dict(parse_dict(s))
    for i in sorted(res.keys()):
        print(f'{i} - ', end='')
        print(*sorted(res[i]), sep=', ')


def main():
    try:

        default_str = "apple - malum, pomum, popula\nfruit - baca, bacca, popum\npunishment - malum, multa"
        print('Enter input string by string, leave empty for default input:')

        input_str = input()

        if input_str == '':
            input_str = default_str
        else:
            while True:
                print('Enter the next string, leave empty to end input:')
                t = input()
                if t == '':
                    break
                input_str += '\n' + t
        problem2(input_str)

    except Exception as e:
        print('During execution an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}')
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()

