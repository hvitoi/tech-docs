# %%
# __repr__: unambiguous, debug-friendly representation.
#           Shown in the REPL and inside lists/dicts.
#           Goal: eval(repr(x)) == x  (when reasonable).
#
# __str__:  human-readable string. Used by print() and str().
#           Falls back to __repr__ if not defined.
#
# Always define __repr__ for any non-trivial class — it's free debugging.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"


p = Point(3, 5)

repr(p)   # 'Point(x=3, y=5)'
str(p)    # '(3, 5)'
print(p)  # (3, 5)
[p]       # [Point(x=3, y=5)]   ← lists show __repr__ of each element
