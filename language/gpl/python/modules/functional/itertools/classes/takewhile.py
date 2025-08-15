# %%
import itertools

# Opposite of dropwhile
it = itertools.takewhile(
    lambda el: el != "c",
    ["a", "b", "c", "d"],
)

list(it)
