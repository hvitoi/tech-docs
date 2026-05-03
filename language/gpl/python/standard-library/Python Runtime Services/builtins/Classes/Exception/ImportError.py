# %%
# ImportError -- Exception -- BaseException
#   └── ModuleNotFoundError
#
# ImportError: import statement had a problem (module found, but importing it
#              failed -- e.g. broken module body, missing symbol in `from X import Y`).
# ModuleNotFoundError (3.6+): the module itself could not be located.

import nonexistent_module  # ModuleNotFoundError: No module named 'nonexistent_module'

from os import nonexistent  # ImportError: cannot import name 'nonexistent' from 'os'

# %%
# Attributes
try:
    import nope
except ImportError as e:
    e.name  # 'nope'
    e.path  # None (or the file path, for body-level failures)
    e.msg  # str(e)

# %%
# Common idiom: optional dependency
try:
    import ujson as json
except ImportError:
    import json  # fall back to stdlib


# %%
# Lazy / conditional import inside a function -- error surfaces at call time,
# not at module load. Useful for heavy or platform-specific deps.
def use_pandas(df):
    import pandas as pd  # ModuleNotFoundError only if this function runs

    return pd.DataFrame(df)


# %%
# importlib alternative (when the name is dynamic)
import importlib

mod = importlib.import_module("json")  # raises ModuleNotFoundError on failure
