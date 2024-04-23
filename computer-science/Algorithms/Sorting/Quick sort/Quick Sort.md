# Quick Sort

## Steps

- Divide and conquer!
- Uses a pivoting technique

1. Elect a pivot (first element in the array)
1. All elements smaller than the pivot are moved to the left, all elements greater than the pivot are moved to the right
1. Each divided part is called recursively
1. Concatenate everything together (left + pivot + right)

## Complexity

- **Time**
  - $O(n^2)$
  - $\Theta(n*log(n))$
  - $\Omega(n*log(n))$
- **Space**
  - $O(log(n))$

$O(n)$ due to the division of left and right for the halves (by the pivot index) + the concatenation of the halves + pivot

$O(log(n))$ is due to the recursive sorting of each half

The runtime complexity can be $O(n^2)$ when the pivot is not distributed well around the mid point. In this case the $O(log(n))$ portion turns into $O(n)$
