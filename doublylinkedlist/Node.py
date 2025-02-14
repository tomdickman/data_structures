class Node:
    value: int
    next: 'Node' = None
    prev: 'Node' = None

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
