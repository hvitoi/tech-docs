# Tuples are constant, they cannot be changed

# %%
coordinate_2d = (1, 2)
coordinate_3d = (3, 4, 5)

# access
coordinate_2d[0]  # 1
coordinate_2d[1]  # 2

# writes (not allowed!)
# coordinate_2d[0] = 9  # exception!

# %%
# list -> tuple
my_tuple = tuple(["a", "b"])
my_tuple
