# %%
# The __call__ method makes an object "callable"
# Callable by itself means "any object you can call with ()" regardless of the number of args

from collections.abc import Callable  # Python 3.9+
# from typing import Callable # deprecated!


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


add5: Callable = Adder(5)
add5(10)  # 15
