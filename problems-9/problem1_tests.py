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
		def helper_test_3():
			try:
				with Timer():
					time.sleep(1)
					raise ValueError("Exception test")
			except ValueError:
				return 'Exception received'
			return None
		
		self.assertEqual('Exception received', helper_test_3())

	def test_4(self):
		def helper_test_4():
			with Timer():
				try:
					time.sleep(1)
					raise TypeError("Exception test")
				except TypeError:
					return 'Exception received'
			return None

		self.assertEqual('Exception received', helper_test_4())

	def test_5(self):
		def helper_test_5():
			with Timer():
				raise ValueError("Exception test")

		self.assertRaises(ValueError, helper_test_5)

if __name__ == '__main__':
	unittest.main()
