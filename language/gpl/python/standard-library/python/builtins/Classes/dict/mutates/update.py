# %%
my_dict = {"a": 1, "b": 2, "c": 3}

my_dict.update({"a": 9, "z": 99})

my_dict

# %%
# Equivalent to Clojure's "assoc"

my_dict = {"a": 1, "b": 2, "c": 3}

# Update without mutating the original map
my_updated_dict = {**my_dict, "a": 9, "z": 99}
my_updated_dict

# %%
# Equivalent to Clojure's "dissoc"

my_dict = {"a": 1, "b": 2, "c": 3}

# Update without mutating the original map
my_updated_dict = {k: v for k, v in my_dict.items() if k not in ("b", "c")}
my_updated_dict
