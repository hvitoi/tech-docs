# %%
from dataclasses import dataclass


# It's designed to make it easier to create classes that are mainly used to store data
# without having to write a lot of boilerplate code (like __init__, __repr__, __eq__, etc.).
@dataclass
class Point:
    x: int
    y: int


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)  # Point(x=1, y=2)
print(p1 == p2)  # True

# %%

# same example without dataclass


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)  # Point(x=1, y=2)
print(p1 == p2)  # True
