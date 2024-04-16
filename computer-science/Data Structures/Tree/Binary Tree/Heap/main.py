# %%


class MinHeap:
    def __init__(self):
        self.heap = []

    def peek(self):
        return self.heap[0]

    def insert(self, item):
        self.heap.append(item)

    # WIP
