import sys
import unittest


def get_primes(num: int):

    if num <= 0:
        raise ValueError

    factors = {}
    i = 2

    while i * i <= num:
        if num % i != 0:
            i += 1
        else:
            num //= i
            factors[i] = factors.get(i, 0) + 1

    if num > 1:
        factors[num] = factors.get(num, 0) + 1

    result = []
    for key in sorted(factors.keys()):
        result.append([key, factors[key]])

    return result


class PrimesTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_primes(12), [[2, 2], [3, 1]])

    def test_simple_large(self):
        self.assertEqual(get_primes(1000), [[2, 3], [5, 3]])

    def test_negative(self):
        self.assertRaises(ValueError, get_primes, -1)

    def test_zero(self):
        self.assertRaises(ValueError, get_primes, 0)

    def test_wrong_type(self):
        self.assertRaises(TypeError, get_primes, 'a')


if __name__ == '__main__':
    if "--unittest" in sys.argv:
        suite = unittest.TestLoader().loadTestsFromTestCase(PrimesTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
        exit()

    while True:
        try:
            number = int(input("Please enter integer number > 0: "))
            print('Result: ', get_primes(number))
            exit()
        except ValueError as e:
            print("Error! Please enter valid integer number > 0: ", e)
        except KeyboardInterrupt:
            print("Keyboard interrupt occurred.")
            exit()
        except IOError:
            print("IO error occurred. Please enter only integer number > 0.")
        except Exception:
            print("Unexpected error occurred. Aborting..")
            exit()
