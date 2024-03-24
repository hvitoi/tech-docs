# Mutates and returns None

# Inserts an element before the index
# All the elements after need to be shifted (copied) into a higher index
# O(n) at worst scenario (inserting at the beginning of the list)

# %%
my_list = ["a", "c"]
my_list.insert(1, "b")
my_list
