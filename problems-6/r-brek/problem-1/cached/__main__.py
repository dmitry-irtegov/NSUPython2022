import unittest
from .cached_impl import cached

class CachedTest(unittest.TestCase):
    def test_cached_same_results(self):

        payload_function = lambda x: x + 1

        @cached
        def some_function(x):
            return x + 1

        for arg in range(100):
            self.assertEqual(
                payload_function(arg),
                some_function(arg)
            )

    def test_different_args(self):
        
        @cached
        def some_function(*args, **kwargs):
            return ' '.join(map(str, args)) + ';' + ' '.join(map(str, kwargs.items()))

        expectedAnswer = "1 2 3;('one', 'two') ('three', 'four')"

        self.assertEqual(
            expectedAnswer,
            some_function('1', '2', '3', one='two', three='four')
        )

        self.assertEqual(
            expectedAnswer,
            some_function('1', '2', '3', three='four', one='two')
        )

if __name__ == "__main__":
    unittest.main()
