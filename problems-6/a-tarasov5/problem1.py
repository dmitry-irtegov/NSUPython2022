import functools
import unittest


def cached(func):
    cache = {}

    @functools.wraps(func)
    def cached_func(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return cached_func


class CachedTest(unittest.TestCase):
    def setUp(self) -> None:
        CachedTest.var = 0

    var = 0

    @staticmethod
    @cached
    def dirty_func(num, *args, **kwargs):
        CachedTest.var += 1

    def test_cached(self):
        self.assertEqual(CachedTest.var, 0)
        CachedTest.dirty_func(5)
        self.assertEqual(CachedTest.var, 1)
        CachedTest.dirty_func(5)
        CachedTest.dirty_func(5)
        CachedTest.dirty_func(5)
        self.assertEqual(CachedTest.var, 1)

        CachedTest.dirty_func(6)
        self.assertEqual(CachedTest.var, 2)

    def test_args_kwargs(self):
        self.assertEqual(CachedTest.var, 0)
        CachedTest.dirty_func(5, 3, 4, name="string")
        self.assertEqual(CachedTest.var, 1)
        CachedTest.dirty_func(5, 3, 4, name="string")
        CachedTest.dirty_func(5, 3, 4, name="string")
        CachedTest.dirty_func(5, 3, 4, name="string")
        self.assertEqual(CachedTest.var, 1)
        CachedTest.dirty_func(5, 3, 3, name="string")
        self.assertEqual(CachedTest.var, 2)
        CachedTest.dirty_func(5, 3, 3, name="absolute_another_string")
        self.assertEqual(CachedTest.var, 3)
        CachedTest.dirty_func(5, 3, 4, name="string")
        self.assertEqual(CachedTest.var, 3)


if __name__ == "__main__":
    unittest.main()
