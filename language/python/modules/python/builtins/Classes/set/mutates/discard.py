# same as "remove", but does not throw if not found

# %%
my_set = {"a", "b", "c"}

my_set.discard("a")
my_set.discard("a")  # ignores

my_set
