import unittest

from stack import Stack

class StackTest(unittest.TestCase):

    def test_init(self):
        mystack = Stack()
        self.assertEqual(mystack.elements, [])

        mystack = Stack([1, 2, 3])
        self.assertEqual(mystack.elements, [1, 2, 3])

    def test_pop(self):
        mystack = Stack([1, 2, 3])
        mystack.push(4)
        self.assertEqual(mystack.elements, [1, 2, 3, 4])
        mystack.pop()
        self.assertEqual(mystack.elements, [1, 2, 3])


    #так как при измении значения elements, изменяется его значение по умолчанию, то
    #при создании нового стэка, он не будет пустым
    def test_push(self):
        mystack = Stack()
        mystack.push(1)
        self.assertEqual(mystack.elements, [1])
        mystack.push(2)
        self.assertEqual(mystack.elements, [1, 2])
        mystack = Stack()
        self.assertEqual(mystack.elements, [])


if __name__ == '__main__':
    unittest.main()
