# Sorting

- <https://en.wikipedia.org/wiki/Sorting_algorithm>
- <https://www.toptal.com/developers/sorting-algorithms>
- <https://www.bigocheatsheet.com/>
- Python sorted() method: uses `powersort` (3.11+) and `timsort` (3.10-)

## Comparison sorts

Compares somehow each elements against each other. These algorithms can mathematically have at most $O(n\ log\ n)$

### S-Tier

- Timsort
  - for almost sorted
- Heapsort
  - for memory limitations

### A-Tier — $O(n\ log\ n)$

- Merge Sort
- Quick Sort

### B-Tier — $O(n^2)$ ~ $O(n)

- Insertion Sort

### C-Tier — $O(n^2)$

- Selection Sort
- Bubble Sort

## Non-comparison sorts

- Uses the way how data (0s and 1s) is stored on memory
- Only works with integer numbers in a specific range
- `Types`
  - Counting Sort
  - Radix Sort
  - Bucket Sort

## Stable vs. Unstable

A given sorting algorithms is considered `stable` when two elements with same value appear in the same order in the sorted list

On `unstable` algorithms, this order is not guaranteed

## Tradeoffs

- Fastest possible regardless?
  - Timsort, Mergesort
- Almost sorted?
  - Insertion
- Short memory space?
  - Insertion
- Only integers with low values?
  - Counting sort
