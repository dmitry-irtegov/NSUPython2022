#!/usr/bin/env python3

def problem1(num_list: [int]) -> [int]:
    """Returns a list of cumulative sums of first elements of the input."""
    res: [int] = []
    s: int = 0
    for i in num_list:
        res.append(s)
        s += i
    res.append(s)
    return res


if __name__ == '__main__':
    print('Enter the input list (space-separated):')
    input_list = [int(i) for i in input().split()]
    print(problem1(input_list))
