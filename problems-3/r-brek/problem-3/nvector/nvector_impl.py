import math

class NVector:
    def __init__(self, initial_value):
        if isinstance(initial_value, NVector):
            self._data = initial_value._data
            return
        if initial_value is not None:
            self._data = tuple(initial_value)
        else:
            self._data = ()

    def length(self):
        return math.sqrt(sum([x * x for x in self._data]))

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return f"NVector({self._data})"
    
    def __add__(self, other):
        if self.size() != other.size():
            raise ValueError("Can't sum vectors of different length")
        return NVector([x + y for x, y in zip(self._data, other._data)])

    def __sub__(self, other):
        if self.size() != other.size():
            raise ValueError("Can't sum vectors of different length")
        return NVector([x - y for x, y in zip(self._data, other._data)])

    def __mul__(self, other):
        "inner product or scalar multiplication depending on other type"
        if isinstance(other, NVector):
            if self.size() != other.size():
                raise ValueError("Can't get inner product of vectors of different dimensions")
            if self.size() == 0:
                return None
            return sum([x * y for x, y in zip(self._data, other._data)])
        # scalar case
        return NVector([x * other for x in self._data])

    def __xor__(self, other):
        "cross product"
        if len(self) != len(other) or len(self) != 3:
            raise ValueError("Cross product is only defined for 3D vectors")
        res = [self[1] * other[2] - self[2] * other[1],
               self[2] * other[0] - self[0] * other[2],
               self[0] * other[1] - self[1] * other[0]]
        return NVector(res)

    def __eq__(self, other):
        return self._data == other._data

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        "returns number of dimensions"
        return len(self._data)

    def size(self):
        return len(self)
