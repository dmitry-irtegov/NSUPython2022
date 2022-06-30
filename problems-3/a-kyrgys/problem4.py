class Cartesian:
    def __init__(self, n, els):
        self.elements = tuple(els)
        self.n = n
        self.i = 0  # [0 .. len(elements) ** n)

    # O(n)
    def get(self):
        a = self.i
        res = []
        for _ in range(self.n):
            res.append(self.elements[a % len(self.elements)])
            a //= len(self.elements)
        return res

    # O(1)
    def next(self):
        self.i = (self.i + 1) % (len(self.elements) ** self.n)




if __name__ == '__main__':
    c = Cartesian(3, [1, 'a'])
    for i in range(10):
        print(c.get())
        c.next()


