import unittest
from problem4 import load_pi_number, find_sequences


class TestFactorize(unittest.TestCase):
	def test_1(self):
		self.assertEqual(
			find_sequences(load_pi_number("pi.txt"), '123'), 
			(['1923', '2937', '2975', '3891', '6547'], 4185)
		)
	
	def test_2(self):
		self.assertEqual(
			find_sequences(load_pi_number("pi.txt"), '1415'), 
			(['0', '6954', '29135', '45233', '79686'], 424)
		)

	def test_3(self):
		self.assertEqual(
			find_sequences(load_pi_number("pi.txt"), '1239324'), 
			(['2643353'], 1)
		)

	def test_4(self):
		self.assertEqual(
			find_sequences(load_pi_number("pi.txt"), '374928365498'), 
			([], 0)
		)

	def test_5(self):
		self.assertEqual(
			find_sequences(load_pi_number("pi.txt"), 123), 
			(['1923', '2937', '2975', '3891', '6547'], 4185)
		)

	def test_6(self):
				self.assertEqual(
			find_sequences('123123123', '123'), 
			(['0', '3', '6'], 3)
		)

	def test_7(self):
		self.assertRaises(ValueError, find_sequences, load_pi_number("pi.txt"), 123.0)

	def test_8(self):
		self.assertRaises(ValueError, find_sequences, load_pi_number("pi.txt"), [123.0])

	def test_9(self):
		self.assertRaises(ValueError, find_sequences, 0, '123')


if __name__ == '__main__':
	unittest.main()
