from sys import stderr
from os import listdir, stat
from os.path import isdir, isfile, join
from argparse import ArgumentParser, ArgumentTypeError


def dir_path(path):
    """
    Checks if the path is a valid directory path, otherwise throws an error.

    :param path: the directory path to check
    :return: the specified path argument
    """

    if isdir(path):
        return path
    else:
        raise ArgumentTypeError(f'"{path}" is not a valid directory path')


def dir_stats(path):
    """
    Gets statistics for each file in the directory.

    :param path: the specified directory path
    :return: a sorted list of tuples of file names and sizes
    """

    result = []
    for filename in listdir(path):
        filepath = join(path, filename)
        if isfile(filepath):
            filesize = stat(filepath).st_size
            result.append((filename, filesize))
    return sorted(result, key=lambda x: (-x[1], x[0]))


if __name__ == '__main__':
    parser = ArgumentParser(description='Lists the contents of a directory and sorts them by size.')
    parser.add_argument('path', type=dir_path, help='a directory path to list contents')
    args = parser.parse_args()

    try:
        statistics = dir_stats(args.path)
        for name, size in statistics:
            print(f'{name} - {size} bytes')
    except OSError as e:
        print(f'Failed to get statistics for "{e.filename}": {e.strerror}', file=stderr)
