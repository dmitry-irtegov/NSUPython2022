#!/usr/bin/env python3

# NOTE: this solution includes the number 3 before the point
# This will lead to this solution being "off" exactly by 1 (if input is something like 3141, 0 is included)
# i.e. input of "1415" will print "1 6955 ..." instead of "0 6954 ..." , etc
import sys


def main():
    try:
        # pi.txt has to be in the same directory
        with open('pi.txt') as file:
            pi = file.read(-1)

        pi = pi.replace('\n', '')
        pi = pi.replace('.', '')
        while True:
            print('Enter sequence to search for.')

            inp = input()

            res = []
            t = 0
            count = 0
            while inp in pi[t:]:
                t = pi.find(inp, t)
                if len(res) < 5:
                    res.append(t)
                count += 1
                t += 1

            print(f'Found {count} result{"s" if count != 1 else ""}.')
            if len(res) > 0:
                print(f'Position{"s" if count != 1 else ""}:', *res[:5], '...' if count > 5 else '')

    except Exception as e:
        print('During execution an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
