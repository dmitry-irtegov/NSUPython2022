from .timer_context_manager_impl import Timer
import sys
from time import sleep

def main():
    print("Timer context manager showcase")
    print("Sleeping 2 seconds with Timer to stdout")

    with Timer():
        sleep(2)

    print("Sleeping 2 seconds with Timer to stderr")
    with Timer(where_to_print=sys.stderr):
        sleep(2)

    print("Measuring time to sum all numbers from 0 to 100000")
    with Timer(message_prefix="Summing all numbers from 0 to 100000"):
        s = 0
        for x in range(0, 100001):
            s += x
        print(f"Result is {s}")
    

if __name__ == "__main__":
    main()
