#!/usr/bin/env python3

import os.path
import sys


def main():
    d: str
    # set current working directory as the directory if no parameters were passed
    if len(sys.argv) == 1:
        d = os.getcwd()
    else:
        d = sys.argv[1]

    files = []
    try:
        files = [f for f in os.listdir(d)
                 if os.path.isfile(os.path.join(d, f))]
    except FileNotFoundError:
        print(f'Directory "{d}" does not exist.', file=sys.stderr)
        exit(1)
    except NotADirectoryError:
        print(f'"{d}" is a file, not a directory.', file=sys.stderr)
        exit(1)
    except PermissionError:
        print(f'You don\'t have permission to access "{d}".')
        exit(1)

    filesize_dict = {}
    if len(files) == 0:
        max_name_len = 0
    else:
        max_name_len = max([len(f) for f in files])
    for f in files:
        filesize_dict[f] = os.stat(os.path.join(d, f)).st_size

    filesize_dict = sorted(filesize_dict.items(), key=lambda x: x[0])
    for i in sorted(filesize_dict, key=lambda x: x[1], reverse=True):
        print(i[0] + '-' * (max_name_len - len(i[0])), i[1], 'B')


if __name__ == "__main__":
    main()
