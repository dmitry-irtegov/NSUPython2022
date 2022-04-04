import unittest
from io import StringIO
import time
from problem1 import Timer

class TestPythagoreanTriples(unittest.TestCase):
	def test_1(self):
		out = StringIO()

		with Timer(output=out):
			time.sleep(3)

		output = out.getvalue().strip()
		self.assertEqual('Took time: 3 seconds', output)

	def test_2(self):
		out = StringIO()

		with Timer(output=out):
			time.sleep(0)

		output = out.getvalue().strip()
		self.assertEqual('Took time: 0 seconds', output)

	def test_3(self):
		try:
			with Timer():
				time.sleep(1)
				raise ValueError("Exception test")
		except Exception as e:
			return self.assertEqual(ValueError, type(e))
			
		return False


if __name__ == '__main__':
	unittest.main()
