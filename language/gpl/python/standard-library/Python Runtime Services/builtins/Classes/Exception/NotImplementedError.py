# %%
# NotImplementedError -- RuntimeError -- Exception -- BaseException
#
# Marks an abstract method or a not-yet-implemented code path.
# DO NOT confuse with the singleton `NotImplemented`, which is what operator
# dunders return to signal "I don't handle this operand" (see TypeError.py).


class Shape:
    def area(self):
        raise NotImplementedError("subclasses must implement area()")


class Circle(Shape):
    def area(self):
        return 3.14


# %%
# Prefer abc.ABC + @abstractmethod -- it fails at instantiation, not at call.
from abc import ABC, abstractmethod


class Shape2(ABC):
    @abstractmethod
    def area(self): ...


# Shape2()                  # TypeError: Can't instantiate abstract class
