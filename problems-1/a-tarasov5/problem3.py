#!/usr/bin/env python3

def collatz(num):
    """
    This function return all steps collatz hypothesis before it reaches 1 (included)
    :param num: start number
    :return: list of all computed collatz steps
    """

    result = []
    while num != 1:
        result.append(num)
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    result.append(1)
    return result


if __name__ == "__main__":
    print("Enter number to check collatz hypothesis")
    n = int(input())
    print(*collatz(n), sep=" -> ")
