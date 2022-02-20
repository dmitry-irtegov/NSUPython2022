#!/usr/bin/env python3
"""
This module implements solution for problem 4 in Problems-1 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-1.pdf
"""


def ten_green_bottles():
    """
    Function prints lyrics of song "Ten Green Bottles"
    """
    bottles = ' green bottle{s} hanging on the wall{comma}'
    numbers = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'No']

    for i in range(10):
        print(numbers[i] + bottles.format(s='s' if i!= 9 else '', comma=','))
        print(numbers[i] + bottles.format(s='s' if i!= 9 else '', comma=','))
        print('And if one green bottle should accidentally fall,')
        print('There’ll be ' + numbers[i+1].lower() + bottles.format(s='s' if (i+1)!= 9 else '', comma=''), end='.\n\n')

if __name__ == '__main__':
    ten_green_bottles()
