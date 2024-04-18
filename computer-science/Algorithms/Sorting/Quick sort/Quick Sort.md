# Quick Sort

## Complexity

- Time complexity: $O(n\ log\ n)$
  - $O(n)$ due to the division of left and right for the halves
  - $O(log\ n)$ due to the recursive sorting of each half
  - The complexity can be $O(n)$ when the pivot is not distributed well around the mid point
- Space complexity: $O(log\ n)$
  - The call stack

## Steps

- Divide and conquer!
- Uses a pivoting technique

1. Elect a pivot (the middle point in the array)
1. All elements smaller than the pivot are moved to the left, all elements greater than the pivot are moved to the right
1. Each divided part is called recursively
1. Concatenate everything together (left + pivot + right)
