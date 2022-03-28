#!/usr/bin/env python3
import unittest
import sys


def collatz(number: int):
    result = str(number)
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            result += ' --> ' + str(number)
        else:
            number = 3 * number + 1
            result += ' --> ' + str(number)
    return result


if __name__ == '__main__':
    while True:
        try:
            a = int(input('Enter number: '))
            result = collatz(a)
            print(result)
            break
        except ValueError as e:
            print('Please enter an integer. Try again.', sys.stderr)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt received")
            sys.exit()
        except EOFError:
            print("\nEOFError received")
            sys.exit()
        except Exception as e:
            sys.exit(f"Error: {e}")
    unittest.main()


class TestСollatz(unittest.TestCase):
    def test_1(self):
        self.assertEqual(collatz(16), "16 --> 8 --> 4 --> 2 --> 1")

    def test_2(self):
        self.assertEqual(collatz(1), "1")
