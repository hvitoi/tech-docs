# %%
# args and kwargs (and optional ones)
# "*"" mark the start of keyword-only arguments (kwargs)
def args_and_kwargs(x, y=None, *, foo, bar=None):
    # "x" and "y" can be passed positionally or as keywords
    # "foo" and "bar" can only be passed as keywords
    return (x, y, foo, bar)


args_and_kwargs("a", foo="d", y="b")
args_and_kwargs("a", "b", "c")

# %%

# You can also define function args without the "*", this way the arguments can be passed positionally or as keywords


def do_something2(a, b):
    return a, b


# The order of the parameters paramters
do_something2(1, 2)  # (1, 2)
do_something2(b=1, a=2)  # (2, 1)

# %%
# rest of args and kwargs


def args_and_kwargs(x, y, *args, foo, bar, **kwargs):
    # args as tuple
    print(args)

    # kwargs as dict
    print(kwargs)


args_and_kwargs(1, 2, 3, 4, foo=5, bar=6, baz=7, biz=8)


# %%
# args and kwargs, rests and defaults
def everything_mixed_up(x, y, z=None, *args, foo, bar=None, baz, **kwargs):
    return (x, y, z, args, foo, bar, baz, kwargs)


everything_mixed_up("x", "y", foo="foo", baz="baz")  # bare minimum
