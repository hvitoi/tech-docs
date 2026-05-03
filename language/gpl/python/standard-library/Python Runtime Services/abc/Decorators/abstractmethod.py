# %%
# @abstractmethod -- mark a method as required by subclasses.
# The class containing it must use ABCMeta (typically by inheriting from ABC),
# otherwise the decorator is silently ignored.

from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def read(self, key: str) -> bytes: ...

    @abstractmethod
    def write(self, key: str, value: bytes) -> None: ...


# Storage()                # TypeError: Can't instantiate abstract class

# %%
# Combining with @property -- declare a required attribute-style accessor.
# `@abstractmethod` must be the INNERMOST decorator (closest to the function).


class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels(self) -> int: ...


class Car(Vehicle):
    @property
    def wheels(self):
        return 4


Car().wheels  # 4

# %%
# Combining with @classmethod / @staticmethod -- same rule, abstractmethod innermost.


class Parser(ABC):
    @classmethod
    @abstractmethod
    def from_str(cls, s: str): ...

    @staticmethod
    @abstractmethod
    def supported_formats() -> list[str]: ...


# %%
# An abstract method MAY have a body. Subclasses can call it via super().
# Useful when subclasses must extend, not replace.
class Processor(ABC):
    @abstractmethod
    def run(self):
        # shared setup -- subclasses must call super().run()
        print("setting up")


class JobProcessor(Processor):
    def run(self):
        super().run()  # reuse the abstract base's body
        print("doing job")


JobProcessor().run()
# setting up
# doing job

# %%
# Deprecated decorators (DO NOT USE):
#   @abstractproperty       -- use @property + @abstractmethod
#   @abstractclassmethod    -- use @classmethod + @abstractmethod
#   @abstractstaticmethod   -- use @staticmethod + @abstractmethod

# %%
# Gotcha: forgetting to inherit from ABC (or use ABCMeta) makes @abstractmethod a no-op.
class NotActuallyAbstract:  # no ABC base!
    @abstractmethod
    def must_implement(self): ...


NotActuallyAbstract()  # works -- the decorator is silently ignored
