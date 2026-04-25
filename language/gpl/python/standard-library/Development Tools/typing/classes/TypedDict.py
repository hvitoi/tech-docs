# %%
from typing import TypedDict

# It's just a type checker at the IDE. At runtime it's not validated


class User(TypedDict):
    name: str
    age: int


u: User = {"name": "Alice", "age": 30}
