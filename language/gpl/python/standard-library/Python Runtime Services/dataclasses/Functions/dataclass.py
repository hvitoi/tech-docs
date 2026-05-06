# %%
from dataclasses import dataclass, field
from uuid import UUID, uuid4


# It's designed to make it easier to create classes that are mainly used to store data
# without having to write a lot of boilerplate code (like __init__, __repr__, __eq__, etc.).
@dataclass
class Point:
    x: int
    y: int

    # force it to be passed as a kw arg (not positional)
    z: int | None = field(default=None, kw_only=True)

    # my_list = []  # forbidden! (dataclass explicitly forbids mutable defaults)
    my_list: list = field(default_factory=list)  # correct way to instantiate lists


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

# %%

# Data Classes can have methods too!


@dataclass
class Account:
    account_id: UUID = field(default_factory=uuid4)
    balance: int = 0

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> bool:
        if self.balance < amount:
            return False
        self.balance -= amount
        return True

    def get_balance(self) -> int:
        return self.balance
