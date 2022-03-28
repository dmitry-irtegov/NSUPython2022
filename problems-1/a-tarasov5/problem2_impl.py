import unittest


def trim_nums(l, l_bound, up_bound):
    """
    Return list where every element less than l_bound turns into l_bound
    and every element greate than u_bound turns into u_bound
    :param l: list to transform
    :param l_bound: lower bound
    :param up_bound: upper bound
    :return: transformed list
    """
    if l_bound > up_bound:
        raise ValueError("Lower bound cannot be greater then upper")
    lowed_result = map(lambda x: l_bound if x < l_bound else x, l)
    result = list(map(lambda x: up_bound if x > up_bound else x, lowed_result))
    return result


class TestTrimNums(unittest.TestCase):
    def test_simple(self):
        self.assertListEqual(trim_nums([1, 2, 3, 4, 5, 6, 7], 3, 5), [3, 3, 3, 4, 5, 5, 5])
        self.assertListEqual(trim_nums([9, 9, 9, 9, 9, 9, 9], 3.2, 8.8), [8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8])
        self.assertListEqual(trim_nums([], 3.2, 8.8), [])
        self.assertListEqual(trim_nums(range(10), 4, 6), [4, 4, 4, 4, 4, 5, 6, 6, 6, 6])
        self.assertListEqual(trim_nums(["1", "3", "3", "333", "4", "5", "7"], "4", "6"), ["4", "4", "4", "4", "4", "5", "6"])

    def test_errors(self):
        self.assertRaises(ValueError, trim_nums, [1, 5, 6], 4, 3.9)
        self.assertRaises(TypeError, trim_nums, [1, 5, ""], 4, 9)
        self.assertRaises(TypeError, trim_nums, None, 4, 9)
        self.assertRaises(TypeError, trim_nums, [1, 2, 3, 4], "asss", 9)


if __name__ == "__main__":
    unittest.main()
