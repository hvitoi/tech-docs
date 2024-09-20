# Partitioning

- In-place partitioning is the key of the quicksort algorithm
- The partitioning takes a pivot and moves all the lower elements to the left, and all the greater elements to the right

```python
def partition(arr: list[int], *, left: int, right: int) -> int:
    pivot = arr[right]  # pivot is the rightmost el
    i = left  # elements to the left of this index (exclusive) are lower than the pivot
    for j in range(left, right):  # excludes the last element (the pivot)
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]  # Bring pivot to the correct position
    return i  # return the pivot's final resting position
```
