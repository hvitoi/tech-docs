# House Robber

> [LeetCode #198](https://leetcode.com/problems/house-robber/) — Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that **adjacent houses have security systems connected** and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money in each house, return the **maximum amount of money** you can rob tonight **without alerting the police**.

## Examples

### Example 1

```text
Input:  nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.
```

### Example 2

```text
Input:  nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 (money = 2), house 3 (money = 9) and house 5 (money = 1). Total = 2 + 9 + 1 = 12.
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## What to practise

- Define `dp[i]` = max money robbing houses `[0..i]`.
- Recurrence: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` — at each house, either skip it or take it (and skip the previous).
- Optimise to `O(1)` space by keeping only the two most recent values.
- This is the canonical *skip-or-take* 1D DP, distinct from Fibonacci's "always combine".
