def cut(input, upper_limit, lower_limit):
    if upper_limit < lower_limit:
        raise ValueError("upper limit less then lower limit")
    def susbtitute(x):
        if x > upper_limit:
            return upper_limit
        if x < lower_limit:
            return lower_limit
        return x
    return [susbtitute(x) for x in input]

def run_set_of_tests_for_func(func, testing_data):
    for args, expected in testing_data:
        pretty_test(func, args, expected)

def pretty_test(func, args, expected):
    got = func(*args)
    passed = (got == expected)
    print(f"Expected function {func.__name__} on args {args} to be {expected}, got {got}")
    print(f"Test: {'OK' if passed else 'FAIL'}")

if __name__ == '__main__':
    testing_data = [
        (
            ([1, 2, 3, 4, 5, 4, 3, 2, 1], 4, 2),
            [2,2,3,4,4,4,3,2,2]
        ),
        (
            ([100 for _ in range(100)], 1000, 30),
            [100 for _ in range(100)]
        )
    ]
    run_set_of_tests_for_func(cut, testing_data)
