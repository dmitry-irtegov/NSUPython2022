#!/usr/bin/env python3
"""
This module implements solution for problem 1 in Problems-2 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-2.pdf
"""


if __name__ == '__main__':
    print('Enter upper bound to generate all Pythagorean triples:')
    num = int(input())
    print([
        (x , y, int((x*x +  y*y) **(0.5)))
        for x in range(num)
        for y in range(1, x)
        if ((x*x + y*y) ** (0.5)) % 1 == 0
     ])
