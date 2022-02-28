def cum_sum(input):
    res = [0]
    for x in input:
        last = res[-1]
        res.append(x + last)
    return res

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
            ([1,2,3,4,5], ),
            [0, 1, 3, 6, 10, 15]
        ),
        (
            ([10, 10, 10, 11, 12, 13, 0], ),
            [0, 10, 20, 30, 41, 53, 66, 66]
        ),
        (
            ([0 for _ in range(100)], ),
            [0 for _ in range(101)]
        )
    ]
    run_set_of_tests_for_func(cum_sum, testing_data)
