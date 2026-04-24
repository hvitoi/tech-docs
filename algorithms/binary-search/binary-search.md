# Binary search

Search a sorted sequence (or a monotonic predicate) in `O(log n)` by halving the candidate range each step.

## When to use

- Input is sorted, or can be made sorted cheaply.
- You can evaluate a monotonic predicate `f(x)` that flips false → true exactly once over the search space ("binary search the answer").
- You need a specific boundary: leftmost, rightmost, first-true, last-false.

## Invariant

At every step the answer lies in `[lo, hi]`. The loop narrows this interval; the exit condition determines which boundary you return.

## Canonical forms

- **Find exact**: `while lo <= hi`, return `mid` on match.
- **Leftmost true** (lower bound): `while lo < hi; mid = (lo+hi)//2; if pred(mid): hi = mid else: lo = mid+1` → `lo`.
- **Rightmost true** (upper bound): mirror of above with `mid = (lo+hi+1)//2`.
- **Search on answer**: `lo/hi` are candidate answers, `pred` checks feasibility (e.g. min capacity to ship in D days).

## Complexity

`O(log n)` comparisons; `O(1)` extra space.

## Pitfalls

- `mid = lo + (hi - lo) // 2` to avoid overflow in fixed-width languages.
- Off-by-one on the exit condition — pick one template per variant and stick to it.
- Infinite loop when `lo = mid` without `+1` in left-biased midpoint.
