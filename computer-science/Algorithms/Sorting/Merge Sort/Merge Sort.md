# Merge Sort

## Steps

- Divide and conquer!

1. Array is divided in two halves and each is sorted
1. Two sorted halves are concatenated in the correct order

## Complexity

- **Time**
  - $O(n*log(n))$
  - $\Theta(n*log(n))$
  - $\Omega(n*log(n))$
- **Space**
  - $O(n)$
    - Each subarray created

- $O(n)$ due to the slicing and concatenation of each half
- $O(log(n))$ due to the recursive sorting of each half
