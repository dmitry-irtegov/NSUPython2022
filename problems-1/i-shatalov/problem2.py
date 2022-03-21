import sys
import unittest


def cutter(array, bottom, upper):
    new_array = [bottom if x < bottom else upper if x > upper else x for x in array]
    return new_array


class CutterTestMethods(unittest.TestCase):

    def test_different(self):
        self.assertEqual(cutter([1, 2, 3, 4, 5, 6], 2, 5), [2, 2, 3, 4, 5, 5])

    def test_same(self):
        self.assertEqual(cutter([3, 3, 3, 3], 4, 5), [4, 4, 4, 4])

    def test_still(self):
        self.assertEqual(cutter([3, 4, 5, 6], 2, 7), [3, 4, 5, 6])


if __name__ == "__main__":

    if "--unittest" in sys.argv:
        suite = unittest.TestLoader().loadTestsFromTestCase(CutterTestMethods)
        unittest.TextTestRunner(verbosity=2).run(suite)
        exit()

    while True:
        try:
            input_array = [int(item) for item in input("Enter the list items without commas: ").split()]
            input_bottom = int(input("Enter bottom border: "))
            input_upper = int(input("Enter upper border: "))
            result = cutter(input_array, input_bottom, input_upper)
            print(result)
            exit()
        except ValueError as e:
            print("Error! Please enter valid integer numbers: ", e)
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            exit()
        except IOError:
            print("Error! Please enter valid integer numbers.")
        except Exception:
            print("Unexpected error!")
            exit()
