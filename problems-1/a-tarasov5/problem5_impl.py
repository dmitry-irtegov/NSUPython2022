from collections import Counter
import unittest


def prime_factors(n):
    """
    Return prime factors of n
    :param n: positive integer
    :returns: list of pairs [p,k] where p - prime number, k - its frequency
    """
    if type(n) is not int:
        raise TypeError(f"You must provide integers, but you provided {type(n)}")

    if n < 0:
        raise ValueError(f"You must provide positive integers, but you provided {n}")
    i = 2
    factors = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    return [[p, k] for p, k in Counter(factors).items()]


class TestPrimeFactors(unittest.TestCase):

    def test_simple_cases(self):
        self.assertCountEqual(prime_factors(2 ** 2 * 3), [[2, 2], [3, 1]])
        self.assertCountEqual(prime_factors(11 * 83), [[11, 1], [83, 1]])
        self.assertCountEqual(prime_factors(2 * 3 * 11 * 29), [[2, 1], [3, 1], [11, 1], [29, 1]])
        self.assertCountEqual(prime_factors(2 ** 5 * 7 ** 3), [[7, 3], [2, 5]])

    def test_edge_cases(self):
        self.assertCountEqual(prime_factors(31 * 31), [[31, 2]])
        self.assertCountEqual(prime_factors(1), [])
        self.assertCountEqual(prime_factors(-131), [])

    def test_errors(self):
        self.assertRaises(TypeError, prime_factors, None)
        self.assertRaises(TypeError, prime_factors, "ABOBA")
        self.assertRaises(TypeError, prime_factors, 3.3)
        self.assertRaises(ValueError, prime_factors, -3)

if __name__ == '__main__':
    unittest.main()
