import unittest

from linkedlist.LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_construct(self):
        list = LinkedList(3)
        self.assertEqual(list.head.value, 3)
        self.assertEqual(list.tail.value, 3)
        self.assertEqual(list.length, 1)

    def test_construct_no_value(self):
        list = LinkedList()
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)
        self.assertEqual(list.length, 0)

    def test_find_middle_node_exists(self):
        list = LinkedList()
        list.append(3)
        list.append(4)
        list.append(5)

        self.assertEqual(list.find_middle_node().value, 4)

    def test_find_middle_node_none(self):
        list = LinkedList(3).append(4)

        self.assertEqual(list.find_middle_node(), False)


    def test_find_middle_node_single_node(self):
        list = LinkedList(3)

        self.assertEqual(list.find_middle_node().value, 3)

    def test_find_middle_node_empty(self):
        list = LinkedList(None)

        self.assertEqual(list.find_middle_node(), False)

    def test_has_loop(self):
        list = LinkedList(1).append(2).append(3).append(4)
        list.tail.next = list.head

        self.assertTrue(list.has_loop())

    def test_has_loop_no_loop(self):
        list = LinkedList(1).append(2).append(3).append(4)

        self.assertFalse(list.has_loop())

    def test_find_kth_from_end(self):
        list = LinkedList(1)
        list.append(2)
        list.append(3)
        list.append(4)

        self.assertEqual(list.find_kth_from_end(1).value, 4)
        self.assertEqual(list.find_kth_from_end(2).value, 3)

    def test_find_kth_from_end_equal_to_length(self):
        list = LinkedList(1).append(2).append(3).append(4)
        self.assertEqual(list.find_kth_from_end(4).value, 1)

    def test_partition_list(self):
        list = LinkedList(2).append(5).append(4).append(3).append(1)
        actualList = list.partition_list(3)
        expectedList = LinkedList(2).append(1).append(3).append(5).append(4)

        actualNode = actualList.head
        expectedNode = expectedList.head

        while (actualNode != None) and (expectedNode != None):
            self.assertEqual(actualNode.value, expectedNode.value)
            actualNode = actualNode.next
            expectedNode = expectedNode.next

    def test_partition_list_empty(self):
        self.assertIsNone(LinkedList().partition_list(3))

    def test_remove_duplicates(self):
        list = LinkedList(1).append(1).append(2).append(3).append(1).append(1)
        list.remove_duplicates()
        self.assertEqual(list.head.value, 1)
        self.assertEqual(list.head.next.value, 2)
        self.assertEqual(list.tail.value, 3)
        self.assertEqual(list.length, 3)

    def test_remove_duplicates_empty(self):
        list = LinkedList()
        list.remove_duplicates()
        self.assertEqual(list.length, 0)

    def test_binary_to_decimal(self):
        list = LinkedList(1).append(1).append(1)
        result = list.binary_to_decimal()
        self.assertEqual(result, 7)

    def test_reverse_between(self):
        list = LinkedList(1).append(2).append(3).append(4).append(5)
        result = list.reverse_between(1, 3)
        self.assertEqual(result.head.value, 1)
        self.assertEqual(result.head.next.value, 4)
        self.assertEqual(result.head.next.next.value, 3)
        self.assertEqual(result.head.next.next.next.value, 2)
        self.assertEqual(result.tail.value, 5)

    def test_reverse_between_including_head(self):
        list = LinkedList(1).append(2).append(3).append(4).append(5)
        result = list.reverse_between(0, 3)
        self.assertEqual(result.head.value, 4)
        self.assertEqual(result.head.next.value, 3)
        self.assertEqual(result.tail.value, 5)

    def test_reverse_between_including_head_and_tail(self):
        list = LinkedList(1).append(2).append(3).append(4).append(5)
        result = list.reverse_between(0, 4)
        self.assertEqual(result.head.value, 5)
        self.assertEqual(result.tail.value, 1)

if __name__ == '__main__':
    unittest.main()
