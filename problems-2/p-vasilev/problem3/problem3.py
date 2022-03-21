#!/usr/bin/env python3

import os.path
import sys
import unittest
from typing import List, Tuple


def get_filenames_from_dir(d: str) -> List[str]:
    return [f for f in os.listdir(d)
            if os.path.isfile(os.path.join(d, f))]


def get_filenames_and_sizes_from_dir(d: str) -> List[Tuple[str, int]]:
    """Returns a list of tuples of names and sizes of files in a given directory."""
    files = get_filenames_from_dir(d)

    filesize_dict = {}

    for f in files:
        filesize_dict[f] = os.stat(os.path.join(d, f)).st_size

    filesize_dict = sorted(filesize_dict.items(), key=lambda x: x[0])

    res = []

    for i in sorted(filesize_dict, key=lambda x: x[1], reverse=True):
        res.append((i[0], i[1]))

    return res


# This is a class that adds utilities for tests
# Do not use in other contexts!
class _Problem3TestUtil:
    dirname = "./_problem3_temporary_test_directory"

    def setUp(self):
        os.mkdir(self.dirname)

    def tearDown(self):
        for i in [os.path.join(self.dirname, i) for i in os.listdir(self.dirname)]:
            os.remove(i)
        os.rmdir(self.dirname)

    @staticmethod
    def create_dummy_file(file, size):
        with open(os.path.join(Problem3TestEmpty.dirname, file), 'w') as f:
            f.write('L' * size)


# Test: empty directory
class Problem3TestEmpty(unittest.TestCase, _Problem3TestUtil):
    def setUp(self):
        _Problem3TestUtil.setUp(self)

    def tearDown(self):
        _Problem3TestUtil.tearDown(self)

    def test_empty(self):
        self.assertEqual(get_filenames_and_sizes_from_dir(self.dirname), [])


# Test: directory with some dummy files
class Problem3TestSimple(unittest.TestCase, _Problem3TestUtil):
    def setUp(self):
        _Problem3TestUtil.setUp(self)
        self.create_dummy_file('a', 10)
        self.create_dummy_file('b', 5)
        self.create_dummy_file('asdf', 20)
        self.create_dummy_file('c', 5)

    def tearDown(self):
        _Problem3TestUtil.tearDown(self)

    def test_simple(self):
        self.assertEqual(get_filenames_and_sizes_from_dir(self.dirname), [('asdf', 20), ('a', 10), ('b', 5), ('c', 5)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
