import sys
import unittest


def collatz_conjecture(number: int):
    arr = [number]
    if number > 0:
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                arr.append(number)
            else:
                number = 3 * number + 1
                arr.append(number)
    else:
        raise ValueError
    return arr


class CollatzConjectureTestMethods(unittest.TestCase):
    def test_correct_number(self):
        self.assertEqual(collatz_conjecture(3), [3, 10, 5, 16, 8, 4, 2, 1])

    def test_number_one(self):
        self.assertEqual(collatz_conjecture(1), [1])

    def test_number_zero(self):
        self.assertRaises(ValueError, collatz_conjecture, 0)

    def test_wrong_input(self):
        self.assertRaises(TypeError, collatz_conjecture, 'a')

    def test_negative_number(self):
        self.assertRaises(ValueError, collatz_conjecture, -1)


if __name__ == "__main__":

    if "--unittest" in sys.argv:
        suite = unittest.TestLoader().loadTestsFromTestCase(CollatzConjectureTestMethods)
        unittest.TextTestRunner(verbosity=2).run(suite)
        exit()

    while True:
        try:
            n = int(input("Please enter integer number > 0: "))
            print('->'.join(map(str, collatz_conjecture(n))))
        except ValueError as e:
            print("Error! Please enter valid integer number > 0: ", e)
        except KeyboardInterrupt:
            print("Keyboard interrupt occurred.")
            exit()
        except IOError:
            print("IO error occurred. Please enter only integer number > 0.")
        except EOFError:
            print("EOF occured. Aborting..")
            exit()
        except Exception:
            print("Unexpected error occurred. Aborting..")
            exit()
