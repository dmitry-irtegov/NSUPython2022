#!/usr/bin/env python3
import sys


def trim_nums(l, l_bound, up_bound):
    """
    Return list where every element less than l_bound turns into l_bound
    and every element greate than u_bound turns into u_bound
    :param l: list to transform
    :param l_bound: lower bound
    :param up_bound: upper bound
    :return: transformed list
    """
    lowed_result = map(lambda x: l_bound if x < l_bound else x, l)
    result = list(map(lambda x: up_bound if x > up_bound else x, lowed_result))
    return result


if __name__ == "__main__":
    print("Enter numbers to trim (divided by whitespace):")
    try:
        l = [int(elem) for elem in input().split()]
        print("Enter lower bound and upper bound")

        lower_bound, upper_bound = [int(elem) for elem in input().split()]

        if lower_bound > upper_bound:
            print("lower bound must be less or equal then upper")
            exit(1)

        print(trim_nums(l, lower_bound, upper_bound))

    except ValueError:
        print("You must provide only numbers divided by space", file=sys.stderr)
        exit(1)
