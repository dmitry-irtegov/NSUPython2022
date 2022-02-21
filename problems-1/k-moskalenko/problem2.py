def trim_values(nums, a, b):
    """
    Replaces all numbers less than `a` with `a`, and all numbers greater than `b` with `b`.

    :param nums: The input list of numbers
    :param a: The lower bound
    :param b: The upper bound
    """

    if a > b:
        raise ValueError('The lower bound must be less than or equal to the upper bound.')

    for i, num in enumerate(nums):
        if num < a:
            nums[i] = a
        if num > b:
            nums[i] = b


if __name__ == '__main__':
    in_str = input('Enter a sequence of numbers: ')
    lb = int(input('Enter the lower bound: '))
    ub = int(input('Enter the upper bound: '))

    numbers = list(map(int, in_str.split()))
    trim_values(numbers, lb, ub)

    print('Result:', numbers)
