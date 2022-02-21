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
    result = cumulativeSums(map(int, in_s.split()))
    print('Result is:', result)
