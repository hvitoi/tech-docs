# Syntax [start:stop[:step]]

# %%
foo = ["a", "b", "c", "d", "e"]
foo[2:]  # from index 2 (inclusive)
foo[-1:]  # from last index (inclusive)

# %%
foo = ["a", "b", "c", "d", "e"]
foo[:2]  # until index 2 (exclusive)
foo[:-1]  # until last index (exclusive)
foo[:99]  # works, take until the very last

# %%
foo = ["a", "b", "c", "d", "e"]
foo[1:3]  # from index 1 (inclusive) until index 3 (exclusive)
foo[3:1]  # empty

# %%
foo = ["a", "b", "c", "d", "e"]
foo[:]  # the whole array
foo[::1]  # same (step 1)

# %%
foo = ["a", "b", "c", "d", "e"]
foo[::2]  # the whole array in step 2

# %%
foo = ["a", "b", "c", "d", "e"]
foo[::-1]  # the whole array in reverse

# %%
# Simple access
foo = ["a", "b", "c", "d", "e"]
foo[0]
foo[-1]
foo[-2]
# foo[5]  # Throws!
