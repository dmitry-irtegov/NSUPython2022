#!/usr/bin/env python3

import argparse as ap
import sys


def main():
    try:
        parser = ap.ArgumentParser(usage="An analogue of UNIX's tr utility")
        parser.add_argument('old', help="the list of symbols to be replaced")
        parser.add_argument('new', help='the list of symbols that "old" symbols will be translated to')
        parser.add_argument('-d', '--delete', dest='delete', default='', help='the list of symbols to be deleted')

        args = parser.parse_args()
        translate_arr = []
        for i in range(min(len(args.old), len(args.new))):
            translate_arr.append((args.old[i], args.new[i]))

        while True:

            try:
                t = input()
            except EOFError:
                break

            for i in args.delete:
                t = t.replace(i, '')
            for a, b in translate_arr:
                t = t.replace(a, b)
            print(t)

    except Exception as e:
        print('During execution an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
