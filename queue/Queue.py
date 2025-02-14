from .Node import Node

class Queue:
    first: 'Node' = None
    last: 'Node' = None
    length: int = 0

    def __init__(self, value: int = None):
        if value != None:
            node = Node(value)
            self.first = node
            self.last = node
            self.length = 1

    def enqueue(self, value: int):
        node = Node(value)
        if (not self.length) or (not self.first):
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

        return self

    def dequeue(self):
        if (not self.length) or (not self.first):
            return None
        else:
            node = self.first
            if (self.length == 1) or (not self.first.next):
                self.last = None
            self.first = self.first.next
            self.length -= 1
            return node
