class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None
    
    def __init__(self, value: int):
        self.value = value