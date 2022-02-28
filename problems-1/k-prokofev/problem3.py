#!/usr/bin/env python3

def collatz(number: int):
    result = str(number)
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            result += ' --> ' + str(number)
        else:
            number = 3 * number + 1
            result += ' --> ' + str(number)
    return result


if __name__ == '__main__':
    try:
        a = int(input('Enter number: '))
        result = collatz(a)
        print(result)
    except ValueError:
        print('Please enter an integer. Try again.')
