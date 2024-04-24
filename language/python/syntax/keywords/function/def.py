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
sum_nums()  # take default values


# %%
# Keyword arguments
# asterisk marks the start of keyword arguments


def foo(x, y, *, z):
    return z


# ... *args also mark the start of kwargs
def foo2(x, y, *args, z):
    return z


foo("a", "b", z="c")


# %%
# yield is another kind of "return"
def my_movie_splitter(line):
    (userId, movieId, rating, timestamp) = line.split("\t")
    yield userId, movieId


# %%
# Side Effects & Pointers

nums = []


def fn_with_side_effects(arr: list) -> None:
    arr.append("a")


def fn_with_side_effects2() -> None:
    nums.append("b")


fn_with_side_effects(nums)
fn_with_side_effects2()
nums


# %%
# Prevent side effects
import copy

nums = ["a"]


def fn_without_side_effects(arr: list) -> list:
    arr = copy.deepcopy(arr)
    arr.append("b")
    return arr


fn_without_side_effects(nums)

nums  # original array untouched


# %%
# args and kwargs (and optional ones)
def args_and_kwargs(x, y=None, *, foo, bar=None):
    return (x, y, foo, bar)


args_and_kwargs("a", foo="b")


# %%
# rest of args and kwargs
def foo_args(x, y, *args):
    return args  # a list of extra arguments


def foo_kwargs(x, y, **kwargs):
    return kwargs  # a map of extra keyword arguments


foo_args("a", "b", "c", "d")
foo_kwargs("a", "b", foo=1, bar=2)


# %%
# args and kwargs, rests and defaults
def everything_mixed_up(x, y, z=None, *args, foo, bar=None, baz, **kwargs):
    return (x, y, z, args, foo, bar, baz, kwargs)


everything_mixed_up("x", "y", foo="foo", baz="baz")  # bare minimum


# %%
# The default value is created ONCE at the function definition
# Do not use mutable data types (references) as default arguments because they are remembers across function calls. This may lead to strange behaviors


def append_num(num, nums=[]):
    nums.append(num)
    return nums


append_num(1)
append_num(2)


# %%
# Modifying the arguments received
def modify_list(ls: list) -> None:
    ls.append("d")  # works! (in-place modification)


def modify_list_again(ls: list) -> None:
    ls[:] = ls + ["e"]  # works! (in-place modification)


def try_to_modify_list(ls: list) -> None:
    ls = ["z"]  # does not work! Reassigns only the local pointer


my_list = ["a", "b", "c"]
modify_list(my_list)
modify_list_again(my_list)
modify_list(my_list)
my_list
