import math


class NVector:
    def __init__(self, n_dim, initial_value=None):
        if n_dim < 0:
            raise ValueError("Can't have vector of n_dim < 0")
        if initial_value is not None:
            if len(initial_value) != n_dim:
                raise ValueError("initial_value len is not equal to n_dim")
            self._data = initial_value
        else:
            self._data = [0] * n_dim

    def get_dim(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return f"NVector({self.get_dim()}, {self._data})"
    
    def __add__(self, other):
        if self.get_dim() != other.get_dim():
            raise ValueError("Can't sum vectors of different length")
        return NVector(self.get_dim(), [x + y for x, y in zip(self._data, other._data)])

    def __sub__(self, other):
        if self.get_dim() != other.get_dim():
            raise ValueError("Can't sum vectors of different length")
        return NVector(self.get_dim(), [x - y for x, y in zip(self._data, other._data)])

    def __mul__(self, other):
        return NVector(self.get_dim(), [x * other for x in self._data])

    def __mod__(self, other):
        "inner product"
        if self.get_dim() != other.get_dim():
            raise ValueError("Can't get inner product of vectors of different length")
        if self.get_dim() == 0:
            return None
        return sum([x * y for x, y in zip(self._data, other._data)])

    def __eq__(self, other):
        if (self.get_dim() != other.get_dim()):
            return False
        return self._data == other._data

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return math.sqrt([x * x for x in self._data])

def simple_demo():
    v = NVector(3)
    print(f"v is {v}")
    u = NVector(3, [1, 2, 3])
    print(f"u is {u}")
    print(f"v + u is {v + u}")

    v = NVector(5, [-10, 2, 30, 40, 5])
    u = NVector(5, [5, 5, -5, 5, 5])
    print(f"u, v = {u}, {v}")
    print(f"u + v = {u + v}")

    print(f"v[1] == {v[1]}")

def run_set_of_tests_for_func(func, testing_data):
    for args, expected in testing_data:
        pretty_test(func, args, expected)

def pretty_test(func, args, expected):
    got = func(*args)
    passed = (got == expected)
    print(f"Expected function {func.__name__} on args {args} to be {expected}, got {got}")
    print(f"Test: {'OK' if passed else 'FAIL'}")

def run_tests():
    print("Testing sums")
    testing_data = [
        (
            (NVector(0), NVector(0),),
            NVector(0)
        ),
        (
            (NVector(3, [12, 13, 0]), NVector(3, [-12, 10, -1])),
            NVector(3, [0, 23, -1])
        ),
        (
            (NVector(4, [-1, -1, -2, 3]), NVector(4, [1, 1, 2, -3]),),
            NVector(4, [0, 0, 0, 0])
        )
    ]
    run_set_of_tests_for_func(lambda x, y: x + y, testing_data)
    print("Testing for sub")
    testing_data = [
        (
            (NVector(0), NVector(0),),
            NVector(0)
        ),
        (
            (NVector(3, [12, 13, 0]), NVector(3, [-12, 10, -1])),
            NVector(3, [24, 3, 1])
        ),
        (
            (NVector(4, [-1, -1, -2, 3]), NVector(4, [1, 1, 2, -3]),),
            NVector(4, [-2, -2, -4, 6])
        )
    ]
    run_set_of_tests_for_func(lambda x, y: x - y, testing_data)
    testing_data = [
        (
            (NVector(0), 3),
            NVector(0)
        ),
        (
            (NVector(3, [12, 13, 0]), -1),
            NVector(3, [-12, -13, 0])
        ),
        (
            (NVector(4, [-1, -1, -2, 3]), 10),
            NVector(4, [-10, -10, -20, 30])
        )
    ]
    run_set_of_tests_for_func(lambda x, y: x * y, testing_data)
    testing_data = [
        (
            (NVector(0), NVector(0)),
            None
        ),
        (
            (NVector(3, [12, 13, 0]), NVector(3, [10, 15, 0])),
            12*10 + 13*15 + 0
        ),
        (
            (NVector(4, [-1, -1, -2, 3]), NVector(4, [20, 0, 0, -1])),
            -1*20 + -1*0 + -1*0 + 3*-1
        )
    ]
    run_set_of_tests_for_func(lambda x, y: x % y, testing_data)

if __name__ == '__main__':
    simple_demo()
    run_tests()
    
