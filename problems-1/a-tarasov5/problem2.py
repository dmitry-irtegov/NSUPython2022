#!/usr/bin/env python3
import sys

from problem2_impl import trim_nums

if __name__ == "__main__":
    print("Enter numbers to trim (divided by whitespace):")
    try:
        l = [int(elem) for elem in input().split()]
        print("Enter lower bound and upper bound")

        lower_bound, upper_bound = [int(elem) for elem in input().split()]
    except ValueError:
        print("You must provide only numbers divided by space", file=sys.stderr)
        exit(1)
    except KeyboardInterrupt:
        print("keyboard interrupt", file=sys.stderr)
        exit(1)
    except EOFError:
        print("EOF occurred", file=sys.stderr)
        exit(1)

    try:
        print(trim_nums(l, lower_bound, upper_bound))
    except ValueError as e:
        print(f"{e}", file=sys.stderr)
        exit(1)
