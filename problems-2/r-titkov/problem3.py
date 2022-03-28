import os
import sys
from argparse import ArgumentParser

def getDirFiles(path):
	"""
	The function takes a directory path and prints
	file name and file size for each file in the directory.

	:param path: path to directory
	"""

	try:
		files = [s for s in os.listdir(path) 
			if os.path.isfile(os.path.join(path, s))
		]
	except Exception as e:
		e.args = ("Error occurred while listing directory: ", ) + e.args
		raise e.with_traceback(e.__traceback__)

	try:
		files_and_sizes = [
			(file, os.stat(os.path.join(path, file)).st_size) 
			for file in files
		]
	except Exception as e:
		e.args = ("Error occurred while listing directory: ", ) + e.args
		raise e.with_traceback(e.__traceback__)

	files_and_sizes.sort(key=lambda elem: (-elem[1], elem[0]))
	for filename, size in files_and_sizes:
		print(f'{filename} - {size} bytes')


if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument("path", type=str, help="Enter path to the directory")
	args = parser.parse_args()

	try:
		getDirFiles(args.path)
	except Exception as e:
		sys.exit(e.args[0] + str(e))
