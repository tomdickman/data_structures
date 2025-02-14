from .Node import Node

class LinkedListNoLength:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        one_step_pointer = self.head
        two_step_pointer = self.head

        if self.head == None:
            return False

        while two_step_pointer.next != None:
            if two_step_pointer.next == None:
                return one_step_pointer
          
            one_step_pointer = one_step_pointer.next
            two_step_pointer = two_step_pointer.next.next
          
            if two_step_pointer == None:
                return None


    def has_loop(self):
        slow_pointer = self.head
        faster_pointer = self.head

        # Cycle through and
        return

    def find_kth_from_end(self):
        # The function should utilize two pointers, slow and fast, initialized to the head of the linked list.

        # The fast pointer should move k nodes ahead in the list.

        # If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.

        # The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.

        # The function should return the slow pointer, which will be at the k-th position from the end of the list.
        return

    def partition_list(self, key):
        # All list nodes with a value less than key are moved to head in order
        # All list nodes with a value more than key are moved to tail in order
        # input key = 5, LL: 3 -> 8 -> 5 -> 10 -> 2 -> 1
        # output LL: 3 -> 2 -> 1 -> 8 -> 5 -> 10
        return
