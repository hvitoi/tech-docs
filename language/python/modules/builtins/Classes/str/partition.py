# Returns a tuple of 3 elements of string broken down on the first separator
#
# %%
"a;bc;d".partition(";")

# %%
# No separator found
"abcd".partition(";")
