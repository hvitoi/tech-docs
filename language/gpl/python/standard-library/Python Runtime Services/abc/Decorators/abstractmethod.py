# %%
# @abstractmethod -- mark a method as required by subclasses.
# Only effective if the class uses ABCMeta (typically via inheriting ABC);
# without it, the decorator is silently ignored.

from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def read(self, key: str) -> bytes: ...


# %%
# Combine with @property / @classmethod / @staticmethod.
# @abstractmethod must be the INNERMOST decorator.
class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels(self) -> int: ...

    @classmethod
    @abstractmethod
    def from_str(cls, s: str): ...
