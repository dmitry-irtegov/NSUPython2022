import os
from argparse import ArgumentParser

def getDirFiles(path):
	if not os.path.exists(path) or not os.path.isdir(path):
		raise ValueError("Incorrect directory path")

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
	parser.add_argument("path", help="Enter path to the directory")
	args = parser.parse_args()
	getDirFiles(args.path)
