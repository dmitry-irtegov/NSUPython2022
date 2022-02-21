#!/usr/bin/env python3

def fltr(list: [int], a: int, b: int):
    if b < a:
        raise ValueError("upper limit B is less then lower limit A.")
    result = [compare(element, a, b) for element in list]
    return result


def compare(element, a, b):
    if element < a:
        return a
    if element > b:
        return b
    return element


if __name__ == '__main__':
    l = input('Enter the list: ')
    a = int(input('lower bound: '))
    b = int(input('upper bound: '))
    result = fltr(map(int, l.split()), a, b)
    print('Answer for the list is: ', result)
