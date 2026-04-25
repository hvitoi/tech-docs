# Common interview problems by pattern

Format per entry: **Problem** `time / space` — approach.

## Arrays & hashing

- **Two Sum** `O(n) / O(n)` — hash map of `target - x` while iterating.
- **Contains Duplicate** `O(n) / O(n)` — set membership check.
- **Valid Anagram** `O(n) / O(1)` — counter of each string, compare.
- **Group Anagrams** `O(n·k log k) / O(n·k)` — map sorted-key (or count-tuple) → list.
- **Top K Frequent Elements** `O(n log k) / O(n)` — counter + heap of size k, or bucket sort.
- **Product of Array Except Self** `O(n) / O(1) extra` — prefix and suffix products in two passes.
- **Valid Sudoku** `O(1)` — three sets (row, col, 3×3 box).
- **Longest Consecutive Sequence** `O(n) / O(n)` — set lookup; only start counting from numbers without `n-1`.

See [data-structures/array/](data-structures/array/array.md), [data-structures/map/](data-structures/map/hash-table.md).

## Two pointers

- **Valid Palindrome** `O(n) / O(1)` — skip non-alphanumerics; converge from ends.
- **Two Sum II (sorted)** `O(n) / O(1)` — `left`/`right` move toward each other based on sum.
- **3Sum** `O(n²) / O(1)` — sort, fix `i`, two pointers for remaining sum; skip duplicates.
- **Container With Most Water** `O(n) / O(1)` — move the shorter wall inward.
- **Trapping Rain Water** `O(n) / O(1)` — two pointers; track left/right max.
- **Remove Duplicates from Sorted Array** `O(n) / O(1)` — read/write pointers in place.

See [two-pointers/](two-pointers/two-pointers.md).

## Sliding window

- **Best Time to Buy and Sell Stock** `O(n) / O(1)` — track running min, update best profit.
- **Longest Substring Without Repeating Characters** `O(n) / O(min(n,Σ))` — map char→last index; advance left past duplicates.
- **Longest Repeating Character Replacement** `O(n) / O(Σ)` — window with counter; shrink when window − maxFreq > k.
- **Permutation in String** `O(n) / O(Σ)` — fixed window; counter equality.
- **Minimum Window Substring** `O(n) / O(Σ)` — expand right, shrink left while window covers `t`.
- **Sliding Window Maximum** `O(n) / O(k)` — monotonic deque of indices.

See [sliding-window/](sliding-window/sliding-window.md).

## Stack

- **Valid Parentheses** `O(n) / O(n)` — push openers; on closer, pop and match.
- **Min Stack** `O(1) per op / O(n)` — pair every push with current min on stack.
- **Evaluate Reverse Polish Notation** `O(n) / O(n)` — push numbers, pop two on operator.
- **Generate Parentheses** `O(4ⁿ/√n) / O(n)` — backtracking with `open` and `close` counts.
- **Daily Temperatures** `O(n) / O(n)` — monotonic decreasing stack of indices.
- **Largest Rectangle in Histogram** `O(n) / O(n)` — monotonic stack; pop when current < top.

See [data-structures/stack/](data-structures/stack/stack.md).

## Binary search

- **Binary Search** `O(log n) / O(1)` — standard template.
- **Search in Rotated Sorted Array** `O(log n) / O(1)` — detect which half is sorted; recurse on relevant half.
- **Find Minimum in Rotated Sorted Array** `O(log n) / O(1)` — compare `mid` to `right` to pick half.
- **Search a 2D Matrix** `O(log m·n) / O(1)` — treat as flat sorted array, map index to (row, col).
- **Koko Eating Bananas** `O(n log max) / O(1)` — binary search the answer; predicate is "can finish at speed k?".
- **Median of Two Sorted Arrays** `O(log min(m,n)) / O(1)` — binary search partition on smaller array.

See [binary-search/](binary-search/binary-search.md).

## Linked list

- **Reverse Linked List** `O(n) / O(1)` — iterative `prev`/`curr`/`next` rewiring.
- **Merge Two Sorted Lists** `O(n+m) / O(1)` — dummy head; splice smaller node.
- **Linked List Cycle** `O(n) / O(1)` — Floyd's tortoise & hare.
- **Remove Nth Node from End** `O(n) / O(1)` — two pointers, gap of n.
- **Reorder List** `O(n) / O(1)` — find middle, reverse second half, interleave.
- **LRU Cache** `O(1) per op / O(capacity)` — hash map + doubly linked list.
- **Merge K Sorted Lists** `O(N log k) / O(k)` — min-heap of heads.

See [data-structures/linked-list/](data-structures/linked-list/linked-list.md).

## Trees

- **Invert Binary Tree** `O(n) / O(h)` — recurse, swap children.
- **Maximum Depth of Binary Tree** `O(n) / O(h)` — recursion or BFS level count.
- **Same Tree / Subtree** `O(n) / O(h)` — recurse comparing nodes.
- **Binary Tree Level Order Traversal** `O(n) / O(n)` — BFS with a queue, process per level.
- **Validate BST** `O(n) / O(h)` — DFS with `(low, high)` range.
- **Lowest Common Ancestor (BST)** `O(h) / O(1)` — walk down comparing values.
- **Lowest Common Ancestor (Binary Tree)** `O(n) / O(h)` — recurse; node where left and right both find a target.
- **Construct Tree from Preorder + Inorder** `O(n) / O(n)` — use preorder for root, split inorder.
- **Kth Smallest in BST** `O(h+k) / O(h)` — inorder traversal, count to k.
- **Serialize/Deserialize Binary Tree** `O(n) / O(n)` — preorder with null markers.

