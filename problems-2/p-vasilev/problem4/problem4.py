#!/usr/bin/env python3

# NOTE: this solution includes the number 3 before the point
# This will lead to this solution being "off" exactly by 1 (if input is something like 3141, 0 is included)
# i.e. input of "1415" will print "1 6955 ..." instead of "0 6954 ..." , etc
import sys
import unittest


def prepare_pi():
    # pi.txt has to be in the same directory
    with open('pi.txt') as file:
        pi = file.read(-1)

    pi = pi.replace('\n', '')
    pi = pi.replace('.', '')
    return pi


def pi_find(inp, pi):
    res = []
    t = 0
    count = 0
    while inp in pi[t:]:
        t = pi.find(inp, t)
        if len(res) < 5:
            res.append(t)
        count += 1
        t += 1
    return count, res


class Problem4Tests(unittest.TestCase):
    def setUp(self):
        self.pi = prepare_pi()

    def test_zero(self):
        self.assertEqual(pi_find('1234123412341234', self.pi)[0], 0)

    def test_position_0(self):
        self.assertIn(0, pi_find('31415', self.pi)[1])

    def test_position_1(self):
        self.assertIn(1, pi_find('14159', self.pi)[1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
