# %%
num = 2
num if num % 2 == 0 else -1

# %%
num = 3
num if num % 2 == 0 else -1

# %%
# Try to access an out of bound index
# LBYL (look before you leap)
myList = ["a", "b", "c"]
i = 3

myList[3] if i < len(myList) else None  # Returns None
