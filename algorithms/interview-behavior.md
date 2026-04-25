# Live coding interview prep

The goal is not to solve hard problems — it is to demonstrate clean fundamentals, structured thinking, communication, and self-debugging. Most loss happens to silence and to bugs the candidate didn't catch first.

## Structure

- **Understand** `3-5 min` — restate the problem in your words. Ask about input shape, size, edge cases (empty, negatives, duplicates, unicode), constraints, expected output. **Write down** 1-2 example inputs/outputs.
- **Plan** `3-5 min` — describe an approach in plain words. State time/space complexity. Explicitly ask: "is this acceptable, or should I aim for something better?"
- **Code** `15-20 min` — implement the agreed approach. Narrate as you go. Use clear names. Don't optimize prematurely.
- **Test** `5-8 min` — walk a small example through your code by hand. Then add edge cases (empty, single element, all-same, max size). Find and fix bugs **yourself** before the interviewer points them out.
- **Reflect** `2-3 min` — restate actual time/space complexity (it may differ from what you predicted). Propose at least one optimisation, even if you don't implement it.

## Clarifying questions to always ask

- What is the input type and shape? (array? string? stream? object?)
- What is the size range of the input? (10? 10⁹? unbounded?)
- Are values bounded? Positive only? Integer? Floats? Unicode?
- Can the input be empty? Can it contain duplicates? Be already sorted?
- What should happen on invalid input — raise, return sentinel, undefined?
- Is there one answer or many? If many, return any or all?
- Can I modify the input in place?
- Time/space constraints? Is `O(n²)` acceptable for `n=1000`?

Bad assumption you don't ask about → bug you'll trip on → less time to recover.

## Communication patterns that score

- **Think aloud.** Silence reads as "stuck." A weak idea spoken is better than a strong idea hidden.
- **Signal transitions.** "OK, I think I have an approach — let me describe it before I code." "I'm going to test this now."
- **Name your tradeoffs.** "Hash map gives O(1) lookup at the cost of O(n) extra space — acceptable here?"
- **Own your mistakes.** "Wait — this fails on an empty array. Let me fix the guard." This is a positive signal, not a negative one. The interviewer is watching for self-correction.
- **Don't argue.** If the interviewer hints at a bug, take the hint, verify on paper, then fix.

## Approach checklist (the "what pattern" decision tree)

When you read the problem, scan for these cues — they map directly to the topic dirs in this repo:

- *"contiguous subarray / substring with property X"* → **sliding window** — [sliding-window/](sliding-window/sliding-window.md)
- *"sorted array, find pair / triple summing to target"* → **two pointers** — [two-pointers/](two-pointers/two-pointers.md)
- *"find / count / smallest / largest in sorted (or monotonic) space"* → **binary search** — [binary-search/](binary-search/binary-search.md)
- *"frequency / count / has-seen lookup"* → **hash map / set** — [data-structures/map/](data-structures/map/hash-table.md)
- *"matching / nesting / most recent"* → **stack** — [data-structures/stack/](data-structures/stack/stack.md)
- *"level-by-level / shortest path in unweighted graph"* → **BFS (queue)** — [data-structures/queue/](data-structures/queue/queue.md), [traversal/](traversal/traversal.md)
- *"explore all paths / connected component"* → **DFS (recursion or stack)** — [traversal/](traversal/traversal.md)
- *"all combinations / permutations / partitions"* → **backtracking** — [backtracking/](backtracking/backtracking.md)
- *"min / max / count of ways to reach state X"* → **dynamic programming** — [dynamic-programming/](dynamic-programming/dynamic-programming.md)
- *"always pick the locally best"* → **greedy (prove it!)** — [greedy-algorithms/](greedy-algorithms/greedy-algorithms.md)
- *"k-th smallest / largest / streaming top-k"* → **heap** — [data-structures/tree/heap/](data-structures/tree/heap/)
- *"prefix lookup / autocomplete"* → **trie** — [data-structures/tree/trie/](data-structures/tree/trie/)

If two patterns fit, name both, then pick the simpler one.

## Complexity cheatsheet for live use

- Constraints suggest the target complexity:
  - `n ≤ 10`: factorial / exponential is fine — backtracking, brute force.
  - `n ≤ 20`: `O(2^n)` bitmask DP.
  - `n ≤ 1_000`: `O(n²)` is fine.
  - `n ≤ 100_000`: aim for `O(n log n)` or `O(n)`.
  - `n ≤ 10⁹`: `O(log n)` or math.
- Don't forget **space**: recursion stack is `O(depth)`; copying inputs is `O(n)`; memoization tables are `O(states)`.
- Hash-map lookups are *amortized* O(1) — say "amortized" when you mention it.

See [asymptotic-notation/](asymptotic-notation/time-complexity.md) for full reference.

## Testability

1. **Write a couple of asserts** alongside or below your function. Even 3 lines of `assert f([1,2,3]) == 6` shows you think in cases.
2. **Walk through the code** with a concrete input, tracing each variable.
3. **Cover edge cases verbally** even if you don't write them all: empty, single element, duplicates, all-same, sorted, reverse-sorted, max size, negative, zero.
4. If they ask "how would you test this in production?" — mention property-based tests, fuzzing, and the boundary between unit-of-logic and integration tests.

## Use of internal libraries

- **Random**: `random.randint`, `random.choice`, `random.sample`, `random.shuffle`, seeding for reproducibility.
- **Collections**: `dict`, `set`, `list`, `tuple`; `collections.Counter`, `defaultdict`, `deque`, `OrderedDict`.
- **Sorting**: `sorted(..., key=..., reverse=...)`, stability guarantees.
- **Heaps**: `heapq.heappush/heappop`, min-heap by default (negate for max-heap).
- **String**: `str.split`, `join`, `strip`, `lower`, `f-strings`, `''.join(...)`.
- **Iteration**: `enumerate`, `zip`, `map`, `filter`, `range`, list/dict/set comprehensions.
- **Numbers**: `math.inf`, `float('inf')`, `divmod`, `bin`, `int(s, base)`.

## Common bugs to self-catch

- Off-by-one in loop bounds (`<` vs `<=`, `n-1` vs `n`).
- Mutating a list while iterating it.
- Integer division vs float division (`/` vs `//` in Python).
- Returning inside a loop too early — missing later candidates.
- Hash map key collision when keys are mutable types.
- Forgetting to handle empty input, single-element input.
- Recursion without a base case → stack overflow.
- Using `==` for floating-point equality.
- BFS/DFS without a visited set → infinite loop on cyclic graphs.
- Sliding-window shrink using `if` instead of `while`.

When you find one yourself, *say so out loud* and fix it.

## Optimisation moves to suggest

Even if you don't implement, naming an optimisation closes the interview strongly:

- "We could pre-sort and use two pointers to drop the `O(n²)` to `O(n log n)`."
- "A hash map of seen values would let us skip the inner loop, trading space for time."
- "Memoization of the recursive call would dedupe overlapping subproblems."
- "If the input is a stream, we'd switch to a heap-of-size-k for streaming top-k."
- "Bit-packing the visited set would shrink memory if `n` is small."
- "Early exit once we've found `k` answers."

## The last minutes — questions to ask

This is part of the interview. Have 3-4 ready questions

- What does the developer feedback loop look like today — local build → CI → staging → prod?
- What metric do you watch to know dev productivity is improving?
- What's the most painful piece of internal tooling right now, and is it on the roadmap?
- How much of the work is platform-team coding vs. unblocking other teams?
- What does the on-call rotation look like for the platform team?
- How does the team balance shipping new tooling vs. maintaining what exists?
