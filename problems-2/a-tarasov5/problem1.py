import sys

from problem1_test import pythagorean_triples

if __name__ == "__main__":
    print("Enter number you want to limit pythagorean triples to")
    try:
        num = int(input())
        print(pythagorean_triples(num))
    except ValueError:
        print("You entered not a number", file=sys.stderr)
        exit(1)
