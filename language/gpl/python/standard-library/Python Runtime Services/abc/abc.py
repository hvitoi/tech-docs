# %%
# `abc` -- Abstract Base Classes
#
# Python's way of declaring "interfaces". An ABC is a class you can't instantiate
# directly; subclasses MUST implement methods marked @abstractmethod.
# Validation happens at instantiation time, not at call time.
#
# Two pieces, almost always used together:
#   - ABC               -- a base class to inherit from (preferred)
#   - ABCMeta           -- the metaclass (use directly only if you already have
#                          a different metaclass; ABC is just `class ABC(metaclass=ABCMeta)`)
#   - @abstractmethod   -- decorator that marks a method as required
#   - .register(cls)    -- declares a class is a "virtual subclass" without inheritance

# %%
# Minimal example
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def name(self) -> str: ...


# Shape()                          # TypeError: Can't instantiate abstract class Shape
#                                  # without an implementation for abstract methods
#                                  # 'area', 'name'


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r * self.r

    def name(self):
        return "circle"


Circle(2).area()  # 12.566... -- ok, all abstract methods implemented


# %%
# Partial implementation -> still abstract -> still can't instantiate
class Square(Shape):
    def area(self):
        return 1


# Square()                         # TypeError: missing 'name'

# %%
# isinstance / issubclass work as you'd expect via inheritance
isinstance(Circle(1), Shape)  # True
issubclass(Circle, Shape)  # True

# %%
# Concrete methods are fine on an ABC -- only @abstractmethod ones are required
class Animal(ABC):
    @abstractmethod
    def sound(self) -> str: ...

    def greet(self):  # concrete, inherited as-is
        return f"hello, I say {self.sound()}"


class Dog(Animal):
    def sound(self):
        return "woof"


Dog().greet()  # 'hello, I say woof'

# %%
# `collections.abc` is where the *standard* ABCs live -- Iterable, Iterator,
# Sized, Container, Mapping, Sequence, Hashable, Callable, ...
# These are what `isinstance(x, Iterable)` checks against. Most use
# __subclasshook__ so any class with the right dunder methods is accepted.
from collections.abc import Iterable, Sized

isinstance([1, 2], Iterable)  # True
isinstance("abc", Sized)  # True (has __len__)
