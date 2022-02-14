#!/usr/bin/env python3

from typing import Dict, List


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
    for i in [i.split(' - ') for i in s.splitlines()]:
        key = i[0]
        val = i[1].split(', ')
        res[key] = val
    return res


def problem2(s: str):
    """Prints a Latin-English dictionary given an English-Latin dictionary."""
    res = rev_dict(parse_dict(s))
    for i in sorted(res.keys()):
        print(f'{i} - ', end='')
        print(*sorted(res[i]), sep=', ')


if __name__ == '__main__':
    teststring = "apple - malum, pomum, popula\nfruit - baca, bacca, popum\npunishment - malum, multa"
    problem2(teststring)


