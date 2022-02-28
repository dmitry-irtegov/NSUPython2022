#!/usr/bin/env python3
"""
This module implements solution for problem 5 in Problems-2 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-2.pdf
"""
from math import sqrt


def get_primes(n):
    """
    Retruns list of prime numbers to the given numbers
    :param n: given number
    :return: list of prime numbers
    """
    return [
        i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, int(sqrt(i)) + 1))
    ]


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Enter upper bound to generate list of prime numbers: '))
            print(get_primes(num))
            break
        except ValueError as e:
            print(f'Invalid input: \n{e} \nTry again.')
        except KeyboardInterrupt:
            print()
            exit(0)
        except EOFError as e:
            print()
            exit(0)
        except Exception as e:
            print(f"{e}\nTry again")
