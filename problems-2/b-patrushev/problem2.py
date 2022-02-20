#!/usr/bin/env python3
"""
This module implements solution for problem 2 in Problems-2 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-2.pdf
"""


def rev_dict(filename):
    """
    Function prints a Latin-English dictionary
    based on English-Latin dictionary.
    :param filename: filename of English-Latin dictionary
    """
    defs = {}
    with open(filename, 'r') as f:
        for ln in f.readlines():
            eng, latin = ln.rstrip().split(' - ')
            for wds in latin.split(', '):
                if wds in defs:
                    defs[wds].append(eng)
                else:
                    defs[wds] = [eng]

    for latin, eng in sorted(defs.items()):
        print(f'{latin} - {", ".join(eng)}')


if __name__ == '__main__':
   rev_dict('problem2.txt')
