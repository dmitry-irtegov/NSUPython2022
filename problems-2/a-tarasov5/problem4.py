import sys

from problem4_test import find_in_pi_file

if __name__ == "__main__":
    try:
        num = input("Enter digit sequence you want to find into ./pi.txt> ")
        int(num)
    except (ValueError, EOFError):
        print("You didn't enter number", file=sys.stderr)
        exit(1)

    try:
        positions = find_in_pi_file(num)
        print(f"Found {len(positions)} results.")
        print(f"Positions: {' '.join(map(str, positions[:5]))}", end="")
        if len(positions) > 5:
            print(f" ...")
        else:
            print()

    except OSError:
        print("Cannot open/read file pi.txt", file=sys.stderr)
