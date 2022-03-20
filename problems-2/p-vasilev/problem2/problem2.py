#!/usr/bin/env python3

import unittest
from io import StringIO
from typing import List, IO, Dict


def parse_a_singular_line_of_text(s: str) -> (str, List[str]):
    """Parses the input string (a line (singular)) into a tuple of a word and its translations
    (see example dictionary for reference)"""
    s = s.lower()
    s_split = s.split('-')

    if len(s_split) != 2:
        raise ValueError('Lines have to have the word and its translations separated by "-" symbol')

    key, val = s_split
    key = key.strip()
    val = [i.strip() for i in val.split(',')]

    if not key.isalpha() or False in [i.isalpha() for i in val]:
        raise ValueError('Words have to be alphabetic and non-empty')

    return key, val


def reverse_dictionary_from_file(file: IO) -> Dict[str, List[str]]:
    """Reverses an English-Latin dictionary contained in a file-like object"""
    res: Dict[str, List[str]] = {}

    for line in file:
        a, b = parse_a_singular_line_of_text(line)

        for i in b:
            if i not in res.keys():
                res[i] = []
        for i in b:
            res[i].append(a)

    res = {i: sorted(res[i]) for i in res}

    return res


class Problem2Tests(unittest.TestCase):
    def test_example(self):
        input_str = StringIO("apple - malum, pomum, popula\nfruit - baca, bacca, popum\npunishment - malum, multa")
        self.assertEqual(reverse_dictionary_from_file(input_str),
                         {'baca': ['fruit'],
                          'bacca': ['fruit'],
                          'malum': ['apple', 'punishment'],
                          'multa': ['punishment'],
                          'pomum': ['apple'],
                          'popula': ['apple'],
                          'popum': ['fruit']}
                         )

    def test_empty(self):
        input_str = StringIO('')
        self.assertEqual(reverse_dictionary_from_file(input_str), {})

    def test_non_alpha_input(self):
        self.assertRaises(ValueError, reverse_dictionary_from_file, StringIO('42 - 19, 20'))

    def test_not_separated_input(self):
        self.assertRaises(ValueError, reverse_dictionary_from_file, StringIO('apple malum, popum'))

    def test_too_much_separated(self):
        self.assertRaises(ValueError, reverse_dictionary_from_file, StringIO('apple - malum - popum'))

    def test_double_comma(self):
        self.assertRaises(ValueError, reverse_dictionary_from_file, StringIO('apple - malum,, popum'))

    def test_no_comma(self):
        self.assertRaises(ValueError, reverse_dictionary_from_file, StringIO('apple - malum popum'))

    def test_no_translation(self):
        self.assertRaises(ValueError, reverse_dictionary_from_file, StringIO('apple - '))

    def test_no_word(self):
        self.assertRaises(ValueError, reverse_dictionary_from_file, StringIO(' - malum, popum'))


if __name__ == '__main__':
    unittest.main(verbosity=2)

