#!/usr/bin/env python3

from problem3 import get_filenames_and_sizes_from_dir
import os.path
import sys


def try_and_return(op, operation_str, *args, **kwargs):
    try:
        return op(*args, **kwargs)
    except Exception as e:
        print(f'During {operation_str} an exception was raised:', file=sys.stderr)
        print(f'{type(e).__name__}: {e}', file=sys.stderr)
        exit(1)
    except KeyboardInterrupt:
        print()
        exit(0)


def main():
    d: str
    # set current working directory as the directory if no parameters were passed
    if len(sys.argv) == 1:
        d = try_and_return(os.getcwd, 'getting the current directory')
    else:
        d = sys.argv[1]

    files_and_sizes = try_and_return(
        get_filenames_and_sizes_from_dir,
        'getting the filenames and sizes from the directory', d)

    max_name_len = max(len(i[0]) for i in files_and_sizes) if len(files_and_sizes) > 0 else 0

    for i in sorted(files_and_sizes, key=lambda x: x[1], reverse=True):
        print(i[0] + '-' * (max_name_len - len(i[0])), i[1], 'B')


if __name__ == "__main__":
    main()
