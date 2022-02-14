#!/usr/bin/env python3

def problem2(num_list: [int], lower_bound: int = None, higher_bound: int = None) -> [int]:
    """Returns the input list that is limited by the given bounds"""

    if lower_bound and higher_bound and lower_bound > higher_bound:
        raise ValueError("Lower bound has to be lower than the higher bound")

    # check that lower_bound/higher_bound is set
    # then compare and set the element accordingly
    return [lower_bound if lower_bound and i < lower_bound else
            higher_bound if higher_bound and i > higher_bound else
            i for i in num_list]


if __name__ == '__main__':
    print(problem2(range(10), 3, 7))
    print(problem2(range(10), higher_bound=6))
