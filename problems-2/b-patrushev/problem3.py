#!/usr/bin/env python3
"""
This module implements solution for problem 3 in Problems-2 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-2.pdf
"""
import argparse
import os
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List files in a directory sorted by size')
    parser.add_argument('path', type=str, help='Path to directory')
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print('Path not found', file=sys.stderr)
        sys.exit(-1)

    if not os.path.isdir(args.path):
        print('Path is not a directory', file=sys.stderr)
        sys.exit(-1)

    files = []
    for name in os.listdir(args.path):
        full_path = os.path.join(args.path, name)
        if os.path.isfile(full_path):
            files.append([os.stat(full_path).st_size, name])

    for size, name in sorted(files, key=lambda x: (-x[0], x[1])):
        print(f'{name}  {size}B')
