import os
import sys
from argparse import ArgumentParser

def getDirFiles(path):
	"""
	The function takes a directory path and prints
	file name and file size for each file in the directory.

	:param path: path to directory
	"""

	files = [s for s in os.listdir(path) 
		if os.path.isfile(os.path.join(path, s))
	]
	files_and_sizes = [
		(file, os.stat(os.path.join(path, file)).st_size) 
		for file in files
	]
	files_and_sizes.sort(key=lambda elem: (-elem[1], elem[0]))
	for filename, size in files_and_sizes:
		print(f'{filename} - {size} bytes')


if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument("path", type=str, help="Enter path to the directory")
	args = parser.parse_args()
	try:
		getDirFiles(args.path)
	except NotADirectoryError as e:
		print(f'NotADirectoryError occurred for "{e.filename}": {e.strerror}', file=sys.stderr)
	except FileNotFoundError as e:
		print(f'FileNotFoundError occurred for "{e.filename}": {e.strerror}', file=sys.stderr)
	except OSError as e:
		print(f'OSError occurred for "{e.filename}": {e.strerror}', file=sys.stderr)
