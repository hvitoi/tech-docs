# Search

- **Search** is a kind of traversal stops as soon as the target item is found

## Linear search

- Search over a `linear data structure`
  - e.g., array
- It's also called **iteration**
- Runtime complexity: $O(n)$

```python
def linear_search(arr, target):
    for el in arr:
        if el == target:
            return True
    return False
```

## Binary search

- Search in a ordered data structure, in which at each loop half of the items can discarded
  - E.g., sorted array, binary search tree
- Runtime complexity: $O(log\ n)$

```python
def binary_search(arr, target):
    if not arr:
        return False

    mid_index = len(arr) // 2

    if target == arr[mid_index]:
        return True

    if target < arr[mid_index]:
        return binary_search(arr[:mid_index], target)

    if target > arr[mid_index]:
        return binary_search(arr[mid_index + 1 :], target)
```
