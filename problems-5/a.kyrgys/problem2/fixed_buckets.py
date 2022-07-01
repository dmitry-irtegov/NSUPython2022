import copy

class FixedBuckets(object):
    def __init__(self, length, default):
        self.buckets = []
        for _ in range(length):
            self.buckets.append(copy.copy(default))
        self.default = copy.copy(default)


    def add(self, index, element):
        self.buckets[index].append(element)

    def find(self, index, element):
        return element in self.buckets[index]

    def clear(self, index):
        self.buckets[index] = copy.copy(self.default)
