#!/usr/bin/env python3
import sys

from problem3_impl import collatz

if __name__ == "__main__":
    print("Enter number to check collatz hypothesis")
    try:
        n = int(input())
    except ValueError:
        print(f"You provided not an integer", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"Keyboard interrupt happened", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print(f"EOF reached", file=sys.stderr)
        sys.exit(1)

    try:
        print(*collatz(n), sep=" -> ")
    except ValueError as e:
        print(f"{e}")
