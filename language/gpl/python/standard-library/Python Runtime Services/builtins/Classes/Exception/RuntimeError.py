# %%
# RuntimeError -- Exception -- BaseException
#
# Generic "something went wrong at runtime and no other built-in fits".
# Catch-all when you want to signal an error but none of ValueError/TypeError/
# LookupError/OSError describe the situation. Many libraries subclass it.

raise RuntimeError("invariant violated")

# %%
# Real cases the interpreter raises RuntimeError for:

# Mutating a dict while iterating
d = {"a": 1, "b": 2}
for k in d:
    d[f"{k}_x"] = 0  # RuntimeError: dictionary changed size during iteration

# generator returning from inside a yield-from chain when async/sync mixed,
# or `asyncio.run()` called when a loop is already running

# %%
# Subclasses you'll see often:
# - NotImplementedError  -> abstract-method placeholder
# - RecursionError       -> max recursion depth exceeded
# (See NotImplementedError.py and RecursionError.py)
