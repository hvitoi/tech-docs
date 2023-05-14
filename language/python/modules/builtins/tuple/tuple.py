foo = tuple(("a", "b"))
coordinates = (4, 5)
coordinates = [(4, 5), (6, 7), (80, 34)]
spatial = (1, 2, 3)

# access
spatial[0]  # 1

# writes (not allowed!)
# Tuples are constant, they cannot be changed
spatial[0] = 9  # exception!
