from buckets import Buckets
import unittest



class TestBuckets(unittest.TestCase):

    def test_init(self):
        mybucket1 = Buckets(7, 0)
        self.assertEqual(mybucket1.buckets, [0, 0, 0, 0, 0, 0, 0])

        mybucket2 = Buckets(3, [])
        self.assertEqual(mybucket2.buckets, [[], [], []])


    #в данном случае тест не проходит, так как все списки саязана и получается,
    #что при добавлении в один список остальные списки тоже изменяются
    def test_add(self):
        mybucket = Buckets(5, [1])
        mybucket.add(2, 3)
        self.assertEqual(mybucket.buckets, [[1], [1], [1, 3], [1], [1]])

    #данный тест подтверждает тот факт, что при добавлении элмента в один список,
    #в остальные списки элемент тоже добавляется
    def test_add_check(self):
        mybucket = Buckets(4 [1])
        mybucket.add(2, 3)
        self.assertEqual(mybucket.buckets, [[1, 3], [1, 3], [1, 3], [1, 3]])

    def test_find(self):
        mybucket = Buckets(5, [])
        mybucket.add(1, 1)
        mybucket.add(1, 2)
        self.assertNotEqual(mybucket.find(0, 1), False)
        self.assertNotEqual(mybucket.find(0, 2), False)

    #так как значение default изменяется при добавлении в корзину элементов
    #и при очистке, корзине присвается ссылка на default, а не его значение
    #то он добавиться в очищенную корзину
    def test_clear(self):
        mybucket = Buckets(4, [])
        mybucket.add(1, 5)
        mybucket.add(1, 6)
        mybucket.clear(1)
        self.assertEqual(mybucket.buckets, [[5, 6], [], [5, 6], [5, 6]])

    def test_clear_check(self):
        mybucket = Buckets(4, [])
        mybucket.add(1, 5)
        mybucket.add(1, 6)
        mybucket.clear(1)
        self.assertEqual(mybucket.buckets, [[5, 6], [5, 6], [5, 6], [5, 6]])


if __name__ == '__main__':
    unittest.main()
