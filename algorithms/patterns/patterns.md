# Patterns

Triage:

1. `Is the input sorted, or could sorting cheaply unlock something?` → two pointers, binary search
2. `Is the answer a contiguous subarray/substring?` → sliding window or prefix sums
3. `Does the answer require pairing/triplet/lookup?` → hashing
4. `Is there nesting / matching / "most recent"?` → stack
5. `Is there a monotonic predicate over a numeric search space?` → binary search the answer
6. `Tree or graph?` → BFS for shortest unweighted, DFS for "explore all"
7. `"All combinations / all valid configurations"?` → backtracking
8. `"Min/max/count of ways" + overlapping subproblems?` → DP
9. `Top-k / streaming / k-way merge?` → heap
10. `"Range sum / range count" of static array?` → prefix sums
11. `"Always pick the locally best" + can prove it works?` → greedy

---

## Hashing — frequency, lookup, dedup

> Replace an `O(n)` scan-for-existence with an `O(1)` lookup.

`Triggers`

- "Has this value been seen before?" / "find duplicates" / "two values that sum to k".
- Counting frequencies / detecting anagrams.
- Mapping `a[i] → i`, or grouping items by some derived key.

`Skeleton`

```python
seen = {}
for i, x in enumerate(a):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```

`Problems`

- **Two Sum** `O(n) / O(n)` — hash map of `target - x` while iterating.
- **Contains Duplicate** `O(n) / O(n)` — set membership check.
- **Valid Anagram** `O(n) / O(1)` — counter of each string, compare.
- **Group Anagrams** `O(n·k log k) / O(n·k)` — map sorted-key (or count-tuple) → list.
- **Valid Sudoku** `O(1)` — three sets (row, col, 3×3 box).
- **Longest Consecutive Sequence** `O(n) / O(n)` — set lookup; only start counting from numbers without `n-1`.
- **LRU Cache** `O(1) per op / O(capacity)` — hash map + doubly linked list.
- **Encode and Decode Strings** `O(n) / O(n)` — length-prefix each segment (`"5#hello"`).
- **Roman to Integer / Integer to Roman** — lookup table; greedy with paired tokens.
- **Set Matrix Zeroes** — use first row/col as in-place markers.
- **FizzBuzz** — small lookup-style conditional chain; mind the order.

---

## Two pointers

> Two indices walk a sequence to replace a nested `O(n²)` loop with a single `O(n)` pass.

`Triggers`

- Sorted array / string with a pair/triple constraint.
- Palindromes (converge from ends).
- In-place rewrite ("read" pointer ahead of "write" pointer).
- Linked-list cycle / nth-from-end (fast & slow).

`Skeleton`

```python
# opposite ends
l, r = 0, len(a) - 1
while l < r:
    s = a[l] + a[r]
    if s == target: return (l, r)
    if s < target: l += 1
    else: r -= 1
```

```python
# fast & slow
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast: ...   # cycle detected
```

`Problems`

- **Valid Palindrome** `O(n) / O(1)` — skip non-alphanumerics; converge from ends.
- **Two Sum II (sorted)** `O(n) / O(1)` — `left`/`right` move toward each other based on sum.
- **3Sum** `O(n²) / O(1)` — sort, fix `i`, two pointers for remaining sum; skip duplicates.
- **Container With Most Water** `O(n) / O(1)` — move the shorter wall inward.
- **Trapping Rain Water** `O(n) / O(1)` — two pointers; track left/right max.
- **Remove Duplicates from Sorted Array** `O(n) / O(1)` — read/write pointers in place.
- **Reverse Linked List** `O(n) / O(1)` — iterative `prev`/`curr`/`next` rewiring.
- **Merge Two Sorted Lists** `O(n+m) / O(1)` — dummy head; splice smaller node.
- **Linked List Cycle** `O(n) / O(1)` — Floyd's tortoise & hare.
- **Remove Nth Node from End** `O(n) / O(1)` — two pointers, gap of n.
- **Reorder List** `O(n) / O(1)` — find middle, reverse second half, interleave.
- **Reverse Integer (with overflow)** — repeatedly `% 10`; check bounds.
- **String to Integer (atoi)** — trim, sign, accumulate, clamp.
- **Spiral Matrix** — track 4 boundaries, peel layer at a time.
- **Rotate Image** — transpose then reverse rows.

