# %%
a = 6  # 0000 0110
b = 12  # 0000 1100

# bitwise "AND"
a & b  # 0000 0100 (4)
a.__and__(b)

# %%
# set intersection
{1, 2} & {2, 3}
set({1, 2}).__and__({2, 3})

# %%
# Summing two numbers
(a ^ b) + ((a & b) << 1)
