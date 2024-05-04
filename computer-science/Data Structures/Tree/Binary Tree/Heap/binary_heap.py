# %%
from unittest import TestCase


class MaxHeap:
    def __init__(self, numbers: list | None = None):
        self.heap: list = numbers if numbers else []
        self.__heapify()

    def __parent(self, i: int) -> int | None:
        parent_index = (i - 1) // 2
        if 0 <= parent_index < len(self.heap):
            return parent_index

    def __left(self, i: int) -> int | None:
        left_child_index = 2 * i + 1
        if 0 <= left_child_index < len(self.heap):
            return left_child_index

    def __right(self, i: int) -> int | None:
        right_child_index = 2 * i + 2
        if 0 <= right_child_index < len(self.heap):
            return right_child_index

    def __largest_child(self, i: int) -> int | None:
        left_child = self.__left(i)
        right_child = self.__right(i)
        children = list(filter(lambda el: el, [left_child, right_child]))
        return max(children, key=lambda i: self.heap[i]) if children else None

    def __bubble_downwards(self, i):
        """
        O(log(n))
        """
        child = self.__largest_child(i)
        if child is not None and self.heap[child] > self.heap[i]:
            self.heap[child], self.heap[i] = self.heap[i], self.heap[child]
            self.__bubble_downwards(child)

    def __bubble_upwards(self, i):
        """
        O(log(n))
        """
        parent = self.__parent(i)
        if parent is not None and self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.__bubble_upwards(parent)

    def __heapify(self):
        """
        O(n*log(n))
           O(n) due to the half array iteration
           O(log(n)) due to the bubble until (possibly) the end of the tree

        We start from the middle of the array and go backwards because the last level of the tree (the rest of the array) will be arranged anyway by the bubbles performed on the upper levels
        """
        mid_index = len(self.heap) // 2
        for i in reversed(range(mid_index + 1)):
            self.__bubble_downwards(i)
        return self.heap

    def peek(self) -> int:
        return self.heap[0]

    def pop(self) -> int | None:
        """
        O(log(n))
        Due to the bubble downwards restoration (bubble downwards)
        """
        if not self.heap:
            return
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        highest = self.heap.pop()
        self.__bubble_downwards(0)
        return highest

    def push(self, number: int) -> None:
        """
        O(log(n))
        Due to the bubble upwards restoration (bubble upwards)
        """
        i = len(self.heap)
        self.heap.append(number)
        self.__bubble_upwards(i)
        return None


test_case = TestCase()

# Heapify
heap = MaxHeap([1, 2, 3, 4, 5, 6, 7])
test_case.assertEqual(heap.heap, [7, 5, 6, 4, 2, 1, 3])

# Peek
test_case.assertEqual(heap.peek(), 7)
test_case.assertEqual(heap.heap, [7, 5, 6, 4, 2, 1, 3])

# Pop
test_case.assertEqual(heap.pop(), 7)
test_case.assertEqual(heap.heap, [6, 5, 3, 4, 2, 1])

# Push
heap.push(7)
test_case.assertEqual(heap.heap, [7, 5, 6, 4, 2, 1, 3])
