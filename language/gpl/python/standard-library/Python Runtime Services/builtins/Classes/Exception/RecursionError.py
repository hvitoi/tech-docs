# %%
# RecursionError -- RuntimeError -- Exception -- BaseException
#
# Maximum recursion depth exceeded. Default limit is 1000 (CPython).


def f():
    return f()


f()  # RecursionError: maximum recursion depth exceeded

# %%
# Inspect / change the limit
import sys

sys.getrecursionlimit()  # 1000
sys.setrecursionlimit(5000)  # raise it (risk: C-stack overflow -> hard crash)


# %%
# The fix is almost never raising the limit -- convert recursion to iteration,
# or use an explicit stack.
def fact_iter(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out
