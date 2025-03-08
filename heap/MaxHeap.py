class MaxHeap:
    heap: list[int]

    def __init__(self):
        self.heap = []

    def _left_child_index(self, index):
        return index * 2 + 1

    def _right_child_index(self, index):
        return index * 2 + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _parent_index(self, index: int):
        return (index -1) // 2

    def _is_parent_less_than(self, index: int):
        return self.heap[self._parent_index(index)] < self.heap[index]

    def insert(self, value: int):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0 and self._is_parent_less_than(i):
            self._swap(i, self._parent_index(i))
            i = self._parent_index(i)

        return self

    def _sink_down(self, index: int):
        i = index
        i_max = index
        length = len(self.heap)

        while True:
            left_child_index = self._left_child_index(i)
            right_child_index = self._right_child_index(i)

            if (left_child_index < length) and (self.heap[left_child_index] > self.heap[i_max]):
                i_max = left_child_index

            if (right_child_index < length) and (self.heap[right_child_index] > self.heap[i_max]):
                i_max = right_child_index

            if i_max != i:
                self._swap(i, i_max)
                i = i_max
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        self._swap(0, len(self.heap) - 1)
        value = self.heap.pop()

        self._sink_down(0)

        return value


    def print(self):
        print(self.heap)