---

## Sliding window

> Maintain a contiguous range `[l, r]` and update an aggregate incrementally as it grows or shrinks.

`Triggers`

- Answer is a **contiguous** subarray/substring.
- "Longest / shortest / max / min subarray with property X".
- Aggregate (sum, count, frequency map) is reversible.

`Skeleton`

```python
# variable window
l = 0; best = 0; agg = init()
for r, x in enumerate(a):
    agg.add(x)
    while not feasible(agg):
        agg.remove(a[l]); l += 1
    best = max(best, r - l + 1)
```

```python
# fixed window of size k
agg = sum(a[:k]); best = agg
for r in range(k, len(a)):
    agg += a[r] - a[r-k]
    best = max(best, agg)
```

`Problems`

- **Best Time to Buy and Sell Stock** `O(n) / O(1)` — track running min, update best profit.
- **Longest Substring Without Repeating Characters** `O(n) / O(min(n,Σ))` — map char→last index; advance left past duplicates.
- **Longest Repeating Character Replacement** `O(n) / O(Σ)` — window with counter; shrink when window − maxFreq > k.
- **Permutation in String** `O(n) / O(Σ)` — fixed window; counter equality.
- **Minimum Window Substring** `O(n) / O(Σ)` — expand right, shrink left while window covers `t`.
- **Sliding Window Maximum** `O(n) / O(k)` — monotonic deque of indices.

---

## Binary search

> Halve the candidate space each step using a monotonic predicate.

`Triggers`

- Sorted input — find target / first ≥ x / last ≤ x.
- Rotated-sorted array.
- Numeric search space where `f(x)` flips false → true exactly once. (Capacity, speed, time, threshold problems.)

`Skeleton`

```python
# leftmost true
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if pred(mid): hi = mid
    else: lo = mid + 1
return lo
```

`"Binary search the answer" recipe`

1. Pick the answer's range `[lo, hi]`.
2. Define `feasible(x)` — "can we achieve the goal with parameter x?".
3. Verify `feasible` is monotonic.
4. Binary search the smallest (or largest) feasible `x`.

`Problems`

- **Binary Search** `O(log n) / O(1)` — standard template.
- **Search in Rotated Sorted Array** `O(log n) / O(1)` — detect which half is sorted; recurse on relevant half.
- **Find Minimum in Rotated Sorted Array** `O(log n) / O(1)` — compare `mid` to `right` to pick half.
- **Search a 2D Matrix** `O(log m·n) / O(1)` — treat as flat sorted array, map index to (row, col).
- **Koko Eating Bananas** `O(n log max) / O(1)` — binary search the answer; predicate is "can finish at speed k?".
- **Median of Two Sorted Arrays** `O(log min(m,n)) / O(1)` — binary search partition on smaller array.
- **Pow(x, n)** `O(log n) / O(1)` — fast exponentiation; halve `n`, square `x`.

---

## Stack

> LIFO matches the structure when the most recent unmatched item drives the next decision. A *monotonic* stack additionally enforces an ordering on what stays in it — pops anything that would break the order — and that's how "next greater / smaller" is `O(n)`.

`Triggers`

- Bracket / parenthesis / tag matching.
- Nested expressions (RPN, calculator, decode string).
- "Most recent" lookups during a single scan.
- "Next greater / smaller element" → monotonic stack.

`Skeleton`

```python
# matching
stack = []
for t in tokens:
    if is_open(t): stack.append(t)
    elif is_close(t):
        if not stack or not match(stack.pop(), t): return False
return not stack
```

```python
# monotonic (next greater on the right)
res = [-1] * n; stack = []
for i, x in enumerate(a):
    while stack and a[stack[-1]] < x:
        res[stack.pop()] = x
    stack.append(i)
```

`Problems`

