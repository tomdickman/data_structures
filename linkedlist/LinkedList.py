from .Node import Node

class LinkedList:
    head: Node = None
    length: int = 0
    tail: Node = None

    def __init__(self, value = None):
        if value:
            self.append(value)

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return self

    def pop(self):
        """
        pop node off end of list
        """
        if self.length <= 1:
            removed = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        else:
            current = self.head
            while current != None:
                next = current.next
                if next.next == None:
                    removed = next
                    current.next = None
                    self.tail = current
                    self.length -= 1
                    return removed
                current = next

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.tail = node
        else:
            node.next = self.head
        self.head = node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            result = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return result
        else:
            result = self.head
            self.head = result.next
            self.length -= 1
            return result

    def get(self, index):
        if (index < 0) | (index >= self.length):
            return None

        if index == 0:
            return self.head
        if index == self.length - 1:
            return self.tail

        if self.length > 0:
            temp = self.head
            i = 0
            while i < index:
                temp = temp.next
                i += 1
            return temp

        return None

    def set_value(self, index, value):
        node = self.get(index)

        if node != None:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if (index < 0) | (index > self.length):
            return False

        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        linker_node = self.get(index - 1)
        current = linker_node.next
        node = Node(value)
        node.next = current
        linker_node.next = node
        return True


    def remove(self, index):
        if (self.length == 0) | (index < 0) | (index >= self.length):
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        linker_node = self.get(index - 1)
        removed = linker_node.next
        linker_node.next = removed.next
        return removed

    def reverse(self):
        new_head = self.tail
        new_tail = self.head

        current = self.head
        next = None

        while current != None:
            temp = current.next
            current.next = next
            next = current
            current = temp

        self.head = new_head
        self.tail = new_tail

    def find_middle_node(self):
        if self.head == None:
            return False

        one_step_pointer = self.head
        two_step_pointer = self.head

        while two_step_pointer != None:
            if two_step_pointer.next == None:
                return one_step_pointer

            one_step_pointer = one_step_pointer.next
            two_step_pointer = two_step_pointer.next.next

            if two_step_pointer == None:
                return False

    def has_loop(self):
        '''
        Check if the linked list contains a loop using Floyd's Cycle Finding Algorithm
        '''

        # Initialise the pointers
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer != None:
            if (fast_pointer.next == None) | (fast_pointer.next.next == None):
                # Reached the tail, no loop
                return False

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True


    def find_kth_from_end(self, k):
        if (k == None) | (self.head == None):
            return None

        slow_pointer = self.head
        fast_pointer = self.head

        for _ in range(k - 1):
            if fast_pointer.next != None:
                fast_pointer = fast_pointer.next
            else:
                return None

        while fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        return slow_pointer

    def partition_list(self, value):
        '''
        Partition the list based on the passed in value so that
        values less than the passed in value are moved to the head
        of the list while the rest are moved to the tail.
        Maintain the order of the values when moved

        For example with a list of [2, 5, 4, 3, 1] when 3 is passed in
        the list would  end up shaped as [2, 1, 3, 5, 4]
        '''
        if not self.head:
            return None

        new_list = LinkedList()
        tail_list = LinkedList()

        current = self.head
        while (current != None):
            if (current.value < value):
                new_list.append(current.value)
                last_head = current
            else:
                tail_list.append(current.value)
            current = current.next

        last_head.next = tail_list.head
        new_list.tail = tail_list.tail
        new_list.length = self.length

        return new_list

    def remove_duplicates(self):
        if not self.head:
            return self

        prev = None
        current = self.head
        values = []

        while current:
            if not (current.value in values):
                values.append(current.value)
                prev = current
            else:
                prev.next = current.next
                self.length -= 1
                if not current.next:
                    self.tail = prev
            current = current.next

        return self

    def binary_to_decimal(self):
        position = self.length - 1
        decimal = 0
        current = self.head

        while position >= 0:
            if (current.value != 1) and (current.value != 0):
                raise ValueError('Invalid binary number')
            decimal += (current.value * 2 ** position)
            current = current.next
            position -= 1

        return decimal

    def reverse_between(self, start_index: int, end_index: int):
        if end_index >= self.length:
            return None

        i = 0
        head_list_tail_node = None
        current = self.head

        # Increment the head list tail node to point to the
        # last node before the reverse needs to be implemented.
        while i < start_index:
           head_list_tail_node = current
           current = current.next
           i += 1

        prev = None
        # Store a pointer to the first node in the sequence, so
        # we can use it to update tail if it is the last node in list.
        sequence_tail = current

        for _ in range(end_index - start_index + 1):
            next = current.next
            current.next = prev
            prev = current
            current = next

        if current:
            sequence_tail.next = current
        else:
            self.tail = sequence_tail

        if not head_list_tail_node:
            self.head = prev
        else:
            head_list_tail_node.next = prev

        return self

def find_kth_from_end(list, k):
    if (k == None) | (list.head == None) | (list == None):
        return None

    slow_pointer = list.head
    fast_pointer = list.head

    for _ in range(k - 1):
        if fast_pointer.next != None:
            fast_pointer = fast_pointer.next
        else:
            return None

    while fast_pointer.next != None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return slow_pointer
