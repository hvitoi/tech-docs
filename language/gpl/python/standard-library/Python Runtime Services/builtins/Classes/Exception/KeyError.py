# %%
# KeyError -- LookupError -- Exception -- BaseException
#
# Mapping key not found. Raised by dict[k], set member lookups for missing items,
# and any Mapping-protocol __getitem__.

{"a": 1}["z"]  # KeyError: 'z'

# %%
# str(KeyError("z")) == "'z'"  -- it quotes the key. This is unique to KeyError
# and surprises people. Use e.args[0] to get the raw key.
try:
    {"a": 1}["z"]
except KeyError as e:
    e.args[0]  # 'z'  (raw)
    str(e)  # "'z'"  (with quotes!)

# %%
# Avoid by using .get / .setdefault / "in"
d = {"a": 1}
d.get("z")  # None, no raise
d.get("z", 0)  # 0, default
"z" in d  # False
d.setdefault("z", [])  # inserts [] if missing, returns it

# %%
# collections.defaultdict avoids KeyError on read (auto-creates the value)
from collections import defaultdict

counts = defaultdict(int)
counts["x"] += 1  # no KeyError
