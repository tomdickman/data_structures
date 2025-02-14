from .Node import Node

class Stack:
    top: 'Node' = None
    height: int = 0

    def __init__(self, value: int = None):
        if value:
            self.top = Node(value)
            self.height = 1

    def print(self):
        current = self.top

        if not current:
            print('No nodes in stack')

        while current:
            print(current)
            current = current.next

    def push(self, value: int):
        if (not self.height) or (not self.top):
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node
        self.height += 1

        return self

    def pop(self):
        if (not self.height) or (not self.top):
            return None
        else:
            node = self.top
            self.top = self.top.next
            self.height -= 1
            return node
