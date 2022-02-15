#!/usr/bin/env python3

def cumulativeSums(list):
    result = [0]
    currentSum = 0
    for element in list:
        currentSum += element
        result.append(currentSum)
    return result

if __name__ == '__main__':
     print(f"cumulativeSums [1,3,5,7] should be [0, 1, 4, 9, 16]: {cumulativeSums([1,3,5,7])}")
