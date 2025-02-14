import unittest

from doublylinkedlist.DoublyLinkedList import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_construct(self):
        list = DoublyLinkedList(3)
        self.assertEqual(list.head.value, 3)
        self.assertEqual(list.tail.value, 3)
        self.assertEqual(list.length, 1)

    def test_construct_no_value(self):
        list = DoublyLinkedList()
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)
        self.assertEqual(list.length, 0)

    def test_append(self):
        list = DoublyLinkedList()
        result = list.append(5).append(3)
        self.assertEqual(list, result)
        self.assertEqual(list.head.value, 5)
        self.assertEqual(list.tail.value, 3)
        self.assertEqual(list.length, 2)

    def test_append_single_node(self):
        list = DoublyLinkedList(1)
        result = list.append(5)
        self.assertEqual(result.head.value, 1)
        self.assertEqual(result.head.next.value, 5)
        self.assertEqual(result.tail.value, 5)
        self.assertEqual(result.tail.prev.value, 1)
        self.assertEqual(result.length, 2)

    def test_pop_empty(self):
        list = DoublyLinkedList()
        self.assertIsNone(list.pop())

    def test_pop_single_node(self):
        list = DoublyLinkedList(7)
        result = list.pop()
        self.assertEqual(list.length, 0)
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)
        self.assertEqual(result.value, 7)

    def test_pop(self):
        list = DoublyLinkedList(1).append(2).append(3)
        result = list.pop()
        self.assertEqual(result.value, 3)
        self.assertIsNone(result.prev)
        self.assertEqual(list.tail.value, 2)
        self.assertIsNone(list.tail.next)
        self.assertEqual(list.length, 2)

    def test_prepend_empty_list(self):
        list = DoublyLinkedList()
        result = list.prepend(5)
        self.assertEqual(result.head.value, 5)
        self.assertIsNone(result.head.next)
        self.assertEqual(result.tail, result.head)
        self.assertEqual(result.length, 1)

    def test_prepend_single_node_list(self):
        list = DoublyLinkedList(1)
        result = list.prepend(5)
        self.assertEqual(result.head.value, 5)
        self.assertEqual(result.head.next.value, 1)
        self.assertEqual(result.tail.value, 1)
        self.assertEqual(result.tail.prev.value, 5)
        self.assertEqual(result.length, 2)

    def test_pop_first_empty_list(self):
        list = DoublyLinkedList()
        self.assertIsNone(list.pop_first())

    def test_pop_first_single_node(self):
        list = DoublyLinkedList(4)
        result = list.pop_first()
        self.assertEqual(result.value, 4)
        self.assertEqual(list.length, 0)
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)

    def test_get_out_of_bounds(self):
        list = DoublyLinkedList(33)
        self.assertIsNone(list.get(-4))
        self.assertIsNone(list.get(1))

    def test_get_odd_number_nodes(self):
        list = DoublyLinkedList(3).append(55).append(6).append(44).append(9)
        self.assertEqual(list.get(0).value, 3)
        self.assertEqual(list.get(1).value, 55)
        self.assertEqual(list.get(3).value, 44)
        self.assertEqual(list.get(4).value, 9)

    def test_insert_out_of_bounds(self):
        list = DoublyLinkedList(3)
        self.assertFalse(list.insert(-4, 5))
        self.assertFalse(list.insert(5, 5))

    def test_insert_head(self):
        list = DoublyLinkedList(3)
        result = list.insert(0, 99)
        self.assertTrue(result)
        self.assertEqual(list.head.value, 99)

    def test_insert_tail(self):
        list = DoublyLinkedList(3)
        result = list.insert(1, 99)
        self.assertTrue(result)
        self.assertEqual(list.tail.value, 99)

    def test_insert(self):
        list = DoublyLinkedList(1).append(2).append(3)
        result = list.insert(1, 4)
        self.assertTrue(result)
        self.assertEqual(list.length, 4)
        self.assertEqual(list.head.value, 1)
        self.assertEqual(list.head.next.value, 4)

    def test_remove_empty_list(self):
        list = DoublyLinkedList()
        self.assertFalse(list.remove(0))

    def test_remove_single_node(self):
        list = DoublyLinkedList(3)
        result = list.remove(0)
        self.assertEqual(result.value, 3)
        self.assertEqual(list.length, 0)
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)

    def test_remove_last_node(self):
        list = DoublyLinkedList(1).append(2).append(3)
        result = list.remove(2)
        self.assertEqual(result.value, 3)
        self.assertEqual(list.length, 2)
        self.assertEqual(list.tail.value, 2)
        self.assertIsNone(list.tail.next)

if __name__ == '__main__':
    unittest.main()
