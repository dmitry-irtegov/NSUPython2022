#!/usr/bin/env python3

def cumulativeSums(list):
    result = [0]
    currentSum = 0
    for element in list:
        currentSum += element
        result.append(currentSum)
    return result


if __name__ == '__main__':
    in_s = input('Enter the numbers: ')
    try:
        list = map(int, in_s.split())
        result = cumulativeSums(list)
        print('Result is:', result)
    except ValueError:
        print('Please enter integers. Try again.')
