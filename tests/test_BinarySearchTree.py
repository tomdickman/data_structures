import unittest

from binarysearchtree.BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def test_insert_no_root(self):
        sut = BinarySearchTree()
        sut.insert(3)
        self.assertEqual(sut.root.value, 3)

    def test_insert_duplicate(self):
        sut = BinarySearchTree(3)

        with self.assertRaises(ValueError) as context:
            sut.insert(3)

        self.assertEqual(str(context.exception), "Cannot insert duplicate value")

    def test_insert_less_than_root(self):
        sut = BinarySearchTree(7)
        sut.insert(3)
        self.assertEqual(sut.root.left.value, 3)
        self.assertIsNone(sut.root.right)

    def test_insert_greater_than_root(self):
        sut = BinarySearchTree(3)
        sut.insert(7)
        self.assertEqual(sut.root.right.value, 7)
        self.assertIsNone(sut.root.left)

    def test_insert_less_than_child(self):
        sut = BinarySearchTree(4)
        sut.insert(3).insert(2)
        self.assertEqual(sut.root.left.left.value, 2)
        self.assertIsNone(sut.root.left.right)

    def test_insert_greater_than_child(self):
        sut = BinarySearchTree(70)
        sut.insert(45).insert(50)

        '''
        Expected result

                70
              /
             45
               \
               50

        '''

        self.assertEqual(sut.root.left.value, 45)
        self.assertEqual(sut.root.left.right.value, 50)

    def test_contains(self):
        sut = (
            BinarySearchTree(33)
            .insert(45)
            .insert(42)
            .insert(49)
            .insert(15)
            .insert(7)
            .insert(28)
        )

        self.assertTrue(sut.contains(28))
        self.assertFalse(sut.contains(31))

    def test_delete_root(self):
        sut = BinarySearchTree(27)
        sut.delete(27)
        self.assertIsNone(sut.root)
        self.assertFalse(sut.contains(27))

    def test_delete(self):
        sut = (
            BinarySearchTree(77)
            .insert(21)
            .insert(95)
            .insert(14)
            .insert(25)
            .insert(88)
            .insert(107)
            .insert(22)
            .insert(27)
        )

        '''
        Before:
                    77
                  /    \
                21      95
               /  \    /  \
              14  25  88  107
                 /  \
                22  27
        After:
                    77
                  /    \
                22      95
               /  \    /  \
              14  25  88  107
                    \
                    27
        '''
        sut.delete(21)

        self.assertEqual(sut.root.left.value, 22)
        self.assertEqual(sut.root.left.right.value, 25)
        self.assertEqual(sut.root.left.right.right.value, 27)
        self.assertIsNone(sut.root.left.right.left)

if __name__ == "__main__":
    unittest.main()
