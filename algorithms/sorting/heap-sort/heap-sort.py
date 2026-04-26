# %%
import heapq


def heap_sort(col: list[int]) -> list[int]:
    heap = list(col)  # O(n) create a new list and leave the original one untouched
    heapq.heapify(heap)  # O(n*log(n)) - create min heap
    return [heapq.heappop(heap) for _ in range(len(heap))]  # O(n)


assert heap_sort([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
assert heap_sort([]) == []
assert heap_sort([1]) == [1]
assert heap_sort([1, 1]) == [1, 1]
