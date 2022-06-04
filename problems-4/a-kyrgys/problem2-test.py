#!/usr/bin/env python3
import unittest
from problem2 import tr


class TestStringMethods(unittest.TestCase):

    def test_incorrect_table(self):
        self.assertRaises(ValueError, tr, 'abcabc', 'a', '12', '')

    def test_duplicate(self):
        self.assertRaises(ValueError, tr, 'abcabc', 'aa', '12', '')

    def test_replace(self):
        self.assertEqual(tr('abcabc', 'abc', '123', ''), '123123')

    def test_del(self):
        self.assertEqual(tr('abcabc', '', '', 'a'), 'bcbc')

    def test_replace_and_del(self):
        self.assertEqual(tr('abcabc', 'abc', '123', 'c'), '1212')


if __name__ == '__main__':
    unittest.main()