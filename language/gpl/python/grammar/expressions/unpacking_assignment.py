# %%
one, two, three = [1, 2, 3]

one
two
three

# %%
# with rest
# similar to "&" in Clojure
one, two, three, *rest = [1, 2, 3, 4, 5]

one
two
three
rest

# %%
# Unpacking a tuple
one, two, three = 1, 2, 3

# %%
a = 1
b = 2
a, b = b, a  # swap values
