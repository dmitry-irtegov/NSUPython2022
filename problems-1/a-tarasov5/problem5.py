import sys

from problem5_impl import prime_factors

if __name__ == "__main__":
    print("Enter number you want to factorize")
    try:
        num = int(input())
    except ValueError:
        print("You entered not number", file=sys.stderr)
        exit(1)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

    try:
        print(prime_factors(num))
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

