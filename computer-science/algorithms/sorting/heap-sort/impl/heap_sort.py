# %%
import unittest
import heapq

def heap_sort(arr: list) -> list:
  heapq.heapify(arr) # min heap
  sorted_arr = []
  for _ in range(len(arr)):
    sorted_arr.append(heapq.heappop(arr))
  return sorted_arr

# test_case = unittest.TestCase()
# test_case.assertEqual(heap_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
# test_case.assertEqual(heap_sort([]), [])
# test_case.assertEqual(heap_sort([1]), [1])
# test_case.assertEqual(heap_sort([1, 1]), [1, 1])


# arr = [ 1,2,3]
# heap_sort(arr)

# %%
