# %%
import heapq


def heap_sort(col: list[int]) -> list[int]:
    heap = list(col)  # O(n) copy elements into a new list (leave original untouched)
    heapq.heapify(heap)  # O(n) - create min heap

    # O(n*log(n)): heap pop O(log(n)) for every item O(n)
    return [heapq.heappop(heap) for _ in range(len(heap))]


assert heap_sort([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
assert heap_sort([]) == []
assert heap_sort([1]) == [1]
assert heap_sort([1, 1]) == [1, 1]
