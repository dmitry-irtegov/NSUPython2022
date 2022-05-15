import os
import sys
import operator
from argparse import ArgumentParser

def getFilesInDirectory(path):
    try:
        entries = os.listdir(path)
    except OSError as e:
        raise OSError(f"Couldn't open {path} for listing") from e
    entries_fullpaths = map(lambda x: os.path.join(path, x), entries)
    regular_files = list(filter(os.path.isfile, entries_fullpaths))
    regular_files_with_negative_sizes = zip(regular_files,
                                   map(lambda x: -os.stat(x).st_size, regular_files))
    regular_files_with_negative_sizes = list(regular_files_with_negative_sizes)
    regular_files_with_negative_sizes.sort(key=operator.itemgetter(1, 0), reverse=False)
    
    return list(map(lambda x: (x[0], -x[1]), regular_files_with_negative_sizes))

def prettyPrint(filesList):
    for file, size in filesList:
        print(f"{file} {size} B")

if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument("path", type=str, help="path to the directory to list")
	args = parser.parse_args()

	try:
		prettyPrint(getFilesInDirectory(args.path))
	except Exception as e:
		sys.exit(f"Error: {str(e)}")
