# %%
# Checks if a value is present in a list, tuple, etc.
# right-hand side argument must be an iterator
"a" in ["a", "b", "c"]  # True
"a" in {"a": 1}  # True
"a" in {1: "a"}  # False
"a" in ("c", "a")  # True
"a" in ("a", 1)  # True
"a" in (1, "a")  # True
"a" in {"a"}  # True
