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
    l = [1, 2, 3]
    a = 2
    b = 2
    print(f"Answer for list [1,2,3] with a=2 and b=2 should be [2, 2, 2]: {fltr(l, a, b)}")
