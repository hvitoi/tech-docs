# Returns the memory address of a variable

# %%
# Shallow Copy
foo1 = [["a", "b", "c"], [1, 2, 3]]
foo2 = foo1[:]

# Different ids for root-level object
print(id(foo1))
print(id(foo2))

# Same ids for the nested objects
print(id(foo1[0]))
print(id(foo2[0]))


# %%
# Deep copy
import copy

foo1 = [["a", "b", "c"], [1, 2, 3]]
foo2 = copy.deepcopy(foo1)

print(id(foo1))
print(id(foo2))

print(id(foo1[0]))
print(id(foo2[0]))
