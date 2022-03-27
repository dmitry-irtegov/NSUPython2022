import unittest
from problem5 import generate_primes


class TestFactorize(unittest.TestCase):
	def test_1(self):
		self.assertEqual(
			generate_primes(1),
			([])
		)
	
	def test_2(self):
		self.assertEqual(
			generate_primes(2),
			([2])
		)

	def test_3(self):
		self.assertEqual(
			generate_primes(100),
			([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
		)

	def test_4(self):
		self.assertEqual(
			generate_primes(-100),
			([])
		)

	def test_5(self):
		self.assertRaises(TypeError, generate_primes, 'number')


if __name__ == '__main__':
	unittest.main()
