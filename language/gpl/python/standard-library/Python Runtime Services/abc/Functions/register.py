# %%
# ABC.register(cls) -- declare `cls` a "virtual subclass" without real
# inheritance. Affects isinstance / issubclass only; no methods are inherited
# and abstract methods are NOT enforced.
#
# Use it to make external/built-in types match your ABC.

from abc import ABC, abstractmethod


class JSONLike(ABC):
    @abstractmethod
    def to_json(self): ...


class TupleAdapter:
    def to_json(self):
        return "[...]"


JSONLike.register(TupleAdapter)
isinstance(TupleAdapter(), JSONLike)  # True

# %%
# This is how `collections.abc` matches built-ins -- via __subclasshook__
# (structural variant of register: any class with __len__ is Sized, etc.).
