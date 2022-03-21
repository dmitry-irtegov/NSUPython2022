import unittest
from problem1 import get_pythagorean_triples

class TestPythagoreanTriples(unittest.TestCase):
	def test_1(self):
		self.assertEqual(get_pythagorean_triples(3), [])

	def test_2(self):
		self.assertEqual(get_pythagorean_triples(10), [(3, 4, 5), (8, 6, 10)])

	def test_3(self):
		self.assertEqual(get_pythagorean_triples(80), [(3, 4, 5), (8, 6, 10), (5, 12, 13), (15, 8, 17), (12, 16, 20), 
																	  (7, 24, 25), (24, 10, 26), (21, 20, 29), (16, 30, 34), (9, 40, 41), 
																	  (35, 12, 37), (32, 24, 40), (27, 36, 45), (20, 48, 52), (11, 60, 61), 
																	  (48, 14, 50), (45, 28, 53), (40, 42, 58), (33, 56, 65), (24, 70, 74), 
																	  (63, 16, 65), (60, 32, 68), (55, 48, 73), (48, 64, 80)])

if __name__ == '__main__':
	unittest.main()
