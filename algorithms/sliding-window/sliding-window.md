# Sliding window

Maintain a contiguous window `[left, right]` over an array or string and update an aggregate (sum, count, frequency map) incrementally as the window grows or shrinks. Turns an `O(n·k)` recount into `O(n)` amortized.

## When to use

- The answer is a contiguous subarray/substring.
- The aggregate over the window can be updated in `O(1)` when one element enters or leaves.
- The feasibility predicate is monotonic: once the window violates the constraint, shrinking it from the left eventually restores it.

## Variants

- **Fixed window, size `k`**: slide one step at a time; add `arr[right]`, remove `arr[right-k]`. Example: max average of length-k subarray.
- **Variable window**: expand `right` unconditionally; while constraint is violated, advance `left`. Track the best window seen. Example: longest substring without repeating characters, min window substring.
- **At-most-k trick**: "exactly k" = "at most k" − "at most k−1"; each piece is a variable window.

## Complexity

`O(n)` time — each index is entered and left at most once — plus the cost of the aggregate update (often `O(1)` with a hash map or counter).

## Pitfalls

- Confirm the aggregate is reversible (sum yes, min/max no — need a monotonic deque).
- The shrink step is a `while`, not an `if`: multiple left-advances per right-step are common.
