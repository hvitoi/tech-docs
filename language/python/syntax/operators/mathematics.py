# %%
# signal
-2.09
+2.09

# %%
# addition
1 + 1.1
None + 1  # throws!

# %%
# subtraction
1 - 1.1

# %%
# multiplication
1 * 3
2 * "ab"  # "abab"
2 * ["a", "b"]  # ["a", "b", "a", "b"]

2 * [[]]  # [[], []] watch out! It's reference to the same list
[[] for _ in range(2)]  # use this instead

# %%
# division
2 / 2  # outputs float
3 / 2  # outputs float

2 / 2 == 1  # True! (types are coerced)

# %%
# power
2**4

# %%
# math expressions
(2 + 3) * (5 + 5)

# %%
# rest
10 % 3

# %%
# quotient
10 // 3

# %%
"ab" > "aa"  # True
(9, 1) > (1, 9)  # true
