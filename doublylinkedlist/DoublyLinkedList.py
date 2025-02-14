from .Node import Node

class DoublyLinkedList:
    length: int = 0
    head: Node = None
    tail: Node = None

    def __init__(self, value = None):
        if value:
            self.append(value)

    def append(self, value: int):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            if self.length == 1:
                self.head.next = node
            self.tail.next = node
            self.tail = node
        self.length += 1

        return self

    def pop(self):
        if not self.length:
            return None

        result = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            result.prev = None

        self.length -= 1

        return result

    def prepend(self, value):
        node = Node(value)

        if not self.length:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            if self.length == 1:
                self.tail.prev = node
            self.head.prev = node
            self.head = node

        self.length += 1

        return self

    def pop_first(self):
        if not self.length:
            return None
        result = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

        return result


    def get(self, index: int):
        if (index < 0) or (index > (self.length - 1)):
            return None

        if (index < self.length // 2):
            i = 0
            pointer = self.head

            while i < index:
                pointer = pointer.next
                i += 1
            return pointer
        else:
            i = self.length - 1
            pointer = self.tail

            while i > index:
                pointer = pointer.prev
                i -= 1
            return pointer

    def set_value(self, index: int, value: int):
        node = self.get(index)

        if not node:
            return False

        node.value = value

        return True

    def insert(self, index: int, value: int):
        if (index < 0) or (index > self.length):
            return False
        if index == 0:
            self.prepend(value)
            return True

        if index == self.length:
            self.append(value)
            return True

        after = self.get(index)
        before = after.prev
        node = Node(value)
        node.prev = before
        node.next = after
        before.next = node
        after.prev = node

        self.length += 1

        return True

    def remove(self, index):
        if (index < 0) or (index >= self.length):
            return None
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        node = self.get(index)
        after = node.next
        before = node.prev
        before.next = after
        after.prev = before

        self.length -= 1

        return node
