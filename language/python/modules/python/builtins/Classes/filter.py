# Returns an iterator
# %%
v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
it = filter(lambda el: el % 2 == 0, v)
list(it)

# %%
m = {"a": 1, "b": 2, "c": 3}
it = filter(lambda kv: kv[0] != "b", m.items())
dict(it)
