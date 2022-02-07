#!/usr/bin/env python3

def cumulativeSums(list):
    result = [0]
    currentSum = 0
    for element in list:
        currentSum += element
        result.append(currentSum)
    return result