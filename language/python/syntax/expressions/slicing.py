# Syntax [start:stop[:step]]
# %% START
foo = ["a", "b", "c", "d", "e"]
foo[2:]  # from index 2 (inclusive)
foo[-1:]  # from last index (inclusive)

# %% STOP
foo = ["a", "b", "c", "d", "e"]
foo[:2]  # until index 2 (exclusive)
foo[:-1]  # until last index (exclusive)
foo[:99]  # works! take until the very last

# %% START + STOP
foo = ["a", "b", "c", "d", "e"]
foo[1:3]  # from index 1 (inclusive) until index 3 (exclusive)
foo[3:1]  # empty
foo[99:99]  # empty array

# %% STEP
foo = ["a", "b", "c", "d", "e"]
foo[::2]  # the whole array in step 2
foo[::-1]  # the whole array in reverse

# %% Everything
foo = ["a", "b", "c", "d", "e"]
foo[:]  # the whole array
foo[:] = [el * 2 for el in foo]  # can be useful to modify an array in-place

# %% Matrix Slicing
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

p = (0, 1)
n = 2

# takes a n x n slice starting at position p
[row[p[1] : p[1] + n] for row in matrix[p[0] : p[0] + n]]
