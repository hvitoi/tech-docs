# %%
# StopIteration -- Exception -- BaseException
#
# Iterators raise this from __next__() to signal "no more items".
# `for` loops catch it transparently. You normally never see it.

it = iter([1, 2])
next(it)  # 1
next(it)  # 2
next(it)  # StopIteration

# %%
# next() with a default avoids the raise
next(iter([]), "fallback")  # 'fallback'


# %%
# Generators: `return value` becomes StopIteration(value)
def gen():
    yield 1
    return "done"


g = gen()
next(g)  # 1
try:
    next(g)
except StopIteration as e:
    e.value  # 'done'


# %%
# PEP 479 (3.7+): a StopIteration raised inside a generator body is converted
# to RuntimeError to prevent silently terminating the generator.
def buggy():
    yield 1
    next(iter([]))  # raises StopIteration -> becomes RuntimeError


# list(buggy())             # RuntimeError: generator raised StopIteration

# %%
# StopAsyncIteration is the async analogue, raised from __anext__().
