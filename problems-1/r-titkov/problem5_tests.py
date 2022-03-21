import unittest
from problem5 import factorize

class TestFactorize(unittest.TestCase):
	def test_1(self):
		self.assertEqual(factorize(1), [[1, 1]])

	def test_2(self):
		self.assertEqual(factorize(179), [[179, 1]])

	def test_3(self):
		self.assertEqual(factorize(4096), [[2, 12]])

	def test_4(self):
		self.assertEqual(factorize(6343429), [[6343429, 1]])

	def test_5(self):
		self.assertEqual(factorize(3302628420), [[2, 2], [3, 1], [5, 1], [7, 2], [13, 2], [17, 2], [23, 1]])

	def test_6(self):
		self.assertRaises(ValueError, factorize, 's')

	def test_7(self):
		self.assertRaises(ValueError, factorize, -123)

	def test_8(self):
		self.assertRaises(ValueError, factorize, 34.5)
	

if __name__ == '__main__':
	unittest.main()
