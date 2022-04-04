import os
from argparse import ArgumentParser
from collections import namedtuple

FileStat = namedtuple('FileStat', ['name', 'size'])


def files_stat_print(file_stats):
    max_len = max([len(file_stat.name) for file_stat in file_stats])
    for file_stat in file_stats:
        print(f"{file_stat.name:{max_len}} {file_stat.size} bytes")


def get_statistic(path):
    dir_statistic = []
    try:
        with os.scandir(path) as files:
            for f in files:  # As I found it does not raise any exceptions
                try:
                    if not f.is_file():
                        continue
                except OSError as e:
                    raise OSError(f"Cannot get filetype of {f.name}") from e

                try:
                    dir_statistic.append(FileStat(f.name, f.stat().st_size))
                except OSError as e:
                    raise OSError(f"Cannot get file size of {f.name}") from e

    except Exception as e:
        raise type(e)(f"Exception occurred while trying to scan {path} directory") from e

    dir_statistic.sort(key=lambda l: (l.size, l.name), reverse=True)
    return dir_statistic


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("path", type=str, help="path to directory you want to list")
    args = parser.parse_args()
    try:
        files_stat_print(get_statistic(args.path))
    except Exception as e:
        exit(e)