See [data-structures/tree/](data-structures/tree/tree.md), [traversal/](traversal/traversal.md).

## Heap / priority queue

- **Kth Largest Element in Array** `O(n log k) / O(k)` — min-heap of size k, or quickselect.
- **Last Stone Weight** `O(n log n) / O(n)` — max-heap simulation.
- **K Closest Points to Origin** `O(n log k) / O(k)` — max-heap of size k by distance.
- **Find Median from Data Stream** `O(log n) per op` — two heaps (max for lower, min for upper).
- **Task Scheduler** `O(n log Σ) / O(Σ)` — counter + heap by frequency.

See [data-structures/tree/heap/](data-structures/tree/heap/).

## Backtracking

- **Subsets** `O(n·2ⁿ) / O(n) stack` — choose/skip recursion or iterative power-set.
- **Permutations** `O(n·n!) / O(n)` — swap-in-place or used-set recursion.
- **Combination Sum** `O(2ᵗ) / O(target)` — recurse with remaining target; advance index to avoid reuse permutations.
- **Word Search** `O(m·n·4ᴸ) / O(L)` — DFS with visited markers, restore on backtrack.
- **Palindrome Partitioning** `O(n·2ⁿ) / O(n)` — DFS, partition at each palindromic prefix.
- **N-Queens** `O(n!) / O(n)` — track column / diag1 / diag2 sets.

See [backtracking/](backtracking/backtracking.md), [recursion/](recursion/recursion.md).

## Graphs

- **Number of Islands** `O(m·n) / O(m·n)` — DFS or BFS flood fill, mark visited.
- **Clone Graph** `O(V+E) / O(V)` — DFS/BFS with old→new map.
- **Pacific Atlantic Water Flow** `O(m·n) / O(m·n)` — BFS from each ocean's borders inward.
- **Course Schedule** `O(V+E) / O(V+E)` — topological sort via DFS or Kahn's algorithm.
- **Word Ladder** `O(N·L²) / O(N·L²)` — BFS over word graph using wildcard buckets.
- **Network Delay Time** `O((V+E) log V) / O(V)` — Dijkstra with min-heap.

See [data-structures/graph/](data-structures/graph/graph.md), [traversal/](traversal/traversal.md).

## Dynamic programming

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

See [dynamic-programming/](dynamic-programming/dynamic-programming.md).

## Greedy

- **Jump Game** `O(n) / O(1)` — track furthest reachable index.
- **Jump Game II** `O(n) / O(1)` — greedy "current end / furthest" levels.
- **Gas Station** `O(n) / O(1)` — if sum ≥ 0, start is index after last running deficit.
- **Merge Intervals** `O(n log n) / O(n)` — sort by start; merge overlapping.
- **Non-overlapping Intervals** `O(n log n) / O(1)` — sort by end; greedy keep earliest-ending.
- **Meeting Rooms II** `O(n log n) / O(n)` — sort starts/ends; sweep two pointers, or min-heap of end times.

See [greedy-algorithms/](greedy-algorithms/greedy-algorithms.md).

## Strings

- **Longest Palindromic Substring** `O(n²) / O(1)` — expand around each center (2n-1 centers).
- **Palindromic Substrings** `O(n²) / O(1)` — same expansion, count.
- **Valid Anagram** `O(n) / O(Σ)` — counter equality.
- **Encode and Decode Strings** `O(n) / O(n)` — length-prefix each segment (`"5#hello"`).
- **Implement Trie** `O(1) per char` — map of children; `is_end` flag.
- **Word Search II** `O(m·n·4ᴸ)` — trie + DFS from each grid cell.

## Simulation / "small but careful"

These look easy and are commonly asked because they expose careful coding:

- **FizzBuzz** — conditional chain; mind the order.
- **Reverse Integer (with overflow)** — repeatedly `% 10`; check bounds.
- **String to Integer (atoi)** — trim, sign, accumulate, clamp.
- **Roman to Integer / Integer to Roman** — greedy with paired tokens.
- **Spiral Matrix** — track 4 boundaries, peel layer at a time.
- **Rotate Image** — transpose then reverse rows.
- **Set Matrix Zeroes** — use first row/col as in-place markers.
- **Pow(x, n)** — fast exponentiation; halve `n`, square `x`.
- **Reservoir Sampling** — pick item `i` with probability `1/i` (uses `random.randint`).
- **Shuffle an Array (Fisher-Yates)** — swap `i` with random `j ∈ [i, n-1]`.

## A 20-problem rehearsal set

If time is short, drill these 20 (one per pattern, mostly easy/medium):

1. Two Sum
2. Valid Palindrome
3. Best Time to Buy and Sell Stock
4. Valid Parentheses
5. Binary Search
6. Reverse Linked List
7. Merge Two Sorted Lists
8. Linked List Cycle
9. Invert Binary Tree
10. Maximum Depth of Binary Tree
11. Validate BST
12. Binary Tree Level Order Traversal
13. Number of Islands
14. Climbing Stairs
15. House Robber
16. Coin Change
17. Longest Substring Without Repeating Characters
18. Kth Largest Element in an Array
19. Subsets
20. Merge Intervals

Time-box yourself: 20 minutes for easy, 30 for medium. After each, write down the pattern, complexity, and one bug you almost made.
