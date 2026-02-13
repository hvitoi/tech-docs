# %%
a = 6  # 0000 0110
b = 12  # 0000 1100

# %%
# AND
a & b  # 0000 0100 (4)
a.__and__(b)

# %%
# OR
# With bitwise OR, both sides are always evaluated (no short-circuit)
a | b  # 0000 1110 (14)
a.__or__(b)

# %%
# XOR
a ^ b  # 0000 1010 (10)

# %%
# NOT
~a  # -0000 0111 (-7)

# %%
# SHIFT LEFT
a << 1  # 0000 1100 (12)

# %%
# SHIFT RIGHT
a >> 1  # 0000 0011 (3)

# %%
# Summing two numbers
(a ^ b) + ((a & b) << 1)
