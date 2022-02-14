#!/usr/bin/env python3

import os.path
import sys

if __name__ == "__main__":
    d: str
    # set current working directory as the directory if no parameters were passed
    if len(sys.argv) == 1:
        d = os.getcwd()
    else:
        d = sys.argv[1]

    files = [f for f in os.listdir(d)
             if os.path.isfile(os.path.join(d, f))]
    filesize_dict = {}
    max_name_len = max([len(f) for f in files])
    for f in files:
        filesize_dict[f] = os.stat(os.path.join(d, f)).st_size
    for i in sorted(sorted(filesize_dict.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True):
        print(i[0] + '-' * (max_name_len - len(i[0])), i[1], 'B')
