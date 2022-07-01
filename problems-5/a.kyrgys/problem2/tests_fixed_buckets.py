from fixed_buckets import FixedBuckets
import unittest



class TestBuckets(unittest.TestCase):

    def test_init_fixed_buckets(self):
        mybucket = FixedBuckets(4, 2)
        self.assertEqual(mybucket.buckets, [2, 2, 2, 2])

        mybucket = FixedBuckets(4, [])

        self.assertEqual(mybucket.buckets, [[], [], [], []])

    def test_add_fixed_buckets(self):
        mybucket = FixedBuckets(5, [])
        mybucket.add(0, 1)
        self.assertEqual(mybucket.buckets, [[1], [], [], [], []])
        mybucket.add(1, 4)
        self.assertEqual(mybucket.buckets, [[1], [14], [], [], []])
        mybucket.add(4, 9)
        self.assertEqual(mybucket.buckets, [[1], [14], [], [], [28]])

    def test_clear_fixed_buckets(self):
        mybucket = FixedBuckets(5, [])
        mybucket.add(0, 1)
        mybucket.add(1, 4)
        mybucket.add(4, 9)
        mybucket.clear(1)
        mybucket.clear(4)
        self.assertEqual(mybucket.buckets, [[1], [], [], [], []])
        mybucket.add(4, 9)
        self.assertEqual(mybucket.find(0, 1), True)
        self.assertEqual(mybucket.find(4, 90), False)


if __name__ == '__main__':
    unittest.main()
