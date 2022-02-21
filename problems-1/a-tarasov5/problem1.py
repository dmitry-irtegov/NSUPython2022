#!/usr/bin/env python3

def cum_sum(l):
    """
    Compute cumulative sums of the list with first value equal to zero
    :param l: list to compute cumulative sums
    :return: cumulative sums
    """
    result = [0]
    for elem in l:
        result.append(result[-1] + elem)
    return result


if __name__ == '__main__':
    print("Enter number to compute cumulative sums (divided by whitespace):")
    l = [int(elem) for elem in input().split()]
    print(cum_sum(l))
