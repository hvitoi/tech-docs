# Group Anagrams

> [LeetCode #49](https://leetcode.com/problems/group-anagrams/) — Medium

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

## Examples

### Example 1

```text
Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

### Example 2

```text
Input:  strs = [""]
Output: [[""]]
```

### Example 3

```text
Input:  strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## What to practise

- Hash strings by a **canonical key** that is the same for all anagrams.
- Two common keys:
  - **Sorted-string** as the key — `O(n · k log k)`, simple.
  - **Count tuple** of length 26 (number of each letter) — `O(n · k)`, faster.
- This is the canonical *hash-by-derived-key* pattern.
