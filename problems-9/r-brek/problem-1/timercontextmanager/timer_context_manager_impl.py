from time import perf_counter
from sys import stdout

class Timer:
    def __init__(self, message_prefix=None, where_to_print=None):
        self._print_destination = where_to_print if where_to_print is not None else stdout
        self._message_prefix = message_prefix if message_prefix is not None else "Task"

    def __enter__(self):
        self._start_time = perf_counter()

    def __exit__(self, type, value, traceback):
        delta_time = perf_counter() - self._start_time
        print(f"{self._message_prefix} execution took {delta_time}", file=self._print_destination)
