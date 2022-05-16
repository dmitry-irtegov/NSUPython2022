import unittest
from problem4 import load_file, find_substrings, finder


class TestFactorize(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_substrings('123'),
            (4185, [1923, 2937, 2975, 3891, 6547])
        )

    def test_2(self):
        self.assertEqual(find_substrings('1415'),
            (423, [6954, 29135, 45233, 79686, 85879])
        )

    def test_3(self):
        self.assertEqual(find_substrings('1239324'),
            (1, [2643353])
        )

    def test_4(self):
        self.assertEqual(find_substrings('37400061115498'),
            (0,[])
        )

if __name__ == '__main__':
    unittest.main()
