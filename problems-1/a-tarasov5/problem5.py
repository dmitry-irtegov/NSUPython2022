import sys

from problem5_impl import prime_factors

if __name__ == "__main__":
    print("Enter number you want to factorize")
    try:
        num = int(input())
        print(prime_factors(num))
    except (ValueError, EOFError):
        print("You entered not number", file=sys.stderr)
        exit(1)
    except KeyboardInterrupt:
        print(f"Keyboard interrupt happened", file=sys.stderr)
        sys.exit(1)
