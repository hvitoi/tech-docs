# %%
# __eq__:  defines value equality (==).
# __hash__: required if you define __eq__ AND want the object to be
#           usable in sets / as dict keys.
#
# Contract: a == b  ==>  hash(a) == hash(b)
#
# Defining __eq__ alone makes the class UNHASHABLE
# (Python automatically sets __hash__ = None).


from collections.abc import Hashable


class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def __eq__(self, other):
        if not isinstance(other, Color):
            return NotImplemented
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)

    def __hash__(self):
        return hash((self.r, self.g, self.b))

    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"


red1 = Color(255, 0, 0)
red2 = Color(255, 0, 0)
blue = Color(0, 0, 255)

red1 == red2  # True   (same RGB values)
red1 is red2  # False  (different objects in memory)
red1 == blue  # False

# Hashable -> usable in sets and dict keys
palette = {red1, red2, blue}  # duplicates collapse
len(palette)                  # 2

isinstance(red1, Hashable)    # True
