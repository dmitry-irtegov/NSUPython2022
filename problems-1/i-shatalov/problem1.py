import sys
import unittest


def cumulative(array):
    res = 0
    tmpArr = [0]
    for x in array:
        res += x
        tmpArr.append(res)
    return tmpArr


class TestCumulative(unittest.TestCase):

    def test_three(self):
        self.assertEqual(cumulative([1, 2, 3]), [0, 1, 3, 6])

    def test_four(self):
        self.assertEqual(cumulative([1, 2, 3, 4]), [0, 1, 3, 6, 10])

    def test_ten(self):
        self.assertEqual(cumulative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55])


if __name__ == "__main__":
    if "--unittest" in sys.argv:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCumulative)
        unittest.TextTestRunner(verbosity=2).run(suite)
        exit()

    while True:
        try:
            input_array = [int(value) for value in input("Please enter array of numbers: ").split()]
            print(cumulative(input_array))
            exit()
        except ValueError as e:
            print("Error: ", e)
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            exit()
        except IOError:
            print("Some Error occurred. Please enter valid integer number.")
        except Exception:
            print("Unexpected error occurred.")
            exit()
