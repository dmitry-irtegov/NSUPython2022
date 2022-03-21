import sys
import unittest


def calculate(n):
    array = [(a, b, c) for a in range(1, n)
             for b in range(a, n)
             for c in range(b, n) if (a ** 2 + b ** 2) == c ** 2]
    return array


class TestCalculateMethod(unittest.TestCase):

    def test_none(self):
        self.assertEqual(calculate(5), [])

    def test_single(self):
        self.assertEqual(calculate(7), [(3, 4, 5)])

    def test_several(self):
        self.assertEqual(calculate(50), [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17),
                                         (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37),
                                         (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29),
                                         (21, 28, 35), (24, 32, 40), (27, 36, 45)])


if __name__ == "__main__":
    # unittest.main()
    if "--unittest" in sys.argv:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculateMethod)
        unittest.TextTestRunner(verbosity=2).run(suite)
        exit(0)

    while True:
        try:
            n = int(input("Please enter number: "))
            print(calculate(n))
            exit(0)
        except ValueError as e:
            print("Error: please enter valid integer number - ", e)
        except KeyboardInterrupt as e:
            print("Keyboard interrupt. ", e)
            exit()
        except IOError:
            print("Some Error occurred. Please enter valid integer number.")
        except Exception:
            print("Unexpected Error occurred.")
            exit()
