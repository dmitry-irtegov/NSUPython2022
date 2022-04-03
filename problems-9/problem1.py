import time

class Timer(object):
	def __enter__(self):
		self.start_time = time.time()

	def __exit__(self, exc_type, exc_val, exc_tb):
		time_delta = time.time() - self.start_time
		print(f'Took time: {round(time_delta, 3)} seconds')


if __name__ == '__main__':
	with Timer():
		time.sleep(1)
