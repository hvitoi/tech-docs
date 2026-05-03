# Merge Intervals

> [LeetCode #56](https://leetcode.com/problems/merge-intervals/) — Medium

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

## Examples

### Example 1

```text
Input:  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Explanation: Since intervals [1, 3] and [2, 6] overlap, merge them into [1, 6].
```

### Example 2

```text
Input:  intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]
Explanation: Intervals [1, 4] and [4, 5] are considered overlapping.
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## What to practise

- Sort by `start`. Walk the sorted intervals, maintaining a current merged interval `[s, e]`.
- For each next interval `[ns, ne]`: if `ns <= e`, extend (`e = max(e, ne)`); otherwise emit `[s, e]` and start a new one.
- This is the **template** for the entire intervals family (insert-interval, non-overlapping-intervals, meeting-rooms).
- Watch the touching case: are `[1, 4]` and `[4, 5]` overlapping? In this problem, **yes**.
