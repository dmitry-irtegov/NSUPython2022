import unittest


def find_many(string, substring, limit=None):
    """
    Finds all indices of the substring in the string.
    :param string: the specified string
    :param substring: the specified substring
    :return: the list of indices
    """

    start = 0
    result = []

    while True:
        start = string.find(substring, start)
        if start == -1:
            return result
        result.append(start)
        start += 1


def find_in_pi_file(string):
    """
    finds the first six occurrences of a num in a file pi.txt
    :param string: number that you want to find in pi.txt
    :returns: six first positions of this substring
    """
    if not hasattr(find_in_pi_file, "digits"):
        filepath = "./pi.txt"
        with open(filepath, "r") as file:
            find_in_pi_file.digits = "".join(file.read()[2:].split('\n'))

    return find_many(find_in_pi_file.digits, string)


class TestPiFinder(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(len(find_in_pi_file("123")), 4185)
        self.assertListEqual(find_in_pi_file("123")[:5], [1923, 2937, 2975, 3891, 6547])

        self.assertEqual(len(find_in_pi_file("1415")), 424)
        self.assertListEqual(find_in_pi_file("1415")[:5], [0, 6954, 29135, 45233, 79686])

        self.assertListEqual(find_in_pi_file("12345")[:5], [49701, 181675, 224815, 447855, 538330])

        self.assertListEqual(find_in_pi_file("00000")[:5], [17533, 211057, 215286, 652114, 752326])

    def test_last_subseq(self):
        digits_count = 4194303
        print(digits_count - 7 in find_in_pi_file("5841350")[:5])

    def test_errors(self):
        self.assertRaises(TypeError, find_in_pi_file, 123)
        self.assertRaises(TypeError, find_in_pi_file, None)


if __name__ == "__main__":
    unittest.main()
