import unittest
from io import StringIO
import time
from problem1 import Timer

class TestTimer(unittest.TestCase):
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
			self.assertEqual(ValueError, type(e))

	def test_4(self):
		with Timer():
			try:
				time.sleep(1)
				raise TypeError("Exception test")
			except Exception as e:
				self.assertEqual(TypeError, type(e))

	def helper_test_5(self):
		with Timer():
			raise ValueError("Exception test")

	def test_5(self):
		self.assertRaises(ValueError, self.helper_test_5)

if __name__ == '__main__':
	unittest.main()
