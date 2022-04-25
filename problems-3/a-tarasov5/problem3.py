import numbers
import unittest


class Vector:
    def __init__(self, value=None):
        if value is None:
            self._content = []
        else:
            try:
                self._content = list(iter(value))
            except TypeError as e:
                raise TypeError("You must provide an iterable object") from e

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You must provide an vector object")
        if len(other) != len(self):
            raise ValueError("Vectors must be the same size")
        return Vector([x + y for x, y in zip(self._content, other._content)])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You must provide an vector object")
        if len(other) != len(self):
            raise ValueError("Vectors must be the same size")

        return Vector([x - y for x, y in zip(self._content, other._content)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Can multiply vectors of different size")
            return Vector([x * y for x, y in zip(self._content, other._content)])
        elif isinstance(other, numbers.Number):
            return Vector([x * other for x in self._content])
        else:
            raise TypeError("You must provide an vector object or a numeric type")

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You must provide an vector object")
        return self._content == other._content

    def __getitem__(self, key):
        if not isinstance(key, numbers.Integral):
            raise TypeError("You must provide an number")
        if not 0 <= key < len(self._content):
            raise IndexError("Key must be less then size of vector and greater then zero")

        return self._content[key]

    def __setitem__(self, key, value):
        if not isinstance(key, numbers.Integral):
            raise TypeError("You must provide an number")
        if not 0 <= key < len(self._content):
            raise IndexError("Key must be less then size of vector and greater then zero")
        self._content[key] = value

    def __str__(self):
        return str(self._content)

    def __repr__(self):
        return f"Vector({self._content})"

    def __len__(self):
        return len(self._content)

    def __rmul__(self, other):
        return self.__mul__(other)

    def vector_len(self):
        return sum([x ** 2 for x in self._content]) ** .5


class VectorTest(unittest.TestCase):
    def test_init_errors(self):
        self.assertRaises(TypeError, Vector, 344)
        self.assertRaises(TypeError, Vector, VectorTest)

    def test_init(self):
        v1 = Vector(range(10))
        v2 = Vector(range(0, 10, -1))
        v3 = Vector([10] * 10)

    def test_bin_ops(self):
        v1 = Vector(range(10))
        v2 = Vector(range(9, -1, -1))
        v3 = Vector([9] * 10)
        self.assertEqual(v1 + v2, v3)
        self.assertNotEqual(v1 + v2, Vector([10] * 10))
        self.assertEqual(v1 * v2, Vector([0, 8, 14, 18, 20, 20, 18, 14, 8, 0]))
        self.assertEqual(v1 - v2, Vector([-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]))
        self.assertEqual(v3 * 3, Vector([27] * 10))
        self.assertEqual(3 * v3, Vector([27] * 10))
        self.assertEqual(3.3 * v3, Vector([29.7] * 10))

    def test_bin_ops_fail(self):
        v1 = Vector(range(10))
        v3 = Vector([9] * 10)
        self.assertRaises(TypeError, v3.__add__, v1, 3)
        self.assertRaises(TypeError, v3.__add__, 3, v1)
        self.assertRaises(ValueError, Vector.__add__, v1, Vector(range(11)))
        self.assertRaises(ValueError, Vector.__mul__, v1, Vector(range(11)))

    def test_unary_op(self):
        v1 = Vector([1, 2, 3, 4, 5, 4])
        self.assertEqual(len(v1), 6)
        v2 = Vector([1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(v2.vector_len(), 3)
        self.assertEqual((v2 * 2).vector_len(), 6)

    def test_access_fail(self):
        v1 = Vector([1, 2, 3, 4, 5, 4])
        self.assertRaises(IndexError, v1.__getitem__, 6)
        self.assertRaises(IndexError, v1.__setitem__, 6, 3)

    def test_access(self):
        v1 = Vector([1, 2, 3, 4, 5, 4])
        self.assertEqual(v1[0], 1)
        self.assertEqual(v1[5], 4)
        v1[0] = 444
        self.assertEqual(v1[0], 444)

    def test_repr(self):
        v1 = Vector(range(10))
        self.assertEqual(v1, eval(repr(v1)))

if __name__ == "__main__":
    unittest.main()
