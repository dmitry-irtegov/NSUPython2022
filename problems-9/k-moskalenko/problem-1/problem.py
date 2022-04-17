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
        self._start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = perf_counter()
        time = self.elapsed_time()
        print(f'Elapsed time: {time:.3f}s', file=self._file)

    def elapsed_time(self):
        """Returns the elapsed time of the previous timer usage."""
        if not (isinstance(self._start, float) and isinstance(self._end, float)):
            raise RuntimeError('The timer has not ended yet.')
        if self._start > self._end:
            raise RuntimeError('The start time is greater than the end time.')
        return self._end - self._start
