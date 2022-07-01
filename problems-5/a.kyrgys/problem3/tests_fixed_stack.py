import unittest
from fixed_stack import FixedStack

class StackTest(unittest.TestCase):

    def test_init_fixed(self):
        stack = FixedStack()
        self.assertEqual(stack.elements, [])

        stack = FixedStack([1, 2, 3])
        self.assertEqual(stack.elements, [1, 2, 3])

    def test_pop_fixed(self):
        stack = FixedStack([1, 2, 3])
        stack.push(4)
        self.assertEqual(stack.elements, [1, 2, 3, 4])
        stack.pop()
        self.assertEqual(stack.elements, [1, 2, 3])

    def test_push_fixed(self):
        stack = FixedStack()
        stack.push(1)
        self.assertEqual(stack.elements, [1])
        stack.push(2)
        self.assertEqual(stack.elements, [1, 2])
        stack = FixedStack()
        self.assertEqual(stack.elements, [])




if __name__ == '__main__':
    unittest.main()
