import unittest
from problem1 import Table


class MyTestCase(unittest.TestCase):
    def test_1(self):
        t1 = Table([[1, 2, 3], [2, 3, 4, 5], [6, 7, 8, 9]])
        self.assertEqual(t1.head(1).__str__(), '1 2 3 0\n')

    def test_2(self):
        t1 = Table([[1, 2, 3], [2, 3, 4, 5], [6, 7, 8, 9]])
        self.assertEqual(t1.tail(1).__str__(), '6 7 8 9\n')

    def test_3(self):
        t1 = Table([[1, 2, 3], [2, 3, 4, 5], [6, 7, 8, 9]])
        self.assertEqual(t1.get_row(1).__str__(), '[2, 3, 4, 5]')

    def test_4(self):
        t1 = Table([[1, 2, 3], [2, 3, 4, 5], [6, 7, 8, 9]])
        self.assertEqual(t1.get_columns([0, 2]).__str__(), '1 3\n2 4\n6 8\n')

    def test_5(self):
        t1 = Table([[1, 2, 3], [2, 3, 4, 5], [6, 7, 8, 9]])
        self.assertEqual(t1.get_rows([0, 2]).__str__(), '1 2 3 0\n6 7 8 9\n')

    def test_6(self):
        t1 = Table([[1, 2, 3], [2, 3, 4, 5], [6, 7, 8, 9]])
        t2 = Table([[1], [1, 9, 6, 9, 9], [5, 5, 5, 5], [0, 0, 6]])
        self.assertEqual(t1.merge_by_rows(t2).__str__(),
                         '1 2 3 0 0\n2 3 4 5 0\n6 7 8 9 0\n1 0 0 0 0\n1 9 6 9 9\n5 5 5 5 0\n0 0 6 0 0\n')

    def test_7(self):
        t1 = Table([[1, 2, 3], [2, 3, 4, 5], [6, 7, 8, 9]])
        t2 = Table([[1], [1, 9, 6, 9, 9], [5, 5, 5, 5], [0, 0, 6]])
        self.assertEqual(t1.merge_by_columns(t2).__str__(),
                         '1 2 3 0 1 0 0 0 0\n2 3 4 5 1 9 6 9 9\n6 7 8 9 5 5 5 5 0\n0 0 0 0 0 0 6 0 0\n')


if __name__ == '__main__':
    unittest.main()
