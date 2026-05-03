# %%
# `ABC` -- helper class to inherit from when defining an abstract base class.
# Equivalent to `class Foo(metaclass=ABCMeta): ...` but reads more like
# inheritance, so prefer it.

from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get(self, id): ...

    @abstractmethod
    def save(self, obj): ...


# %%
# Use ABCMeta directly only if you need a custom metaclass that *also* needs ABC behavior.
from abc import ABCMeta


class _MyMeta(ABCMeta):  # combines ABCMeta with whatever extra logic you want
    pass


class Custom(metaclass=_MyMeta):
    @abstractmethod
    def do(self): ...


# %%
# Implementations
class InMemoryRepo(Repository):
    def __init__(self):
        self._data = {}

    def get(self, id):
        return self._data.get(id)

    def save(self, obj):
        self._data[obj["id"]] = obj


repo = InMemoryRepo()
repo.save({"id": 1, "name": "x"})
repo.get(1)  # {'id': 1, 'name': 'x'}

# %%
# ABC instances can hold state in __init__ -- being abstract just means
# at least one method is not implemented.
class Cache(ABC):
    def __init__(self, ttl: int):
        self.ttl = ttl

    @abstractmethod
    def get(self, key: str): ...
