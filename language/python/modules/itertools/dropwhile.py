# %%
import itertools

it = itertools.dropwhile(
    lambda el: el != "c",
    ["a", "b", "c", "d"],
)

list(it)
