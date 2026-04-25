# Jump Game

> [LeetCode #55](https://leetcode.com/problems/jump-game/) — Medium

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your **maximum jump length** at that position.

Return `true` if you can reach the last index, or `false` otherwise.

## Examples

### Example 1

```text
Input:  nums = [2, 3, 1, 1, 4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### Example 2

```text
Input:  nums = [3, 2, 1, 0, 4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
             which makes it impossible to reach the last index.
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## What to practise

- Greedy: track the **furthest index reachable so far**. Iterate through the array; at each `i`, if `i > furthest`, return `false`. Otherwise update `furthest = max(furthest, i + nums[i])`.
- Stop early if `furthest >= len(nums) - 1`.
- Why is greedy correct? At each position you have full information about reach; locally extending the max can never hurt.
