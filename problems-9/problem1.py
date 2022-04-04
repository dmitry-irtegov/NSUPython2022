import time
import sys

class Timer(object):
	def __init__(self, output=sys.stderr):
		self._output = output

	def __enter__(self):
		self._start_time = time.time()

	def __exit__(self, exc_type, exc_val, exc_tb):
		time_delta = time.time() - self._start_time
		print(f'Took time: {round(time_delta)} seconds', file=self._output)


if __name__ == '__main__':
	with Timer():
		time.sleep(1)
