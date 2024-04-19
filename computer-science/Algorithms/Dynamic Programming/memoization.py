# %%
def memoize(fn):
    memo = {}

    def lookup_or_miss(*args):
        if args not in memo:
            memo[args] = fn(*args)
        return memo[args]

    return lookup_or_miss


def square(n):
    print(f"Calculating square of {n}...")
    return n * n


# Function is called multiple times but calculated only once
memoized_square = memoize(square)
memoized_square(3)
memoized_square(3)
memoized_square(3)
