#!/usr/bin/env python3
"""
This module implements solution for problem 1 in Problems-2 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-2.pdf
"""
import math


def check(number):
    return math.ceil(number) == math.floor(number)


def get_pythagorean_triples(number):
    """
    Returns all Pythagorean triples to the given number
    :param number: given number
    :return: list of Pythagorean triples
    """
    return [
        (x , y, int(math.sqrt(x*x +  y*y)))
        for x in range(num)
        for y in range(1, x)
        if check(math.sqrt(x*x + y*y))
     ]


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Enter upper bound to generate all Pythagorean triples: '))
            print(get_pythagorean_triples(num))
            break
        except ValueError as e:
            print(f"Invalid value: \n{e}")
        except KeyboardInterrupt:
            print()
            exit(0)
        except EOFError as e:
            print()
            exit(0)
        except Exception as e:
            print(f"{e}\nTry again")
