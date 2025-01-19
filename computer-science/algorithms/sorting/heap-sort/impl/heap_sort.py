# %%
import unittest
import heapq

def heap_sort(arr: list) -> list:
  heap = list(arr) # leave the original arr untouched - O(n)
  heapq.heapify(heap) # min heap - O(n*log(n))
  return [heapq.heappop(heap) for _ in range(len(heap))] # O(n)

test_case = unittest.TestCase()
test_case.assertEqual(heap_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
test_case.assertEqual(heap_sort([]), [])
test_case.assertEqual(heap_sort([1]), [1])
test_case.assertEqual(heap_sort([1, 1]), [1, 1])
