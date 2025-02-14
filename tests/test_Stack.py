import unittest

from stack.Stack import Stack

class TestStack(unittest.TestCase):
    def test_push_empty(self):
        stack = Stack()
        result = stack.push(3)
        self.assertEqual(result, stack)
        self.assertEqual(stack.top.value, 3)
        self.assertEqual(stack.height, 1)

    def test_push(self):
        stack = Stack()
        result = stack.push(3).push(4)
        self.assertEqual(result, stack)
        self.assertEqual(stack.top.value, 4)
        self.assertEqual(stack.height, 2)
