# %%
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    age: int


person = Person("John", 21)

person.first_name
person.age
