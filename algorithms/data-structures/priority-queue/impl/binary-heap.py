# %%


class MaxHeap:
    def __init__(self, numbers: list[int] | None = None):
        self.heap: list[int] = numbers if numbers else []
        self._heapify()

    def _heapify(self) -> None:
        """
        O(n)
           O(n) due to the half array iteration
           O(n) due to the sifting down of the elements. It might seem like it's O(log(n)) because every node needs to travel at most the height of the tree, but few elements actually need to travel all the height, see https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
        """
        # We start from the middle of the array and go backwards because the last level of the tree (the rest of the array) will be arranged anyway by the bubbles performed on the upper levels
        mid_index = len(self.heap) // 2
        for i in reversed(range(mid_index + 1)):
            self._sift_down(i)

    def _sift_down(self, i: int) -> None:
        """
        O(log(n))
        """
        child = self._largest_child(i)
        if child is not None and self.heap[child] > self.heap[i]:
            self.heap[child], self.heap[i] = self.heap[i], self.heap[child]
            self._sift_down(child)

    def _sift_up(self, i: int) -> None:
        """
        O(log(n))
        """
        parent = self._parent(i)
        if parent is not None and self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self._sift_up(parent)

    def _parent(self, i: int) -> int | None:
        parent_index = (i - 1) // 2
        if 0 <= parent_index < len(self.heap):
            return parent_index

    def _largest_child(self, i: int) -> int | None:
        left_child = self._left(i)
        right_child = self._right(i)
        children = list(filter(lambda el: el, [left_child, right_child]))
        return max(children, key=lambda i: self.heap[i]) if children else None

    def _left(self, i: int) -> int | None:
        left_child_index = 2 * i + 1
        if 0 <= left_child_index < len(self.heap):
            return left_child_index

    def _right(self, i: int) -> int | None:
        right_child_index = 2 * i + 2
        if 0 <= right_child_index < len(self.heap):
            return right_child_index

    def peek(self) -> int:
        """
        O(1)
        """
        return self.heap[0]

    def pop(self) -> int:
        """
        O(log(n))
        Due to the bubble downwards restoration (bubble downwards)
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        highest = self.heap.pop()
        self._sift_down(0)
        return highest

    def push(self, number: int) -> None:
        """
        O(log(n))
        Due to the bubble upwards restoration (bubble upwards)
        """
        i = len(self.heap)
        self.heap.append(number)
        self._sift_up(i)


# Heapify
heap = MaxHeap([1, 2, 3, 4, 5, 6, 7])
assert heap.heap == [7, 5, 6, 4, 2, 1, 3]

# Peek
assert heap.peek() == 7
assert heap.heap == [7, 5, 6, 4, 2, 1, 3]

# Pop
assert heap.pop() == 7
assert heap.heap == [6, 5, 3, 4, 2, 1]

# Push
heap.push(7)
assert heap.heap == [7, 5, 6, 4, 2, 1, 3]
