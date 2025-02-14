import unittest

from linkedlist.LinkedListNoLength import LinkedListNoLength

class TestLinkedListNoLengthMethods(unittest.TestCase):
    def test_append(self):
        list = LinkedListNoLength(3)
        list.append(4)

        self.assertEqual(list.tail.value, 4)

if __name__ == '__main__':
    unittest.main()
