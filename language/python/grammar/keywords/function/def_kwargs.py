# %%
# args and kwargs (and optional ones)
# "*"" mark the start of kwargs
def args_and_kwargs(x, y=None, *, foo, bar=None):
    return (x, y, foo, bar)


args_and_kwargs("a", foo="b")

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
