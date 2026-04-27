# Merge Sort

## Steps

- Divide and conquer!

1. Collection is divided in two halves
2. Each half is sorted (subproblem)
3. The sorted halves are merged together

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
