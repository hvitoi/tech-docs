# %%


class MaxHeap:
    def __init__(self, elements=None):
        self.heap = elements
        self.restore()

    def get_parent(self, index: int) -> tuple[int, int]:
        parent_index = (index - 1) // 2
        if parent_index < len(self.heap):
            return (parent_index, self.heap[parent_index])

    def get_left_child(self, index: int) -> tuple[int, int]:
        left_child_index = 2 * index + 1
        if left_child_index < len(self.heap):
            return (left_child_index, self.heap[left_child_index])

    def get_right_child(self, index: int) -> tuple[int, int]:
        right_child_index = 2 * index + 2
        if right_child_index < len(self.heap):
            return (right_child_index, self.heap[right_child_index])

    def restore(self):
        mid_index = len(self.heap) // 2  # start from the middle and go left
        for i in reversed(range(mid_index + 1)):
            node = (i, self.heap[i])

            left_child = self.get_left_child(i)
            right_child = self.get_right_child(i)
            children = list(filter(lambda el: el, [left_child, right_child]))
            max_child = max(children, key=lambda el: el[1]) if children else None

            if max_child and max_child[1] > node[1]:
                self.heap[max_child[0]], self.heap[node[0]] = (
                    self.heap[node[0]],
                    self.heap[max_child[0]],
                )
        return self.heap

    def peek(self):
        return self.heap[0]

    def insert(self, item):
        self.heap.append(item)


heap = MaxHeap([10, 6, 7, 5, 15, 17, 12])
heap.restore()
