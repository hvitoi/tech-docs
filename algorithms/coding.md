# Live coding

## Clarifying questions

- **Types**
  - Are the elements of the list of the same type?
  - array? string? stream? object?

- **Bounded values**
  - Positive only? Integer? Floats? Unicode?
  - Does it contain negative numbers?

- **Input size**
  - What is the size range of the input? (10? 10⁹? unbounded?)

- **List**
  - Does the list contain duplicates?
  - Can it be empty?
  - Is the list sorted?

- **Invalid input**
  - What should happen on invalid input — raise, return sentinel, undefined?

- **In-place?**
  - Can I modify the input in place?

- **Time/space constraints**
  - Is `O(n²)` acceptable for `n=1000`?

## Communication patterns

- **Think aloud.** Silence reads as "stuck." A weak idea spoken is better than a strong idea hidden.
- **Signal transitions.** "OK, I think I have an approach — let me describe it before I code." "I'm going to test this now."
- **Name your tradeoffs.** "Hash map gives O(1) lookup at the cost of O(n) extra space — acceptable here?"
- **Own your mistakes.** "Wait — this fails on an empty array. Let me fix the guard." This is a positive signal, not a negative one. The interviewer is watching for self-correction.
- **Don't argue.** If the interviewer hints at a bug, take the hint, verify on paper, then fix.

## Complexity cheatsheet for live use

- Constraints suggest the target complexity:
  - `n ≤ 10`: factorial / exponential is fine — backtracking, brute force.
  - `n ≤ 20`: `O(2^n)` bitmask DP.
  - `n ≤ 1_000`: `O(n²)` is fine.
  - `n ≤ 100_000`: aim for `O(n log n)` or `O(n)`.
  - `n ≤ 10⁹`: `O(log n)` or math.
- Don't forget **space**: recursion stack is `O(depth)`; copying inputs is `O(n)`; memoization tables are `O(states)`.
- Hash-map lookups are *amortized* O(1) — say "amortized" when you mention it.

## Testability

1. **Write a couple of asserts** alongside or below your function. Even 3 lines of `assert f([1,2,3]) == 6` shows you think in cases.
2. **Walk through the code** with a concrete input, tracing each variable.
3. **Cover edge cases verbally** even if you don't write them all: empty, single element, duplicates, all-same, sorted, reverse-sorted, max size, negative, zero.
4. If they ask "how would you test this in production?" — mention property-based tests, fuzzing, and the boundary between unit-of-logic and integration tests.
