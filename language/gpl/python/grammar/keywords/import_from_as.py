# %%
import math
import math as fancy_math  # with alias

math.cos(0)

# %%
# Select symbols
from math import ceil, floor
from math import ceil as my_ceil


# %%
# Python will look in the package's "__init__.py" for a special variable called __all__.
# If __all__ exists, only the names listed there will be imported.
from math import *

# %%
# Absolute import (file/package)
# If you are absolute importing from within a "python package" (with __init__.py file), you need to specify the full path (e.g., <package>.import_example)
# If you are absolute importing from outside of a "python package", you need to specify the file name (e.g., import_example)

# "import_example" is the filename of a python file in the same dir as this file without the ".py" extension
import import_example  # you need to run using the python commandline

import_example.do_something()

# %%
# Relative import (file/package)
# In order to use relative imports, the file/module must be part of a "python package"
# In order to do that, the parent directory must contain an __init__.py file

# Suppose the absolute path of this module/file is "app.mypackage1.mypackage2.mypackage3.somemodule"
import mymodule  # app.mypackage1.mypackage2.mypackage3.mymodule
from .otherpackage import mymodule  # app.mypackage1.mypackage2.otherpackage.mymodule
from ..otherpackage import mymodule  # app.mypackage1.otherpackage.mymodule
from ...otherpackage import mymodule  # app.otherpackage.mymodule
from ...otherpackage.anotherpackage import (
    mymodule,
)  # app.otherpackage.anotherpackage.mymodule

# you can also import the symbols!
from .otherpackage.mymodule import do_something