- **Valid Parentheses** `O(n) / O(n)` — push openers; on closer, pop and match.
- **Min Stack** `O(1) per op / O(n)` — pair every push with current min on stack.
- **Evaluate Reverse Polish Notation** `O(n) / O(n)` — push numbers, pop two on operator.
- **Decode String** `O(n) / O(n)` — push partial state on `[`, pop and repeat on `]`.
- **Daily Temperatures** `O(n) / O(n)` — monotonic decreasing stack of indices.
- **Largest Rectangle in Histogram** `O(n) / O(n)` — monotonic stack; pop when current < top.
- **Asteroid Collision** `O(n) / O(n)` — stack; resolve collisions on opposite signs.

---

## BFS — level-order / shortest unweighted

> Queue-based traversal that visits all nodes at distance `d` before any at `d+1`. Optimal for shortest path on **unweighted** graphs.

`Triggers`

- "Shortest steps / minimum moves" in a grid or graph with uniform edge cost.
- "Level by level" tree processing.
- Word ladder, knight's shortest path, rotting oranges.

`Skeleton`

```python
from collections import deque
q = deque([start]); seen = {start}; dist = 0
while q:
    for _ in range(len(q)):       # one full level
        node = q.popleft()
        if node == goal: return dist
        for nb in neighbours(node):
            if nb not in seen:
                seen.add(nb); q.append(nb)
    dist += 1
return -1
```

`Problems`

- **Binary Tree Level Order Traversal** `O(n) / O(n)` — BFS with a queue, process per level.
- **Maximum Width of Binary Tree** `O(n) / O(n)` — BFS with index propagation; track first/last per level.
- **Word Ladder** `O(N·L²) / O(N·L²)` — BFS over word graph using wildcard buckets.
- **Rotting Oranges** `O(m·n) / O(m·n)` — multi-source BFS from all rotten cells.
- **Shortest Path in Binary Matrix** `O(m·n) / O(m·n)` — BFS on a grid with 8-direction moves.

---

## DFS — explore all / connected component

> Recursive (or stack-based) traversal that follows a path to its end before backtracking.

`Triggers`

- "Is there a path from A to B?" / "count connected components".
- Tree problems where every node's answer depends on its subtrees (post-order).
- Flood fill on grids.
- Cycle detection in directed/undirected graphs.

`Skeleton`

```python
# graph
seen = set()
def dfs(u):
    seen.add(u)
    for v in g[u]:
        if v not in seen:
            dfs(v)
```

```python
# tree post-order returning info
def dfs(node):
    if not node: return base
    L = dfs(node.left); R = dfs(node.right)
    return combine(node.val, L, R)
```

`Problems`

- **Invert Binary Tree** `O(n) / O(h)` — recurse, swap children.
- **Maximum Depth of Binary Tree** `O(n) / O(h)` — recursion or BFS level count.
- **Same Tree / Subtree** `O(n) / O(h)` — recurse comparing nodes.
- **Validate BST** `O(n) / O(h)` — DFS with `(low, high)` range.
- **Lowest Common Ancestor (BST)** `O(h) / O(1)` — walk down comparing values.
- **Lowest Common Ancestor (Binary Tree)** `O(n) / O(h)` — recurse; node where left and right both find a target.
- **Construct Tree from Preorder + Inorder** `O(n) / O(n)` — use preorder for root, split inorder.
- **Kth Smallest in BST** `O(h+k) / O(h)` — inorder traversal, count to k.
- **Serialize/Deserialize Binary Tree** `O(n) / O(n)` — preorder with null markers.
- **Number of Islands** `O(m·n) / O(m·n)` — DFS or BFS flood fill, mark visited.
- **Flood Fill** `O(m·n) / O(m·n)` — DFS from start cell, repaint matching neighbours.
- **Clone Graph** `O(V+E) / O(V)` — DFS/BFS with old→new map.
- **Pacific Atlantic Water Flow** `O(m·n) / O(m·n)` — DFS/BFS from each ocean's borders inward.
- **Course Schedule** `O(V+E) / O(V+E)` — topological sort via DFS post-order, or Kahn's BFS by indegree.

---

## Backtracking

> DFS where you make a choice, recurse, and **undo** the choice on return. Used to enumerate / search a solution space with pruning.

