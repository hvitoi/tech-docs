# %%
1 > 2
1 < 2
1 >= 1
1 <= 4
1 == 1
1 != 3
"hi" == "bye"

# %%
{"a": 1} == {"a": 1}  # True
["a", "b", "c"] == ["a", "b", "c"]  # True

# %%
{"a": []} == {"a": []}  # True! Compares the values, not the object itself.
{"a": []} is {"a": []}  # False! Compares the values references, not only the values

[] == []  # True
[] is []  # False
