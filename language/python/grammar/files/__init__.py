# This file signalizes that a folder is actually a package
# Before Python 3.3, you had to have __init__.py in a folder for it to be considered a package.
# Today it’s technically optional for basic importing, but it’s still common practice because:
#   - It signals “this is a package”
#   - You can define what gets imported when you import routers (via __all__)
#   - You can run setup code when the package is imported.

# ... import only select files
# from . import users, items

