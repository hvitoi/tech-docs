# %%
# Import package
import math

math.cos(0)

# %%
# Import with alias
import math as fancy_math

# %%
# Select specific symbols
from math import ceil, floor

# %%
#  Select all

# Python will look in the package's "__init__.py" for a special variable called __all__.
# If __all__ exists, only the names listed there will be imported.

from math import *

# %%
# Import python file

# In order to run it you need to run this file using the python commandline
import import_example  # the filename of the other python file without the ".py" extension

import_example.do_something()

# %%
# Import python folder
