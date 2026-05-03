# Daily Temperatures

> [LeetCode #739](https://leetcode.com/problems/daily-temperatures/) — Medium

Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Examples

### Example 1

```text
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

### Example 2

```text
Input:  temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
```

### Example 3

```text
Input:  temperatures = [30, 60, 90]
Output: [1, 1, 0]
```

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## What to practise

- Monotonic decreasing stack of **indices** (not values).
- For each new day, pop every index whose temperature is less than today's; for each popped index `j`, set `answer[j] = i - j`.
- Each index is pushed and popped at most once → amortised `O(n)`.
