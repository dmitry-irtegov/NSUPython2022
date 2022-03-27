import unittest
from itertools import count, takewhile


def prime_nums(upper_bound):
    return [x for x in range(2, upper_bound + 1) if
            all(x % y != 0 for y in takewhile(lambda num: num * num <= x, count(2, 1)))]


class PrimeNumsTest(unittest.TestCase):
    def test_simple_cases(self):
        self.assertListEqual(prime_nums(0), [])
        self.assertListEqual(prime_nums(3), [2, 3])
        self.assertListEqual(prime_nums(12), [2, 3, 5, 7, 11])
        self.assertListEqual(prime_nums(13), [2, 3, 5, 7, 11,13])
        self.assertListEqual(prime_nums(-333), [])

        self.assertEqual(prime_nums(500)[-1], 499)
        self.assertEqual(len(prime_nums(500)), 95)

    def test_errors(self):
        self.assertRaises(TypeError, prime_nums, None)
        self.assertRaises(TypeError, prime_nums, "222")
        self.assertRaises(TypeError, prime_nums, 14.5)


if __name__ == "__main__":
    unittest.main()
