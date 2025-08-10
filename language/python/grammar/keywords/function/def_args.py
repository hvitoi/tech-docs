# %%
# Function with default parameters
# Default parameters must be the last ones (except on kwargs, which doesn't matter the order)
def sum_nums(num1, num2=20, num3=30):
    """
    This function does X
    """
    return num1 + num2 + num3


# Types are optional
def subtract_nums(num1: int = 10, num2: int = 20, num3: int = 30) -> int:
    return num1 - num2 - num3


# Return tuples
def do_something(x, y) -> tuple:
    return x, y


sum_nums(1, 2, 3)
sum_nums(10)  # take default values

# %%
# The default value is created ONCE at the function definition
# Do not use mutable data types (references) as default arguments because they are remembers across function calls. This may lead to strange behaviors

def append_num(num, nums=[]):
    nums.append(num)
    return nums


append_num(1)
append_num(2)
