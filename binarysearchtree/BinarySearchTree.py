from .Node import Node

class BinarySearchTree:
    root: 'Node' = None

    def __init__(self, value: int = None):
        if value != None:
            self.root = Node(value)

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return self

        current = self.root
        while current:
            if value == current.value:
                raise(ValueError('Cannot insert duplicate value'))
            if value < current.value:
                if not current.left:
                    current.left = node
                    return self
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = node
                    return self
                else:
                    current = current.right

    def contains(self, value):
        if not self.root:
            return False

        current = self.root

        while current:
            if value == current.value:
                return True
            elif  value < current.value:
                current = current.left
            else:
                current = current.right

        return False
