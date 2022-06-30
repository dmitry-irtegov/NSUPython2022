import unittest
from problem4 import Cartesian

class MyTestCase(unittest.TestCase):

    def test_1_is_cycled(self):
        c = Cartesian(2, [1, 'a'])
        t1 = c.get()
        for _ in range(4):
            c.next()
        t2 = c.get()
        self.assertEqual(t1, t2)

    def test_2_is_cycled(self):
        c = Cartesian(3, [1, 'a'])
        t1 = c.get()
        for _ in range(2**3):
            c.next()
        t2 = c.get()
        self.assertEqual(t1, t2)

    def test_3_is_cycled(self):
        c = Cartesian(4, [1, 'a', 2, 'qew'])
        t1 = c.get()
        for _ in range(4**4):
            c.next()
        t2 = c.get()
        self.assertEqual(t1, t2)

    def test_4_is_unique(self):
        c = Cartesian(2, [1, 'a'])
        t1 = c.get()
        for _ in range(3):
            c.next()
            t2 = c.get()
            self.assertNotEqual(t1, t2)

    def test_5_is_unique(self):
        c = Cartesian(4, [1, 'a', 2, 'qew'])
        t1 = c.get()
        for _ in range(4**4-1):
            c.next()
            t2 = c.get()
            self.assertNotEqual(t1, t2)


    def test_6_one(self):
        c = Cartesian(1, [1])
        t1 = c.get()
        for _ in range(4**4-1):
            c.next()
            t2 = c.get()
            self.assertEqual(t1, t2)




if __name__ == '__main__':
    unittest.main()