import math

# solution
def primesTilX(x):
    return [x for x in range(2, x) if all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))]

def run_set_of_tests_for_func(func, testing_data):
    for args, expected in testing_data:
        pretty_test(func, args, expected)

def pretty_test(func, args, expected):
    got = func(*args)
    passed = (got == expected)
    print(f"Expected function {func.__name__} on args {args} to be {expected}, got {got}")
    print(f"Test: {'OK' if passed else 'FAIL'}")

if __name__ == '__main__':
    args = (300,)
    # primes till 300
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
    pretty_test(primesTilX, args, expected)
