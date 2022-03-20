import unittest


def collatz(num):
    """
    This function return all steps collatz hypothesis before it reaches 1 (included)
    :param num: start number
    :return: list of all computed collatz steps
    """
    if type(num) is not int or num <= 0:
        raise ValueError("You must provide only integers object greater then 0")
    result = []
    while num != 1:
        result.append(num)
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    result.append(1)
    return result


class TestCollatz(unittest.TestCase):
    def test_simple(self):
        self.assertListEqual(collatz(1), [1])
        self.assertListEqual(collatz(12), [12, 6, 3, 10, 5, 16, 8, 4, 2, 1])
        self.assertListEqual(collatz(5), [5, 16, 8, 4, 2, 1])
        self.assertListEqual(collatz(14), [14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

        self.assertListEqual(collatz(2), [2, 1])

    def test_error(self):
        self.assertRaises(ValueError, collatz, 5.5)
        self.assertRaises(ValueError, collatz, "meow")
        self.assertRaises(ValueError, collatz, None)


if __name__ == "__main__":
    unittest.main()