`Triggers`

- "Generate all permutations / combinations / subsets / partitions".
- Constraint satisfaction (Sudoku, N-Queens, word search).
- "Find any/all valid configurations".

`Skeleton`

```python
def backtrack(path, choices):
    if is_solution(path):
        out.append(path[:]); return
    for c in choices:
        if not valid(path, c): continue
        path.append(c)
        backtrack(path, next_choices(choices, c))
        path.pop()             # undo
```

`Problems`

- **Subsets** `O(n·2ⁿ) / O(n) stack` — choose/skip recursion or iterative power-set.
- **Permutations** `O(n·n!) / O(n)` — swap-in-place or used-set recursion.
- **Combination Sum** `O(2ᵗ) / O(target)` — recurse with remaining target; advance index to avoid reuse permutations.
- **Generate Parentheses** `O(4ⁿ/√n) / O(n)` — backtracking with `open` and `close` counts.
- **Word Search** `O(m·n·4ᴸ) / O(L)` — DFS with visited markers, restore on backtrack.
- **Word Search II** `O(m·n·4ᴸ)` — trie of dictionary + DFS from each grid cell.
- **Palindrome Partitioning** `O(n·2ⁿ) / O(n)` — DFS, partition at each palindromic prefix.
- **N-Queens** `O(n!) / O(n)` — track column / diag1 / diag2 sets.
- **Sudoku Solver** `O(9⁸¹) worst / O(1) board` — choose 1-9 in empty cell; rollback on conflict.

---

## Dynamic programming

> Decompose into overlapping subproblems with optimal substructure; cache each subproblem's answer.

`Triggers`

- "Min / max / count of ways to reach / form X".
- Naive recursion has exponential branching but few **distinct** states.
- 1D: index-based decisions (rob houses, climb stairs). 2D: pair of indices (LCS, edit distance) or grid (unique paths).
- Knapsack-style: "pick items to optimise value under a constraint".

`Recipe`

1. Define `dp[state]` precisely.
2. Write the recurrence: how does `dp[state]` relate to smaller states?
3. Identify base cases.
4. Decide top-down (memoise) or bottom-up (iterate).
5. Optimise space (often `O(n)` → `O(1)` rolling).

`Skeleton`

```python
# 1D bottom-up
dp = [0] * (n + 1); dp[0] = base
for i in range(1, n + 1):
    dp[i] = recurrence(dp, i, a)
return dp[n]
```

`Problems`

- **Climbing Stairs** `O(n) / O(1)` — `dp[i] = dp[i-1] + dp[i-2]` (Fibonacci).
- **House Robber** `O(n) / O(1)` — `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.
- **Coin Change** `O(n·A) / O(A)` — `dp[amt] = min(dp[amt - c] + 1)` over coins.
- **Longest Increasing Subsequence** `O(n²) / O(n)` — `dp[i] = max(dp[j]+1)` for `j<i, a[j]<a[i]`; or patience sort `O(n log n)`.
- **Longest Common Subsequence** `O(n·m) / O(n·m)` — 2D DP on (i, j); `+1` if match else `max(up, left)`.
- **Word Break** `O(n²) / O(n)` — `dp[i] = any(dp[j] and s[j:i] in dict)`.
- **Edit Distance** `O(n·m) / O(n·m)` — 2D DP with insert/delete/replace transitions.
- **Maximum Subarray (Kadane)** `O(n) / O(1)` — `cur = max(x, cur+x)`; track best.
- **Unique Paths** `O(m·n) / O(n)` — Pascal-style 2D DP.
- **Partition Equal Subset Sum** `O(n·sum) / O(sum)` — 0/1 knapsack on `sum/2`.
- **Longest Palindromic Substring** `O(n²) / O(1)` — expand around each center (2n-1 centers) — DP-style without a table.
- **Palindromic Substrings** `O(n²) / O(1)` — same expansion, count.
- **Decode Ways** `O(n) / O(1)` — `dp[i] = dp[i-1] (if s[i-1] valid) + dp[i-2] (if s[i-2:i] valid)`.

---

## Greedy

> At each step, take the locally optimal action; the locally best is also globally best for problems with the **greedy-choice property**.

`Triggers`

- Interval scheduling / merging.
- Activity selection / minimum number of platforms.
- "Always pick the largest / earliest-ending / nearest" feels right and you can prove it.

`Skeleton`

```python
# interval problems
intervals.sort(key=lambda x: x[end])
last_end = -inf; count = 0
for s, e in intervals:
    if s >= last_end:
        count += 1; last_end = e
