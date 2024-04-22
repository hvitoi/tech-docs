# %%
#
class MaxHeap:
    def __init__(self, elements=None):
        self.heap: list = elements
        self.full_restore()

    def get_parent(self, child_index: int) -> int:
        parent_index = (child_index - 1) // 2
        if parent_index < len(self.heap):
            return parent_index

    def get_left_child(self, parent_index: int) -> int:
        left_child_index = 2 * parent_index + 1
        if left_child_index < len(self.heap):
            return left_child_index

    def get_right_child(self, parent_index: int) -> int:
        right_child_index = 2 * parent_index + 2
        if right_child_index < len(self.heap):
            return right_child_index

    def get_largest_child(self, parent_index: int) -> int:
        left_child = self.get_left_child(parent_index)
        right_child = self.get_right_child(parent_index)
        children = list(filter(lambda el: el, [left_child, right_child]))
        return max(children, key=lambda i: self.heap[i]) if children else None

    def bubble_downwards(self, parent_index):
        """
        O(log(n))
        It is a partial restoration of the heap property on a localized area/node
        """
        child_index = self.get_largest_child(parent_index)
        if child_index and self.heap[child_index] > self.heap[parent_index]:
            self.heap[child_index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[child_index],
            )
            self.bubble_downwards(child_index)

    def full_restore(self):
        """
        O(n*log(n))
           O(n) due to the half array iteration
           O(log(n)) due to the bubble until (possibly) the end of the tree

        We start from the middle of the array and go backwards because the last level of the tree (the rest of the array) will be arranged anyway by the bubbles performed on the upper levels
        """
        mid_index = len(self.heap) // 2
        for i in reversed(range(mid_index + 1)):
            self.bubble_downwards(i)
        return self.heap

    def pop_highest(self):
        """
        O(log(n))
        Due to the bubble downwards restoration
        """
        if not self.heap:
            return
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        highest = self.heap.pop()
        self.bubble_downwards(0)
        return highest

    def peek_highest(self):
        return self.heap[0]

    def insert(self, item):
        pass


heap = MaxHeap([10, 6, 7, 5, 15, 17, 12])
heap.full_restore()
