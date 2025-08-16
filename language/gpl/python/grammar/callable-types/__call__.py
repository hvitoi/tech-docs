# %%
# The __call__ method makes an object "callable"


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


add5 = Adder(5)
add5(10)  # 15
