import unittest
from problem3 import Vector


class MyTestCase(unittest.TestCase):
    def test_1(self):
        v1 = Vector([1, 2, 3])
        self.assertEqual(v1.__str__(), '(1, 2, 3)')

    def test_2(self):
        v1 = Vector([4, 3])
        self.assertEqual(v1.length(), 5)

    def test_3(self):
        v1 = Vector([4, 3, 10, 11, 54, 1, 20])
        self.assertEqual(v1.__getitem__(4), 54)

    def test_3_with_exception(self):
        v1 = Vector([4, 3, 10, 11, 54])
        with self.assertRaises(IndexError):
            v1.__getitem__(5)

    def test_4(self):
        v1 = Vector([4, 3, 10, 11, 54, 1, 20])
        self.assertEqual(v1.multiply_by_scalar(10).__str__(), '(40, 30, 100, 110, 540, 10, 200)')

    def test_5(self):
        v1 = Vector([4, 3, 10, 11, 54, 1, 20])
        v2 = Vector([4, 3, 2, 1, 0, 4, 70])
        self.assertEqual(v1.__eq__(v2), False)

    def test_6(self):
        v1 = Vector([4, 3, 10, 11, 54, 1, 20])
        v2 = Vector([4, 3, 2, 1, 0, 4, 70])
        self.assertEqual(v1.__add__(v2).__str__(), '(8, 6, 12, 12, 54, 5, 90)')

    def test_6_different_number_of_components(self):
        v1 = Vector([4, 3, 10, 11, 54, 1, 20, 5])
        v2 = Vector([4, 3, 2, 1, 0, 4, 70])
        with self.assertRaises(IndexError):
            v1.__add__(v2)


    def test_7(self):
        v1 = Vector([9, 4, 7, 8])
        v2 = Vector([5, 10, 1, 6])
        self.assertEqual(v1.__mul__(v2), 140)

    def test_7_different_number_of_components(self):
        v1 = Vector([4, 3, 10, 5])
        v2 = Vector([4, 70])
        with self.assertRaises(IndexError):
            v1.__mul__(v2)


if __name__ == '__main__':
    unittest.main()
