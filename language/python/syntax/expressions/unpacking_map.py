## Splat Operator
## The elements of a list/map are broken into individual elements
# Just like the spread operator (...) in javascript

# %%
from itertools import accumulate

options = {"initial": 10}
list(accumulate([1, 2, 3, 4, 5], **options))
list(accumulate([1, 2, 3, 4, 5], initial=10))  # same
