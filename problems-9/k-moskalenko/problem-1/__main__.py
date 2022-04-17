import unittest
from time import sleep
from io import StringIO
from .problem import Timer


class TimerTestCase(unittest.TestCase):
    def test_sleep(self):
        t = Timer()
        sleep_time = 0.75

        with t:
            sleep(sleep_time)

        self.assertAlmostEqual(t.elapsed_time(), sleep_time, places=2)

    def test_print(self):
        stream = StringIO()
        with Timer(file=stream):
            sleep(1)

        regex = r'^Elapsed time: 1\.\d{3}s$'
        self.assertRegex(stream.getvalue(), regex)

    def test_exception(self):
        with self.assertRaises(RuntimeError):
            with Timer():
                sleep(0.5)
                raise RuntimeError()


if __name__ == '__main__':
    unittest.main()
