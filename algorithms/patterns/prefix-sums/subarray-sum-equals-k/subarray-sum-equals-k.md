# Subarray Sum Equals K

> [LeetCode #560](https://leetcode.com/problems/subarray-sum-equals-k/) — Medium

Given an array of integers `nums` and an integer `k`, return *the total number of subarrays whose sum equals to `k`*.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

## Examples

### Example 1

```text
Input:  nums = [1, 1, 1], k = 2
Output: 2
```

### Example 2

```text
Input:  nums = [1, 2, 3], k = 3
Output: 2
Explanation: Subarrays [1, 2] and [3].
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Watch out

- Values can be **negative** — sliding window does **not** work here. You need prefix sum + hash map.
- A subarray summing to `k` means `prefix[j] - prefix[i] = k`, i.e. for each `prefix[j]` you want to count how many earlier `prefix[i]` equal `prefix[j] - k`.

## What to practise

- Maintain a `Counter` of prefix sums seen so far, seeded with `{0: 1}` (the empty prefix).
- For each new running sum `cur`, add `seen[cur - k]` to the answer, then increment `seen[cur]`.
- This is the canonical *prefix-sum + hash* gotcha — the entire reason prefix sums exist as a pattern beyond plain range-sum queries.
