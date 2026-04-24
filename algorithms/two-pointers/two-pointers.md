# Two pointers

Two indices traverse a sequence together to replace a nested `O(n²)` loop with a single `O(n)` pass.

## When to use

- Sorted array / string where pairs depend on relative order (sum targets, palindromes, merging).
- Linked list traversal that needs a lag or cycle detection (fast/slow).
- In-place array rewriting where a "read" pointer runs ahead of a "write" pointer.

## Variants

- **Opposite ends**: `left` at 0, `right` at `n-1`, converge. Used for sorted-sum problems, container-with-most-water, palindrome check.
- **Same direction, fast/slow**: both start at 0; `fast` advances every step, `slow` advances on a condition. Floyd's cycle, remove-duplicates, partition.
- **Two sequences**: one pointer per input array. Merging sorted arrays, subsequence check.

## Complexity

Typically `O(n)` time, `O(1)` extra space. Each pointer moves monotonically — total moves are bounded by `n`.

## Pitfalls

- Requires sorted input for opposite-ends variants; sort first if you can afford `O(n log n)`.
- Moving both pointers in the same step can skip candidates — advance only one per iteration unless the problem justifies both.
