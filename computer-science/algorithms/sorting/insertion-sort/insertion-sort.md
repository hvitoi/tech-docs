# Insertion Sort

- Great for cases in which the list is almost sorted

## Complexity

- Time complexity: $O(n^2)$
- Space complexity: $O(1)$

- When it's almost sorted: $O(n)$

## Steps

1. Take a subarray `[x:]` of the array, take the last element and check where it would be inserted (from end to start)
1. At each pass, the subarray at the start will be sorted
1. Repeat the process adding one more item at a time to the subarray