```

**Proof obligation:** before committing to greedy, sketch *why* the local choice is safe. Otherwise default to DP.

`Problems`

- **Jump Game** `O(n) / O(1)` — track furthest reachable index.
- **Jump Game II** `O(n) / O(1)` — greedy "current end / furthest" levels.
- **Gas Station** `O(n) / O(1)` — if sum ≥ 0, start is index after last running deficit.
- **Merge Intervals** `O(n log n) / O(n)` — sort by start; merge overlapping.
- **Non-overlapping Intervals** `O(n log n) / O(1)` — sort by end; greedy keep earliest-ending.
- **Can Place Flowers** `O(n) / O(1)` — scan; place when current and neighbours are zero.
- **Increasing Triplet Subsequence** `O(n) / O(1)` — track first and second smallest seen.

---

## Heap / priority queue

> A balanced-tree structure with `O(log n)` push/pop and `O(1)` peek of the min (or max).

`Triggers`

- Top-k / k-th largest / k-th smallest.
- Streaming median (two heaps).
- Merge k sorted lists/streams.
- Scheduling / "process the next available" simulations.
- Dijkstra (priority queue of (dist, node)).

`Skeleton`

```python
import heapq
h = []                              # min-heap by default
for x in a:
    heapq.heappush(h, x)
    if len(h) > k: heapq.heappop(h) # keeps the k largest
return h[0]                         # k-th largest
```

`Problems`

- **Kth Largest Element in Array** `O(n log k) / O(k)` — min-heap of size k, or quickselect.
- **Top K Frequent Elements** `O(n log k) / O(n)` — counter + heap of size k, or bucket sort.
- **Last Stone Weight** `O(n log n) / O(n)` — max-heap simulation.
- **K Closest Points to Origin** `O(n log k) / O(k)` — max-heap of size k by distance.
- **Find Median from Data Stream** `O(log n) per op` — two heaps (max for lower, min for upper).
- **Task Scheduler** `O(n log Σ) / O(Σ)` — counter + heap by frequency.
- **Merge K Sorted Lists** `O(N log k) / O(k)` — min-heap of heads.
- **Network Delay Time** `O((V+E) log V) / O(V)` — Dijkstra with min-heap.
- **Meeting Rooms II** `O(n log n) / O(n)` — sort starts/ends; sweep two pointers, or min-heap of end times.

---

## Prefix sums

> Pre-compute `pre[i] = a[0] + … + a[i-1]`. Range sum `[l, r]` becomes `pre[r+1] - pre[l]` in `O(1)`.

`Triggers`

- Many range-sum or range-count queries on a static array.
- "Number of subarrays with sum exactly k" → prefix sum + hash map of seen sums.
- 2D: pre-compute `pre[r][c]` for instant rectangle sums.

`Skeleton`

```python
# count subarrays summing to k
seen = {0: 1}; cur = 0; count = 0
for x in a:
    cur += x
    count += seen.get(cur - k, 0)
    seen[cur] = seen.get(cur, 0) + 1
```

`Problems`

- **Range Sum Query (immutable)** `O(n) build, O(1) query` — classic prefix array.
- **Subarray Sum Equals K** `O(n) / O(n)` — running sum + hash map of `cur - k`.
- **Continuous Subarray Sum** `O(n) / O(n)` — running sum mod k + hash of remainders.
- **Product of Array Except Self** `O(n) / O(1) extra` — prefix and suffix products in two passes.
- **Find Pivot Index** `O(n) / O(1)` — `2·left == total - a[i]` while scanning.
- **Find the Highest Altitude** `O(n) / O(1)` — running sum, track max.
