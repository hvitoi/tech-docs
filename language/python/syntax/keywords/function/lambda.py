# lambda expressions (Anonymous function)
# Syntax: lambda <inputs>: output

# %%
lambda num: num**2  # square = lambda num: num**2
lambda x: x % 2 == 0  # is even
lambda s: s[0]  # grab first char
lambda s: s[::-1]  # reverse string
lambda x, y: x + y  # adder

# %
# lambda with no args
lambda: print("hello")
