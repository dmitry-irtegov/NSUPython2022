class FixedStack(object):
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        return self.elements.pop()

    def __len__(self):
        return len(self.elements)