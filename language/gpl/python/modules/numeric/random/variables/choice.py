# %%
import random

options = ["red", "blue", "green"]
random.choice(options)

options2 = {"a": 1, "b": 2, "c": 3}
random.choice(list(options2))  # a random k
random.choice(list(options2.items()))  # a random (k, v)
