from time import perf_counter


class Timer:
    """Class for timing execution speed of code snippets.

    Typical use::

        with Timer():
            do_some_long_stuff()
    """

    def __init__(self, file=None):
        """Creates a timer instance.

        :param file: A file-like object (stream) used to print the
        elapsed time message; defaults to the current sys.stdout.
        """
        self._file = file

    def __enter__(self):
        if hasattr(self, '_end'):
            delattr(self, '_end')
        self._start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = perf_counter()
        time = self.elapsed_time()
        print(f'Elapsed time: {time:.3f}s', file=self._file)

    def elapsed_time(self):
        """Returns the elapsed time of the previous timer usage."""
        if not hasattr(self, '_start'):
            raise RuntimeError('The timer has not been started yet.')

        start = self._start
        end = self._end if hasattr(self, '_end') else perf_counter()

        if start > end:
            raise RuntimeError('The start time is greater than the end time.')

        return end - start
