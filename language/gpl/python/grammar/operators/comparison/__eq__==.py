# %%
7 == 3
int(7).__eq__(3)

# %%
"hi" == "bye"
str("hi").__eq__("bye")

# %%
{"a": 1} == {"a": 1}  # True
["a", "b", "c"] == ["a", "b", "c"]  # True

# %%
{"a": []} == {"a": []}  # True! Compares the values, not the object itself.
{"a": []} is {"a": []}  # False! Compares the values references, not only the values

[] == []  # True
[] is []  # False
