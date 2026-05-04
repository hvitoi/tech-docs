# %%
# `abc` -- Abstract Base Classes. Python's way of declaring "interfaces".
# A class is abstract if it has at least one @abstractmethod; it can't be
# instantiated until a subclass implements them. Checked at instantiation,
# not at call time.
#
# Pieces:
#   ABC               -- base class to inherit from (preferred)
#   ABCMeta           -- the metaclass behind ABC. Use directly only if you
#                        need to combine ABC with another custom metaclass.
#   @abstractmethod   -- marks a method as required (see Decorators/)
#   .register(cls)    -- declares a virtual subclass (see Functions/)

# %%
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    # Using Ellipsis is common for an abstract method. Alternatively use "pass"


# Shape() # TypeError: Can't instantiate abstract class


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r * self.r


Circle(2).area()  # 12.566...


# %%
# Concrete methods and __init__ are fine on an ABC. Only @abstractmethod is required.
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self) -> str: ...

    def greet(self):  # concrete, inherited as-is
        return f"{self.name} says {self.sound()}"


class Dog(Animal):
    def sound(self):
        return "woof"


Dog("Rex").greet()  # 'Rex says woof'

# %%
# `collections.abc` is where the *standard* ABCs live -- Iterable, Iterator,
# Sized, Container, Mapping, Sequence, Hashable, Callable, ...
# Built-ins (list, dict, str, ...) match them via __subclasshook__,
# so isinstance(x, Iterable) works without any registration.
from collections.abc import Iterable, Sized

isinstance([1, 2], Iterable)  # True
isinstance("hey", Sized)  # True (has __len__)
