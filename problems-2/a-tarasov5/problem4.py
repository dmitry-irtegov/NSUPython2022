import sys

from problem4_impl import find_in_pi_file

if __name__ == "__main__":
    while True:
        try:
            num = input("Enter digit sequence you want to find into ./pi.txt or exit> ")
            if num == "exit":
                exit(0)
            int(num)
        except ValueError:
            print("You didn't enter number", file=sys.stderr)
            exit(1)
        except (EOFError, KeyboardInterrupt):
            exit(0)

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
            exit(1)
