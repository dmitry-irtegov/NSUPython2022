#!/usr/bin/env python3
"""
This module implements solution for problem 1 in Problems-2 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-2.pdf
"""
import math
import sys


def get_pythagorean_triples(number):
    """
    Returns all Pythagorean triples to the given number
    :param number: given number
    :return: list of Pythagorean triples
    """
    return [
        (x , y, int(math.sqrt(x*x  +  y*y)))
        for x in range(number)
        for y in range(1, x)
        if (math.sqrt(x*x + y*y)).is_integer() and math.sqrt(x*x + y*y) <= number
     ]


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Enter upper bound to generate all Pythagorean triples: '))
            print(get_pythagorean_triples(num))
            break
        except ValueError as e:
            print(f"Invalid value: \n{e}", file=sys.stderr)
        except KeyboardInterrupt:
            print()
            exit(0)
        except EOFError:
            print()
            exit(0)
        except Exception as e:
            print(f"{e}\nTry again", file=sys.stderr)
