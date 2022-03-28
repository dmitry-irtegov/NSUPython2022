import unittest
from .nvector_impl import NVector

class TestNVector(unittest.TestCase):
    def test_constructor_sanity(self):
        NVector([1])
        NVector([])
        NVector(())
        NVector(["Different Type", int, lambda x: x, {}])
        NVector(initial_value=None)
        NVector((x for x in range(10)))

    def test_dim(self):
        self.assertEqual(
            3,
            len(NVector([0, 0, 0]))
        )
        self.assertEqual(
            5,
            NVector([0, 0, 0, 0, 0]).size()
        )
        self.assertEqual(
            0,
            NVector([]).size()
        )
    
    def test_get(self):
        self.assertEqual(
            1,
            NVector([0, 0, 0, 1, 0])[3]
        )
        with self.assertRaises(IndexError):
            NVector([])[10]
        with self.assertRaises(IndexError):
            NVector([0, 1, 2])[3]
        
    def test_sums(self):
        self.assertEqual(
            NVector([0]),
            NVector([0]) + NVector([0])
        )
        self.assertEqual(
            NVector([0, 23, -1]),
            NVector([12, 13, 0]) + NVector([-12, 10, -1])
        )
        self.assertEqual(
            NVector([0, 0, 0, 0]),
            NVector([-1, -1, -2, 3]) + NVector([1, 1, 2, -3])
        )
        u = NVector([9, 8, 7])
        v = NVector([23, 4, 5])
        self.assertEqual(
            u + v,
            v + u
        )
        with self.assertRaises(ValueError):
            u = NVector([1])
            v = NVector([1, 2, 3])
            u + v
        
    def test_sub(self):
        self.assertEqual(
            NVector([0]),
            NVector([0]) - NVector([0])
        )
        self.assertEqual(
            NVector([24, 3, 1]),
            NVector([12, 13, 0]) - NVector([-12, 10, -1])
        )
        self.assertEqual(
            NVector([-2, -2, -4, 6]),
            NVector([-1, -1, -2, 3]) - NVector([1, 1, 2, -3])
        )
        with self.assertRaises(ValueError):
            u = NVector([1])
            v = NVector([1, 2, 3])
            u - v
    
    def test_scalar_product(self):
        self.assertEqual(
            NVector([0]),
            NVector([0]) * 3
        )
        self.assertEqual(
                NVector([-12, -13, 0]),
                NVector([12, 13, 0]) * -1
        )
        self.assertEqual(
            NVector([-10, -10, -20, 30]),
            NVector([-1, -1, -2, 3]) * 10
        )
    
    def test_dot_product(self):
        self.assertEqual(
            None,
            NVector([]) * NVector([])
        )
        self.assertEqual(
            12*10 + 13*15 + 0,
            NVector([12, 13, 0]) * NVector([10, 15, 0])
        )
        self.assertEqual(
            -1*20 + -1*0 + -1*0 + 3*-1,
            NVector([-1, -1, -2, 3]) * NVector([20, 0, 0, -1])
        )

        with self.assertRaises(ValueError):
            u = NVector([1])
            v = NVector([1, 2, 3])
            u * v

    def test_eq(self):
        u = NVector([1])
        v1 = NVector([2])
        v2 = NVector([1, 2])

        self.assertNotEqual(u, v1)
        self.assertNotEqual(u, v2)

        s = "Some other type"
        u = NVector([s])
        v = NVector([s])
        self.assertEqual(u, v)

    def test_len(self):
        self.assertAlmostEqual(
            1.414,
            NVector([1, 1]).length(),
            3
        )

    def test_cross_product(self):
        v = NVector([1, 2, 3])
        u = NVector([3, 4, 5])
        self.assertEqual(
            NVector([2, -4, 2]),
            u ^ v
        )
        with self.assertRaises(ValueError):
            u = NVector([2])
            v = NVector([3, 4, 5])
            u ^ v

if __name__ == "__main__":
    unittest.main()
